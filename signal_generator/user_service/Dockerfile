FROM python:3.7
COPY . /app
Expose 5000
WORKDIR /app
RUN pip install -r user_service_requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

