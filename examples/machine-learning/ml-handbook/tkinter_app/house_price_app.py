# house_price_app.py – run with:  python house_price_app.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import model_service as ms

FIELD_LABELS = {"area_m2": "Area (m²)", "bedrooms": "Bedrooms", "age_years": "Age (years)",
                "distance_km": "Distance to centre (km)", "has_garden": "Garden (1 = yes, 0 = no)"}


class HousePriceApp:
    def __init__(self, root):
        self.root = root
        root.title("House Price Predictor")
        root.geometry("640x440")
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True, padx=8, pady=8)
        self.train_tab = self._add_tab("1  Train")
        self.predict_tab = self._add_tab("2  Predict")
        self.update_tab = self._add_tab("3  Update with new data")
        self.history_tab = self._add_tab("4  History")
        self._build_train_tab()
        self._build_predict_tab()
        self._build_update_tab()
        self._build_history_tab()
        self.status = ttk.Label(root, text="", relief="sunken", anchor="w", padding=4)   # bottom bar: which model is live
        self.status.pack(fill="x", side="bottom")
        self.refresh_versions()

    def _add_tab(self, title):
        frame = ttk.Frame(self.tabs, padding=12)
        self.tabs.add(frame, text=title)
        return frame

    # ---------- tab 1: train ----------
    def _build_train_tab(self):
        self.train_path = tk.StringVar(value="houses_2025.csv")
        ttk.Label(self.train_tab, text="Training data (CSV):").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.train_tab, textvariable=self.train_path, width=45).grid(row=0, column=1, padx=6)
        ttk.Button(self.train_tab, text="Browse…", command=lambda: self._browse(self.train_path)).grid(row=0, column=2)
        ttk.Button(self.train_tab, text="Train & save model", command=self.on_train).grid(row=1, column=1, pady=12, sticky="w")
        self.train_result = tk.Text(self.train_tab, height=10, width=72)
        self.train_result.grid(row=2, column=0, columnspan=3)

    def on_train(self):
        try:
            version, metrics = ms.train_first_model(self.train_path.get())
        except Exception as problem:                                  # show any error in a pop-up instead of crashing
            messagebox.showerror("Training failed", str(problem))
            return
        self._write(self.train_result, f"Model saved as version {version}\n"
                                       f"Test error (MAE): ${metrics['mae']:,}\nR²: {metrics['r2']}")
        self.refresh_versions()

    # ---------- tab 2: predict ----------
    def _build_predict_tab(self):
        ttk.Label(self.predict_tab, text="Model version:").grid(row=0, column=0, sticky="w")
        self.version_choice = ttk.Combobox(self.predict_tab, width=10, state="readonly")
        self.version_choice.grid(row=0, column=1, sticky="w", pady=4)
        self.inputs = {}
        defaults = {"area_m2": "120", "bedrooms": "3", "age_years": "15", "distance_km": "4", "has_garden": "1"}
        for i, name in enumerate(ms.FEATURES, start=1):
            ttk.Label(self.predict_tab, text=FIELD_LABELS[name]).grid(row=i, column=0, sticky="w", pady=3)
            entry = ttk.Entry(self.predict_tab, width=12)
            entry.insert(0, defaults[name])
            entry.grid(row=i, column=1, sticky="w")
            self.inputs[name] = entry
        ttk.Button(self.predict_tab, text="Predict price", command=self.on_predict).grid(row=7, column=1, sticky="w", pady=10)
        self.price_label = ttk.Label(self.predict_tab, text="", font=("Arial", 16, "bold"))
        self.price_label.grid(row=8, column=0, columnspan=3, sticky="w")

    def on_predict(self):
        values = {name: entry.get() for name, entry in self.inputs.items()}
        chosen = self.version_choice.get()
        version = int(chosen.replace("v", "").split()[0]) if chosen else None
        try:
            price, used = ms.predict_price(values, version)
        except (ValueError, FileNotFoundError) as problem:
            messagebox.showwarning("Cannot predict", str(problem))
            return
        self.price_label.config(text=f"Predicted price: ${price:,.0f}   (model v{used})")

    # ---------- tab 3: update ----------
    def _build_update_tab(self):
        self.new_path = tk.StringVar(value="houses_2026_new.csv")
        ttk.Label(self.update_tab, text="New data (CSV):").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.update_tab, textvariable=self.new_path, width=45).grid(row=0, column=1, padx=6)
        ttk.Button(self.update_tab, text="Browse…", command=lambda: self._browse(self.new_path)).grid(row=0, column=2)
        ttk.Button(self.update_tab, text="Update model with new data", command=self.on_update).grid(row=1, column=1, pady=12, sticky="w")
        self.update_result = tk.Text(self.update_tab, height=10, width=72)
        self.update_result.grid(row=2, column=0, columnspan=3)

    def on_update(self):
        try:
            r = ms.update_with_new_data(self.new_path.get())
        except Exception as problem:
            messagebox.showerror("Update failed", str(problem))
            return
        verdict = "NEW model is better -> now current" if r["promoted"] else "OLD model kept as current"
        self._write(self.update_result,
                    f"Error of current model v{r['old_version']} on the new data: ${r['old_mae_on_new_data']:,}\n"
                    f"Error of retrained model v{r['new_version']} on the new data: ${r['new_mae_on_new_data']:,}\n\n{verdict}")
        self.refresh_versions()

    # ---------- tab 4: history ----------
    def _build_history_tab(self):
        cols = ("version", "saved_at", "rows_used", "mae", "r2", "current")
        self.table = ttk.Treeview(self.history_tab, columns=cols, show="headings", height=10)
        widths = {"version": 70, "saved_at": 140, "rows_used": 90, "mae": 90, "r2": 70, "current": 80}
        for c in cols:
            self.table.heading(c, text=c)
            self.table.column(c, width=widths[c], anchor="center")
        self.table.pack(fill="both", expand=True)
        buttons = ttk.Frame(self.history_tab)
        buttons.pack(pady=8)
        ttk.Button(buttons, text="Refresh", command=self.refresh_versions).pack(side="left", padx=4)
        ttk.Button(buttons, text="Make selected version current (rollback)", command=self.on_rollback).pack(side="left", padx=4)

    def on_rollback(self):
        selected = self.table.selection()
        if not selected:
            messagebox.showinfo("Rollback", "Select a version in the table first.")
            return
        version = int(self.table.item(selected[0])["values"][0])
        ms.rollback(version)
        self.refresh_versions()

    # ---------- helpers ----------
    def refresh_versions(self):
        h = ms.history()
        current = ms.current_version()
        self.status.config(text=f"The app is now using model v{current}" if current else "No model yet – train one in tab 1")
        self.table.delete(*self.table.get_children())
        for _, row in h.iterrows():
            self.table.insert("", "end", values=[row[c] for c in ("version", "saved_at", "rows_used", "mae", "r2", "current")])
        names = [f"v{v} (current)" if cur else f"v{v}" for v, cur in zip(h.get("version", []), h.get("current", []))]
        self.version_choice["values"] = names
        current_name = [n for n in names if "current" in n]
        self.version_choice.set(current_name[0] if current_name else "")      # predictions use the current model by default

    def _browse(self, variable):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            variable.set(path)

    @staticmethod
    def _write(box, text):
        box.delete("1.0", "end")
        box.insert("end", text)


if __name__ == "__main__":
    root = tk.Tk()
    HousePriceApp(root)
    root.mainloop()
