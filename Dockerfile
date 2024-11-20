FROM python:3

COPY . .
RUN pip install pandas

CMD ["python", "app.py"]