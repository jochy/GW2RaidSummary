FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY . /app
RUN pip install -r /app/requirements.txt
RUN mv /app/app.py /app/main.py