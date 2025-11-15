FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /gateway

COPY requirements.txt /gateway/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /gateway/

RUN chmod +x /gateway/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/gateway/entrypoint.sh"]
