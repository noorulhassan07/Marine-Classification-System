# ** Ocean Life Classification System **

## Introduction

The Ocean life Classification classifies the marine life under the ocean. This system based on CNN-ResNet50 architechure which used for the Deep Learning systems.
The dataset is taken from Kaggle with the following link:
(https://www.kaggle.com/datasets/sigmakhanam/fish-detection)
In this dataset we have multiple classes related of Marine Species such as Corals, Clams, Fish, Octupus, Dolphins and Whales and other speices. The system is based on streamlit and flask framework. Streamlit is used in Frontend and Flask is used for backend.


## Why useful?

This classification is useful for:

- Students who wants to study the marine speices.
- Marine Drivers who wants to ensure that which speice they see in the ocean.
- Researchers who wants to reasearch on marine species using deep learning classification.

## Deployment

The system is deployed on Docker Desktop WSL server, the easy and useful way to deploy the frontend and backend in the container which are easy to maintain.

### How to run on docker

1. Create the following files:
	
	i. backend/Dockerfile
   ii. frontend/Dockerfile
  iii. docker-compose.yml

These files will hold the power to to create the containers and images in the Docker Desktop.

2. In terminal or CMD, run the following commands step by step

```
docker-compose build
```
```
docker-compose up
```
Make sure your docker desktop is running in background, so it will not throw an error.

There you will see the ports allocated to backend and frontend:

frontend -> http://localhost:8501
backend -> http://localhost:5000

### Model Training

Model was trained on Kaggle Notebook with the dataset (https://www.kaggle.com/datasets/sigmakhanam/fish-detection) with GPU T4x2.
The accuracy were observed per epoch and the esimated Accuracy were observed was 81.19% in Phase 1 and 91.36% in Phase 2. 
The graph plo