# <img src="/static/images/logo.png" style="width:200px; height:auto">
K-Templates is a K-pop photocard collection template, where photocard collectors can customise their photocard wishlist to their liking. They are able to customise the photocards they want, and have almost full control of what their template looks like.

## Tables of Content
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Installation](#installation)
* [Future Features](#future-features)
* [About Me](#about-me)

## <a href="#tech-stack"></a> Tech Stack
__Front-End__: HTML5, JavaScript, jQuery, Bootstrap <br>
__Back-End__: Python, Flask, SQLAlchemy, PostgreSQL <br>

## <a href="#features"></a> Features
Users can log in, or register an account if they want to save their files for later use. <br>
Otherwise, guests can create a simple template without a login. <br>
On the Template Creator, users can search through all of the photocards, or even search for their favorite member. <br>
When users click on the photocard that they want, it will be added to the template. <br>
When they picked all the photocards they want, they can customise the template. <br>
Here, they can dynamically change the title and the font of the template, <br>
And change the colors of the background or the font! <br>
Lastly, using <a href="https://github.com/tsayen/dom-to-image">DOM-TO-IMAGE</a>, users can download their creation and have be of use on any social media platform they want for other collectors to know what photocards they are looking for!

## <a href="#installation"></a> Installation
To have the site run on your local computer, please do the following:
Clone Repository:
```
$ git clone https://github.com/malizas/k-templates.git
```
Create Virtual Environment:
```
$ virtualenv env
```
Activate the Virtual Environment:
```
$ source env/bin/activate
```
Install all necessary dependecies
```
$ pip3 install -r requirements.txt
```
Set up the Database:
```
$ createdb photocards
$ python3 model.py
$ python3 seed.py
```
Run the site:
```
$ python3 server.py
```
To access the site, go to "localhost:5000/", and have fun creating your very own templates!

## <a href="#future-features"></a> Future Features
* Give users the ability to add their own photocards
* More flexibility on the template creator that mimics photo editors, such as Pixlr or Photoshop
* Create a version that is compatible for phones
* Create a page feature for the photocards, that way users don't have to scroll through an endless amount of photocards.

## <a href="#about-me"></a> About Me
__Maliza Sivongsa__ is a software engineer in the Twin Cities are of Minnesota; this is their first project. Visit them on <a href="https://www.linkedin.com/in/malizasivongsa/">LinkedIn</a>