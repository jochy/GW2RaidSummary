# Install dependencies
Run the following command in order to install the required dependencies: `pip install -r requirements.txt`

# Start web server
Run the following command: `flask run`

# Build docker image
To build the docker image, please run the following command: `docker build -t gw2/raid-summary:<TAG>`

# Run the docker image
In order to run the docker image, please run the following command: `docker run -p 80:80 gw2/raid-summary:<TAG>`
