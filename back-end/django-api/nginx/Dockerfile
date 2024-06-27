# Use the official nginx base image
FROM nginx:latest

# Copy the nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the necessary port
EXPOSE 80

# Start nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]