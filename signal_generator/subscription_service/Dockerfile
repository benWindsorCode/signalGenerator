FROM python:3.7-slim
COPY . /app
Expose 7000 
WORKDIR /app
RUN pip install -r subscription_service_requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

