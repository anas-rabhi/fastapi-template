# Warning you have to build image from root directory of the project,
# if you try to construct it into current folder this will not work

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements/api_requirements.txt control_api/requirements/api_requirements.txt

RUN pip install -r control_api/requirements/api_requirements.txt


# Define the name of the directory into which the command are run
# if the directory doesn't exist it will be created
WORKDIR "/fastapi-template"