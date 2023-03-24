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

## Env Vars

 - `USERS_ENDPOINT` - An optional variable to set the path of the Users endpoint, defaulted to `/api/v1/users`
 - `COMMENTS_ENDPOINT` - An optional variable to set the path of the Comments endpoint, defaulted to `/api/v1/comments`
 - `API_HOSTNAME` - The hostname for the backend API.  There is no default, a good value would be `python-api-sample.example.com`.
