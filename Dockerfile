FROM python:3.13

RUN pip install toml

WORKDIR /app/

COPY ./content /app/content
COPY ./convert.py /app/convert.py

RUN python convert.py

CMD [ "bash" ]