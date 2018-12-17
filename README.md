###### Ramanathan Annes
## Problem Solver

Welcome to Problem Solver, a community-driven site where you can report bugs or request features. If user want immediate responses from admin user have to pay for that. These money help us improve our site.  

## UX
These website help user to fix there problem in coding and user can request there feature to help improve the website.These project is presented simply so user can easily understand what they can do. 
* In Initial commit I accidentally added my secret key, in real world projects I am sure I am not going to added that If I did I will change my secret key.
* If user didn't  reply even though that solution worked the status of issue will never changed by admin.
 
* Advantages of making payment for high priority in issues is user can edit issues and they will get immediate response from admin and also they can see how many views they got for there issue.

Overall my target audience are amature in coding and freshers to these coding life. [Wireframe](https://files.slack.com/files-pri/T0L30B202-FESFD5X7D/image.png) 

## Features
### Existing Features
 - website have user login and user register 
 - user can add issues using add issue form
 - user can search the issues 
 - other user can also help users to solve their issues by comment form

### Features Left to Implement
 - already planned to add dislike and like button using ajax and django but not yet implemented

### Technologies Used 
In this section, I  mention main languages, frameworks, libraries, and any other tools that I used to construct this project.
  - [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/): 
       * I used a **Bootstrap** for Responsiveness and Grid
  - [Django](https://docs.djangoproject.com/en/2.1/): 
     * The whole project mainly depend on **Django**.
  - [Materialize css](https://materializecss.com/):
      * I used **materializecss** for icons and nav-mobile view. 
  - [AWS](https://aws.amazon.com/):
      * I used **AWS** to host my static and image files.
  - [Stripe](https://stripe.com/gb)
     * Used **stripe** for payment because stripe will do secure stuffs we don't have to worry
  - [Chart js](https://www.chartjs.org/)
     * Used  **chart js** to show working proccess by chart
  

### Testing
[![Build Status](https://travis-ci.org/Ramanathan03/Issue-tracker.svg?branch=master)](https://travis-ci.org/Ramanathan03/Issue-tracker)

For testing I used Travis and django testcase. In django testcase I tested every single app and few other views and forms. for examples,

**tested_add_issue_form** Reason for these test is to check the add issue form cannot be created only with title I mean the user have to fill the every single field. Result: these test is passed.

**tested_search_view_and_index_page** reason for tested these to check the url is occured and to see that both views are using right templates. result:These test are passed


Another way I tested the website acted like user to check the functionality is working 

| Functional      | Expected Output Y/N          | Pass Y/N| Explaination of the Functionality 
| ------------- |:-------------:| -----:|---:|
|Registration|Yes|Yes|Registration form is simple like other register form If user new to website they have to register their detail|
|Login|Yes|Yes|If user already have account in these website they can access straight away with login form.|
|Add issue|Yes|Yes|If user can't find their issue in these site they can add it then we will reply depend on priority|
|edit issue|Yes|Yes|user can edit issue but these functionality only for user who paid for the issue otherwise the edit button it won't display on the page|
|search|Yes|Yes|user can search issue |

##### Different screen sizes:
   I used  **Chrome development tool** to testing my website responsible  in smaller screen and in large screen.
   
   - The website is quite responsive and works best on both large middle and small screen.
   - The look and feel remains the same in different sizes

### Deployment 
This project was deployed on Heroku 
###### Here is the way to I depolyed to heroku 
 - git remote add heroku 
 - create procfile 
 - used Gunicorn  WSGI web application in procfile
 - Push to Heroku --> $ git push heroku master
 
* Procfile will help to declares types -> web
 [Website](https://ps-issue.herokuapp.com/)

##### Config Vars --> IP = 0.0.0.0, PORT = 5000

## Credits

### Acknowledgements
Code Institute Mentor **Chris Zielinski** 



