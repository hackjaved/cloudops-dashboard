#offical python image from dockerhub
FROM python:3.9-slim

#set working directory
WORKDIR /app

#DISPLAYS PYTHON OUTPUT IMMEDIATELY 
ENV PYTHONBUFFERED=1

#COPY DEPENDENCIES FILES
COPY requirements.txt .

#Install dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

#copy application source code
COPY app.py .

#Run as non-root user
RUN useradd --create-home appuser
USER appuser

#applciaion port
EXPOSE 5000

#run the flask application
CMD ["python", "app.py"]