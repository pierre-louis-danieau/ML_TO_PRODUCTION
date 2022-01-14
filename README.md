# Web App Machine-Learning Deployment on AWS

## Introduction :

- Deployment of NLP model into the cloud in AWS in order to make instant classification on a Tweet. We classify if a tweet has a disaster part (earthquake, floods...) or not.

- The main goal is not the Machine Learning part which is quite classic (TF-IDF matrix with Logistic regression) but the deployment part on AWS with EC2 instance.

## Short explanation on what I do to make instant classification accessible from the web everywhere and everytime

* [Part 1 : Develop the ML code in jupyter](#chapter1)

* [Part 2 : Creating a Webb app with Flask](#chapter2)
    * [Part 1.1 : Create an API with app routes](#section_1_1)
    * [Part 1.2 : Create an HTML file](#section_1_2)

* [Part 3 : Creating a Docker file with a requirements.txt](#chapter3)

* [Part 4 : Launch an Ec2 instance on AWS](#chapter4)
    * [Part 1.1 : Create and launch a Docker container](#section_1_1)

## Technical stack : 
- Machine Learning : Python, NLP, Tf-IDF, Logistic regression, joblib
- Deployment on cloud : AWS Ec2 instance
- Web App : Flask
- Docker

## Description : 
I take 3 inputs parameters (the location, keyword and message) and I predict whether the tweet is a disaster tweet or not.

![localhost aws](https://user-images.githubusercontent.com/67114372/140018017-96315b07-e1a2-4752-b428-d882dde01ae2.PNG)
----------------------------------------------------------------------------------------------------------------------------------------------------------------
![localhost aws2](https://user-images.githubusercontent.com/67114372/140018025-6faf503f-209e-472a-9338-c745ae7736f9.PNG)
