FROM python:3.10

WORKDIR /vkbot

COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

CMD ["python3", "main.py"]