# Use a base image with a minimal Linux distribution
FROM alpine:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the project into the container
COPY . .

# Install required packages
RUN apk add --no-cache \
    curl \
    ffmpeg \
    python3 \
    py3-pip \
    && pip3 install --upgrade yt-dlp

# Make the script executable (if needed)
RUN chmod +x dl.bash

# Run the bash script when the container starts
CMD ["sh", "dl.bash"]
