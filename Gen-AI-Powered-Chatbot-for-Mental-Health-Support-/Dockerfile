# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
