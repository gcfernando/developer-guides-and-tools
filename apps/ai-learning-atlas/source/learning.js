/* Learning controls extend the existing canonical checkbox/progress mechanism. */
(() => {
  'use strict';
  const select = document.getElementById('lesson-focus');
  const lessons = Array.from(document.querySelectorAll('.lesson'));
  const note = document.getElementById('study-note');
  const noteStatus = document.getElementById('study-note-status');
  const noteKey = 'ai-atlas-study-note-v1';
  const showLesson = id => {
    select.value = lessons.some(x => x.id === id) ? id : '';
    lessons.forEach(lesson => { lesson.hidden = !!select.value && lesson.id !== select.value; });
  };
  select.addEventListener('change', () => showLesson(select.value));
  // Reveal hidden lesson destinations before native navigation, including search results.
  const reveal = hash => {
    let id;
    try { id = decodeURIComponent(hash.replace(/^#/, '')); } catch { return; }
    const target = document.getElementById(id);
    const lesson = target?.closest('.lesson');
    if (lesson) showLesson(lesson.id);
  };
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (link) reveal(link.getAttribute('href'));
  }, true);
  window.addEventListener('hashchange', () => reveal(location.hash));
  showLesson('lesson-setup');
  reveal(location.hash);
  const update = () => {
    const practice = lessons.filter(x => x.querySelector('[id$="-practice"]').checked).length;
    const transfer = lessons.filter(x => x.querySelector('[id$="-transfer"]').checked).length;
    document.getElementById('lesson-counter').textContent = `${practice} of ${lessons.length} guided exercises; ${transfer} of ${lessons.length} independent variations self-reported. These do not automatically complete topic scopes.`;
  };
  document.querySelectorAll('.save-check').forEach(c => c.addEventListener('change', update));
  document.addEventListener('atlas-progress-restored', update);
  document.getElementById('reset-progress').addEventListener('click', () => setTimeout(update, 0));
  try { note.value = localStorage.getItem(noteKey) || ''; }
  catch { noteStatus.textContent = 'Storage unavailable; copy your note or export a backup.'; }
  const countNote=()=>{document.getElementById('study-note-count').textContent=`${note.value.length.toLocaleString()} / 50,000 characters${note.value.length>50000?' — existing note exceeds the backup limit; copy it before shortening.':''}`;};
  countNote();
  document.addEventListener('atlas-progress-restored',countNote);
  note.addEventListener('input', () => {
    countNote();
    try { localStorage.setItem(noteKey, note.value); noteStatus.textContent = 'Note saved in this browser.'; }
    catch { noteStatus.textContent = 'Storage unavailable; copy your note or export a backup.'; }
  });
  document.getElementById('copy-study-note').addEventListener('click', async () => {
    noteStatus.textContent = await copyText(note.value) ? 'Note copied.' : 'Copy unavailable; select and copy the note manually.';
  });
  update();
})();
