# Pull base image
FROM python:3.10.2-slim-bullseye

# Set environment variables
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "/code/entrypoint.sh"]
