# I think therefore I Blog: Codestar

## Purpose: 
Employ design thinking within an agile development process to create a full-featured blog via a database-backed Django application.

## Key Learning: 
* Create a database-backed Django app and deploy it to Heroku. 
* How to host uploaded images on a Cloud provider. 
* How to create class-based views in a Django project.
* How to use Django generic views, how to add authentication.
* Create custom models, and 
* Add extra interactivity using JavaScript

## User Stories:
[On GitHub](https://github.com/users/roeszler/projects/3/views/1)

* View post list: As a Site User I can view a list of posts so that I can select one to read
* Open a post: As a Site User I can click on a post so that I can read the full text
* View likes: As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
* View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation
* Account registration: As a Site User I can register an account so that I can comment and like
* Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation
* Like / Unlike: As a Site User I can like or unlike a post so that I can interact with the content
* Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
* Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later
* Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

## DATABASE MODELS:

Django is a MVT or Model, View, Template framework:

The model is our database and structure, 
The templates are the HTML pages that our user sees,
The views are the glue that holds the two of them together 
The logic in our code that reads from (or updates) the model and then updates what the user sees.

Blog variables:

* title
* author  
* updated date
* main content 
* number of likes
* number of comments

What kinds of fields are these?  

[Relationship Diagram](https://docs.google.com/spreadsheets/d/1Bq74KutSfTbplOzb7bEvSfRpMtyyOreDQ4OC_nWXpQI/edit?usp=sharing)

![Relationship Diagram](/static/images/relationship-diagram-blog.png)

## Future updates
1. Expand the messaging system as mentioned in our previous video
	- Have error messages displaying when a user submits an empty comment form,
	- Success messages.
2. Social apps feature of AllAuth to add single sign-on functionality using Google, Facebook, or another authentication provider.
3. Build a number_of_comments method so that the number of comments can be shown on the front page as well as the number of likes.
4. Combine your knowledge of the JavaScript fetch API with your Django 
	- Change the like functionality so that it calls the like URL in the background and doesn't reload the page
