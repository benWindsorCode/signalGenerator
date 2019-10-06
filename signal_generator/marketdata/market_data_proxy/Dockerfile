FROM python:3.7-slim
COPY . /app
Expose 5010
WORKDIR /app
RUN pip install -r market_data_proxy_requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

