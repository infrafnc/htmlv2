FROM python:3-alpine

RUN apk update && apk add py-pip

RUN mkdir /aplicacao

COPY requirements.txt aplicacao/requirements.txt
WORKDIR /aplicacao
RUN pip install -r requirements.txt


COPY . /aplicacao

ENTRYPOINT [ "python3" ]

CMD [ "run.py" ]
