# Project Title

Project for creating two API for creating and fetching coupons

## Description

In this project we create discount code for brand and then fetches it for redemption

## Getting Started

Below are the steps needed to run the application

### Dependencies

* Python >= 3.5

### Executing program

* Download or clone the repository in your system.
* Create virtual environment and activate it.
* Run requirements.txt file to install required modules.
```
pip install -r requirements.txt
```
* Update the environment variables in .env file
* Build the image of the project by running the below command
```
docker build -t api_application .
```
* Change the parameters in docker-compose.yml file according to your environment like image name, container etc
* Run docker compose command command
```
docker run -p 5000:5000 -d api_application
```
* To test it locally run the run.py file in pycharm and try hitting the endpoints using POSTMAN.

## Authors

Lalit

## Version History

* 0.1
    * Initial Release