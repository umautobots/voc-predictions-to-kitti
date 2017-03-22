FROM python:3.6
COPY "doit.py" /usr/src/myapp/
WORKDIR /usr/src/myapp
ENTRYPOINT ["python"]
CMD ["doit.py"]