# First of all specify Python version from dockerhub
FROM python:3.10

# Then make directory 
RUN mkdir fastapi_app

# Choose it as a working dir 
WORKDIR /fastapi_app

# The command tells which files from the project are copied and where.
# In this case we copy requirements.txt to root dir of the image
COPY requirements.txt .

# This command is executed from shell. RUN comands are launched single
# time when creating an image. So it differs from CMD commands.
RUN pip3 install -r requirements.txt

# Copy the whole project into root dir within the image
COPY . .

# This command  will be executed every time we run the container
CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000