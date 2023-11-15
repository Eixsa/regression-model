# Regression Model

Building and deploying a regression ML model.

This code is used in this [blog post](https://www.tekhnoal.com/regression-model.html).

## Requirements

Python 3.8.0

## Installation 

The Makefile included with this project contains targets that help to automate several tasks.

To download the source code execute this command:

```bash
git clone https://github.com/schmidtbri/regression-model
```

Then create a virtual environment and activate it:

```bash
# go into the project directory
cd regression-model

# creation et activation d'un environement virtuel
.\venv\scripts\activate

Install the dependencies:

pip install -r requirements.txt

## Running the Service

To start the service locally, execute these commands:

```bash
uvicorn rest_model_service.main:app --reload
```

## Docker

To build a docker image for the service, run this command:

```bash
docker build -t insurance_charges_model:0.1.0 .
```

To run the image, execute this command:

```bash
docker run -d -p 80:80 insurance_charges_model:0.1.0
```

To watch the logs coming from the image, execute this command:

```bash
docker logs $(docker ps -lq)
```

To stop the docker image, execute this command:

```bash
docker kill $(docker ps -lq)
```
