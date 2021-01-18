# Django Blog Project :rocket:

This is a minimal blog project using Django.
Project is deployed to Heroku at https://django-blog-2021.herokuapp.com/
## Quick Links
* [Introduction](#introduction)
* [Installation Guide](#installation-guide)
* [Create Dummy Posts](#create-dummy-posts)

## Introduction

Some of the functionalities you would see in this app : <br>
    * Posts details, listing, creating updating and deleting using Django generic views. <br>
    * User new photo upload or update with default photo already set for newly-created profiles. <br>
    * Holding media files with S3Boto3Storage MediaStore container. <br>
    * Serving media files from AWS S3 Bucket. <br>
    * User authentication for routes with login and logout functionalities. <br>
    * Reset user password email. See note #4 below. <br>
    * Using django-on-heroku to set the settings for deploying the app to Heroku.
    * Python shell commands to populate the blog with dummy posts for a specific User. See note #5 below.

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
## :arrow_forward: Note :one:

if step 4-5 didn't work, run `pipenv lock` then `pipenv install --ignore-pipfile`. This will install all packages and their dependencies using the pipfile.lock and will ignore the pipfile.

## :arrow_forward: Note :two:
if installation was not successful, try installing packages for development environments. Run `pipenv install r ./requirements.txt --dev`

## :arrow_forward: Note :three:

You might need to upgrade the packages. 

First, check by running `pipenv update --outdated` to see what's changed upstream. If you need to upgrade, you have two options:
1. upgrade everything by running `pipenv update`.
2. upgrade one package at a time by running `pipenv update <pkg>` for each outdated package.

## :arrow_forward: Note :three: :email:
For resetting the password for a User, you need to make sure the following applies:
* You need to go to https://www.google.com/settings/security/lesssecureapps and allow access. Do not forget to switch it off after you finish.
* You need to go to https://accounts.google.com/DisplayUnlockCaptcha and allow access.
* Send reset-password email to the same email-address set in user profile.


## Create Dummy Posts

For creating dummy posts for the blog, you will have a `dummy_posts.json` file in the root directory. 

First, please notice the following:
1. There is a comment on top of the file. Please remove it before running any code in the shell.

2. This file will create dummy posts for 5 users based on their `author_id`. Therefore, please make sure to create a mimimum of 5 users in the shell (you can change the `author_id` in the file if you want).
3. If you want to create an Admin User, change `user.is_superuser` in the file to `True`. Alternatively, you can create a Super User and define its `username` and `password` by typing the following in the shell later (though it is recommended to do that at the very first beginning): 
   
   `python3 manage.py createsuperuser`.


4. While creating the `User`, you can change the `username`, `password` and `email` of the `User` to anything you want.

5. Do not forget the indentation in the `for` loop when typing in the shell (by hitting the `tab` key on your keyboard).


6. Last but not least, please make sure you are in the right directory!


Now, start the shell in terminal: `python3 manage.py shell` then type the following code:

```
import json
from django.contrib.auth.models import User
from blog.models import Post

new_user = User.objects.create_user('Adrian_Holovaty', password='Holovaty15', email='adrian@django.com')
new_user.is_superuser=False
new_user.is_staff=True
new_user.save()

with open('dummy_posts.json') as f:
    posts = json.load(f)

for pos in posts:
    post = Post(title=pos['title'], content=pos['content'], author_id=new_user.id)
    post.save()

exit()
```
Now, check if there are issues by running `python3 manage.py check` . 

If there are none, start the development server `python3 manage.py runserver` and go to `http://127.0.0.1:8000/`

You should now see those dummy posts :tada: