FROM python:3.7.7-alpine

WORKDIR /usr/bin

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "thanos_snap.py" ]

CMD ["--help"]