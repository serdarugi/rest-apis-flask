FROM python:3.11
EXPOSE 5000 
WORKDIR /app
RUN  pip install flask 
COPY . . 
# It means we have coppied entire file  " . " ( current directory contents to " . " current directory)
#Build anındaki proje dosyalarını image'ın içine kopyala.
CMD ["flask", "run", "--host", "0.0.0.0"]
