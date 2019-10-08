FROM python:3.7-slim
COPY . /app
Expose 5000
WORKDIR /app
RUN pip install -r mock_stock_data_service_requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
