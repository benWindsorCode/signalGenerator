FROM python:3.7-slim
COPY . /app
Expose 5001
WORKDIR /app
RUN pip install -r crypto_data_service_requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
