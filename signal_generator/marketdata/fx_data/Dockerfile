FROM python:3.7-slim
COPY . /app
Expose 5002
WORKDIR /app
RUN pip install -r fx_data_service_requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
