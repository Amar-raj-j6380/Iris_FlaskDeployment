FROM python:3.8-slim-buster  
# intsall python and os
WORKDIR /flask-docker2
# in the container create the folder

# upgrade to latest version
RUN python3 -m pip install --upgrade pip 
# building stage
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# cmd when run the image on container mjjjjjj kdkandkkjaknkda
