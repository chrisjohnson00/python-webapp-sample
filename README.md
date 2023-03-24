# python-webapp-sample
A sample Web App in Python with Flask

## PyPi Dependency updates

    docker run -it --rm -v ${PWD}:/repo -w /repo python:3.11.2-slim bash
    pip install --upgrade pip
    pip install --upgrade Flask gunicorn requests
    pip freeze > requirements.txt

## Running locally

```commandline
export FLASK_APP=webapp_sample
export API_HOSTNAME=localhost:5000
flask --debug run -p 5001
```
