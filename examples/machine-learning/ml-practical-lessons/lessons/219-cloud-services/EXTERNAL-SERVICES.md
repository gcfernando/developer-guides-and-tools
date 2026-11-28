# External services

## Cloud platforms

First run the Flask lesson (lesson 222 in the workbook) and try the valid and invalid CSV rows. These test requests run locally. Keeping the same request shape lets you check the service after deployment.

| PDF topic | Steps to try in your own account |
| --- | --- |
| AWS | Follow the Elastic Beanstalk Flask guide. Put the Flask app in `application.py`, expose the Flask object as `application`, and include the training CSV and dependencies. Send a request to `POST /predict` and compare with the Flask lesson. [AWS guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html) |
| Google Cloud | Follow the Python Cloud Run quickstart. Put the Flask app in `main.py`, expose the Flask object as `app`, and include the training CSV plus Flask, pandas, scikit-learn and Gunicorn. Follow the quickstart's authenticated deployment and send the same prediction request. [Google Cloud guide](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service) |
| Heroku | Follow the Python guide. Keep the Flask service in `application.py`, list the dependencies including Gunicorn, and add the process command `web: gunicorn application:app`. After deploying, send the same test rows to the endpoint. [Heroku guide](https://devcenter.heroku.com/articles/getting-started-with-python) |

Copy the Flask lesson code when preparing a project. Keep the route and remove the local test-client calls from the deployed module. Include the training CSV, keeping the same path expected by the code. Each platform uses its own account setup and deployment process.

## Tableau and Power BI

1. Run the Tableau or Power BI lesson. It creates `dashboard_import.csv` in the terminal's current folder.
2. In the BI application, import the CSV and plot `Accuracy` by `Batch`. Set accuracy to display as a percentage.
3. Change a row in the lesson's `sample.csv`, rerun the lesson, and refresh the source in the BI application.

## Web and mobile apps

Use the First API call from a web page lesson (lesson 232 in the workbook) for a browser example. For a mobile client, use the same method and path as the FastAPI lesson (lesson 221 in the workbook) and send JSON such as `{"distance_km": 5, "weight_kg": 2}`. The test table includes a negative distance so you can see what a rejected request looks like.
