# Django Blog Project

This is a minimal blog project using Django.
Project is deployed to Heroku at https://django-blog-2021.herokuapp.com/
## Quick Links
* [Introduction](#introduction)
* [Installation Guide](#installation-guide)

## Introduction

Some of the functionalities you would see in this app : <br>
    * Posts details, listing, creating updating and deleting using Django generic views. <br>
    * User new photo upload or update with default photo already set for newly-created profiles. <br>
    * Holding media files with S3Boto3Storage MediaStore container. <br>
    * Serving media files from AWS S3 Bucket. <br>
    * User authentication for routes with login and logout functionalities. <br>
    * Reset user password email. See note #4 below. <br>
    * Using django-on-heroku to set the settings for deploying the app to Heroku.

## Installation Guide

To set up your environment, follow these steps:<br>
   1. Create a project directory by going to Terminal and typing `mkdir project_name`. 
   2. Type `cd project_name`
   3. Now let's create a new virtual environment. To automatically create and manage a virtualenv for the project, we need to install:
   
   - `Pipx`:  
      - Pipxis a tool to help you install and run end-user applications written in Python. It installs applications into an isolated and clean environment on their own. To install pipx, just run: `pip install --user pipx`. Once you have `pipx` ready on your system, continue to..
- `Pipenv`: 
    - `pipx install pipenv`

4. Now we can create the new environment by running `pipenv shell`. If you check the project directory, you will notice that a new Pipfile has been created.

5. To install packages required for this project, either:
   - run `pipenv install` which will automatically import the contents of `requirements.txt` file and create a `Pipefile`, OR
   -  run `pipenv install -r ./requirements.txt` by specifying the path to the file.
   
   If you wannt to make sure if installation was successfull, run `pipenv lock -r` to display the list of installed packages. You can also print a graph of all installed dependencies by running `pipenv graph`.

    --- 
## :warning: Note 1

if step 4-5 didn't work, run `pipenv lock` then `pipenv install --ignore-pipfile`. This will install all packages and their dependencies using the pipfile.lock and will ignore the pipfile.

## :warning: Note 2
if installation was not successful, try installing packages for development environments. Run `pipenv install r ./requirements.txt --dev`

## :warning: Note 3

You might need to upgrade the packages. 

First, check by running `pipenv update --outdated` to see what's changed upstream. If you need to upgrade, you have two options:
1. upgrade everything by running `pipenv update`.
2. upgrade one package at a time by running `pipenv update <pkg>` for each outdated package.

## :heavy_exclamation_mark: Note 4
For resetting the password for a User, you need to make sure the following applies:
* You need to go to https://www.google.com/settings/security/lesssecureapps and allow access. Do not forget to switch it off after you finish.
* You need to go to https://accounts.google.com/DisplayUnlockCaptcha and allow access.
* Send reset-password email to the same email-address set in user profile.






