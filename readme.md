# Python Project Template

Welcome to the Python project template of the Institut for Acoustics and Dynamics.

## Goal

This project templates aims to support you with a framework that let's you recreate your plots and results. 
It is quite common problem, that after some time one is not able to recreating some plots and results due to changes in the code or missing infomration about the right parameter settings.
Here the framework provieds you with a workflow that saves the used settings as well as the used data for creating the plots.

## Getting started

In order to use the framework you will need to install the [sky package](https://github.com/JS273/sky). This contains some basic method that are common for different problems. So if you change something there it will be available for all your projects. For more details check the page of the sky package.
In order to install the sky package, you should use the editable install: ```pip install -e .``` This command should be called in the directory of the sky project. 

### Basic Structure

The template consists of the following foldersn and files:
- ```data``` tbd
- ```run```  Here should lie the main file of your program as well its configuration yaml file
- ```src```  contains the following subfolders:
  - ```models``` contains the your models. They are called by your main file in ```run```
  - ```utils```  contains
