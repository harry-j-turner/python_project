FROM python:3.9
COPY requirements.txt /code/
WORKDIR /code/
RUN pip install -r requirements.txt
COPY src/ /code/
RUN ls /code/
ENTRYPOINT ["python","main.py"]
