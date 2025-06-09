# Dockerfile
ARG JUPYTER_IMAGE_VERSION
FROM jupyter/datascience-notebook:${JUPYTER_IMAGE_VERSION}

# Install dotenv
RUN pip install python-dotenv

# Set environment variables from .env file
#COPY .env /home/jovyan/.env
RUN echo "source /home/jovyan/.env" >> /home/jovyan/.bashrc