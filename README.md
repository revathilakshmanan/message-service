# message-service
 Overview :The Message Service is a RESTful API built with Flask and PostgreSQL for managing messages. It provides endpoints to create, retrieve, and search for messages by various criteria. The service is containerized with Docker and deployed on Kubernetes with automated CI/CD using Jenkins.
## Setup -Local Development 
1. Clone the repository: ```bash git clone https://github.com/message-service/message-service.git cd message-service 
2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3.Install dependencies
pip install -r requirements.txt
4.Set up PostgreSQL and update the config.py with your database URI
5.Run the application
  flask run
# Docker Setup
 docker build -t message-service .
 docker run -d -p 5000:5000 message-service
# Kubernets setup
  kubectl apply -f kubernets/
# CI/CD Jenkins
   Set up a Jenkins pipeline using the provided Jenkinsfile to automate building, testing, and deploying the service.
# Terraform Setup:
  Use the provided Terraform scripts to set up an EKS cluster on AWS.
  terraform init
  terraform apply
  

