FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
		redis-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000 6379
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]