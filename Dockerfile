# Python image to use.
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
ENTRYPOINT ["python", "app.py"]