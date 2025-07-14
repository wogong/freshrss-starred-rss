FROM python:3.12-slim

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . ./

EXPOSE 5000

# Environment variables are read from the environment or .env file at runtime
# You can pass them via `docker run -e FRESHRSS_URL=... -e FRESHRSS_USERNAME=... -e FRESHRSS_API_PASSWORD=...`
CMD ["python", "app.py"]