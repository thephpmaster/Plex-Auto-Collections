FROM python:3-slim
VOLUME /config

# Install Requirements
COPY requirements.txt /
RUN apt-get update && \
	apt-get upgrade -y --no-install-recommends && \
	apt-get install -y tzdata --no-install-recommends && \
	pip3 install --no-cache-dir --upgrade --requirement /requirements.txt && \
	apt-get autoremove -y && \
	apt-get clean && \
	rm -rf \
		/requirements.txt \
		/tmp/* \
		/var/tmp/* \
		/var/lib/apt/lists/*

# Download stopwords for keyword support
RUN python3 -c "import nltk; nltk.download('stopwords')"

# Copy now that requirements are all cached
COPY . /
RUN chmod +x /app/plex_auto_collections.py
WORKDIR /app

ENTRYPOINT ["python3", "plex_auto_collections.py"]