# Anomaly-detection-using-machine-learning

## Table of contents
* [Motivation](#Motivation)
* [Technologies](#technologies)
* [Dataset](#dataset)

## Motivation

There is a need to identify abnormalities in sensor data from equipment so as to predict faults in equipments way before they break down.
This project uses statistics concepts such as mean and variance to build  a fault detection algorithm using a sliding window that learns from the sensor data and makes prediction on possible faults.

	
## Technologies
Project is created with:
* jupyter notebook

Code is written in:
* Python

Methods used are:
* Statistics
* Data Visualization

## Dataset
The dataset for this project is 6 recordings of magnetic flux measured on a supra conducting magnet.

* Signal1 to Signal6 contains magnetic flux readings. Magnetic flux readings are regularly sampled signal (Te=5ms)

* Jump1 to Jump6 is a boolean signal of the same length as Signal. When a row in Jump1 to Jump6 is equal to 1, a flux jump is present. 
Jump1 to Jump6 thus localizes periods of time when a flux jump occurred.

* Dataset is saved in CSV file format.

