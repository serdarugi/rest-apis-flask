FROM python:3.10
# EXPOSE 5000 we used to use this but no longer we needed it since we are using gunicorn to run the app on port 80.
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80","app:create_app()"] 
# create_app() is a function that returns the Flask app instance. We are using this function to create the app instance and run it with gunicorn.
# guinicorn is a production WSGI server that is used to run the Flask app in production. It is a pre-fork worker model, which means that it forks multiple worker processes to handle requests. This allows for better performance and scalability.

