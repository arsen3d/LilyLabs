# Use an official PyTorch runtime as a parent image
FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-devel
ENV TEST=False

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN apt-get -y update
RUN apt-get -y install git
# Install Flask and any other needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000
WORKDIR /app
ENV PYTHONPATH=/app
# Run app.py when the container launches
CMD ["python","src/server/run.py", "--host=0.0.0.0", "--test=$TEST"]