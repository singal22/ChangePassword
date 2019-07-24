FROM python:alpine3.6
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "./app.py" ]