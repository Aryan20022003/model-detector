#!/bin/bash

#create virtual environment
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Open new terminal and run RabbitMQ
gnome-terminal --window-with-profile=docker -e "docker run -d -p 5672:5672 rabbitmq"

sleep 10

gnome-terminal --window-with-profile=docker -e "bash -c 'cd ./app && celery -A main worker --loglevel=INFO &'"

# Open new terminal and run Python script
gnome-terminal --window-with-profile=docker -e "bash -c 'python3 -u run.py &'"

# Additional commands or setup steps can be added as needed
