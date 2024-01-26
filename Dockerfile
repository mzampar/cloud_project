# Install dependencies
FROM nextcloud

RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        libbz2-dev; \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . /app