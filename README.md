# python-webapp-sample
A sample Web App in Python with Flask

## PyPi Dependency updates

    docker run -it --rm -v ${PWD}:/repo -w /repo python:3.11.2-slim bash
    pip install --upgrade pip
    pip install --upgrade Flask gunicorn
    pip freeze > requirements.txt
