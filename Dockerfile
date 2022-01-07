FROM python

WORKDIR /vkbot

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]