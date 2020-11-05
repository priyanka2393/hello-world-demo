FROM python:3.6
COPY .  /Hello_world
WORKDIR /Hello_world
RUN pip install -r requirements.txt
EXPOSE  8000
CMD ["python", "Hello_world/greet.py"]
