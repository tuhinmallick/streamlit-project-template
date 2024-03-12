FROM python:3.7@sha256:2011a37d2a08fe83dd9ff923e0f83bfd7290152e2e6afe359bde1453170d9bdc
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD bash run.sh