FROM python:3.10-slim

ADD rerequirements.txt .
RUN pip3 install -r requirements.txt

COPY dd.py dd.py

CMD ["python", "dd.py"]
