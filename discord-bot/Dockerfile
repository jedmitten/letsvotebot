FROM python:3.11-slim

RUN pip install --no-cache-dir uv

WORKDIR /app
COPY . .

RUN uv pip install --system -r requirements.txt

CMD ["python", "bot.py"]
