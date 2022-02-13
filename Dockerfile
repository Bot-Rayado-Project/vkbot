FROM python:3.10

WORKDIR /vkbot

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]