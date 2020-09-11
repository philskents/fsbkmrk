FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./api/requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./api /code/
ENTRYPOINT ["waitress-serve"]
CMD ["api:app"]
