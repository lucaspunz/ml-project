FROM python:3.11.6
WORKDIR /app
COPY api/ /app/api/
COPY models/ /app/models/
COPY cleaned_dataset.csv /app
COPY emails.csv /app
RUN pip install --no-cache-dir -r api/requirements.txt
EXPOSE 5001
CMD ["python", "api/app.py"]