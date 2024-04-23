FROM python:3.8-slim-buster  
# intsall python and os
WORKDIR /flask-docker2
# in the container create the folder

# upgrade to latest version

# building stage
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m pip install --upgrade pip 
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# cmd when run the image on container mclsc ahah
