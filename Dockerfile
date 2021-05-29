FROM python:3.8-slim-buster
WORKDIR /app
COPY CPIAUCNS.csv inflation.py ./
RUN chmod 755 inflation.py
ENTRYPOINT ["./inflation.py"]
CMD ["1975", "2020"]
