# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port for Streamlit (default is 8501)
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
