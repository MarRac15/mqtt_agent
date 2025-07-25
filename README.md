# MQTT Agent
Technical documentation


## Description:
What does the agent do:
- Creates MQTT client and connects to your MQTT broker (The Thing Stack/The Thing Network)
- Subscribes to MQTT topic and receives messages
- After receiving a message, it translates it to the Kafka format
- Finally, it saves** the message and sends it to Kafka topic.

** - Messages are stored in the msg_data.txt file, just in case the connection with Kafka is lost.

This agent is built in Python and uses paho-mqtt and python-kafka libraries. All the used packages are listed in the requirements.txt file.

## Local setup
Ensure your terminal working directory is in your project folder.
1. Create Python virtual environment using venv:
   ```bash
   python -m venv .venv
   ```
   The program should work on any newer version of Python, but if there are some conflicts then try using Python 3.11.9

2. Activate the virtual environment (Linux):
    ```bash
    source .venv/bin/activate
    ```

3. Make sure your current terminal instance is using the virtual environment:
    ```bash
    pip -V
    ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory of your project and add the following environment variables:
   ```bash
    
    MQTT_BROKER = <mqtt_broker_url>
    MQTT_PORT = <port>
    MQTT_TOPIC = <topic>
    USER = <username>
    API_KEY = <api_key>

    KAFKA_TOPIC = <kafka_topic>
    KAFKA_BOOTSTRAP_SERVER = <kafka_url>

    #FOR SSL:
    CERT_LOCATION = <path_to_cert.pem>
    KEY_LOCATION = <path_to_key.pem>
    SSL_PASSWORD = <secret_ssl_password>
   ```
   
    Warning: be careful to check if your environment variables names look exactly like this.

6. **If you're using SSL for connection with Kafka** (as I am), then create /certs folder in the root directory of the project and add there your cert.pem and key.pem files.


7. Compile main.py file in order to start the agent. 

    If the setup and connection were successfull, you'll see the following communicate in your terminal:
    
    ```
    Connected to MQTT Broker!
    ```

## Docker setup (deployment):
Create an .env file (just as described above) and add it to the root directory.

Similarly, create /certs folder in the root directory and place there your key.pem and cert.pem files.

**Make sure you are in the root directory of the project (not in the src folder!)**

There are 2 ways of running the container:
    
1. Run the following commands:
    ```
    docker build -t mqtt-agent .
    ```
    ```
    docker run \
    --env-file .env \
    -v $(pwd)/certs:/app/certs:ro \
    mqtt-agent
    ```

3. Alternatively, use docker compose (I added docker-compose.yaml file). Just execute this one command:
    ```
    docker-compose up
    ```

