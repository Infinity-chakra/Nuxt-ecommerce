# Use a slim Python base image
FROM python:3.9

# Set working directory
WORKDIR /usr/src/app

# Update package lists (optional, depending on your base image)
RUN apt-get update && apt-get upgrade -y  # Update package lists for Debian/Ubuntu-based images

# A command to see what's inside the container
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy your Django project code
COPY . .

# Expose port for Django development server (can be removed in production)
EXPOSE 8000

# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]