# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /markify

# Install any dependencies your project may require (if applicable)
# RUN npm install

# Copy the necessary files from your host into the container
# COPY . .

# Expose the required ports (80 for smtp4dev and 25 for SMTP)
EXPOSE 80
EXPOSE 25

# Command to run smtp4dev
CMD ["docker", "run", "--rm", "-it", "-p", "3000:80", "-p", "2525:25", "rnwood/smtp4dev"]
