FROM python:3

RUN git clone https://github.com/AGauchat/Tateti.git

WORKDIR /Tateti

RUN pip install -r requerimientos.txt

CMD [ "python3" , "./test_tateti.py" ]