# Vo-keur 

Lars de Roos | Web Apps Project

## Introduction
The number of students who join student associations has been falling for a long time. This is due to poor publicity and the costs of membership. Yet on the internet the question is often asked "Which student association suits me?". This web application has been designed to respond to this. It serves as a guide for student associations, to find the perfect match as a (future) student!

#### Check the website right here -> [Vo-keur](http://vokeur.herokuapp.com)
Note to user: 
- It also works on smartphones, so feel free to use your phone. 
- In the https version, [this version](https://vokeur.herokuapp.com), the Google Maps API does not work.

## Getting started 
Make sure that you have a copy of Python 3.7 or higher installed on your machine. You’ll also need to install pip. If you downloaded Python from Python’s website, you likely already have pip installed (you can check by running `pip` in a terminal window). If you don’t have it installed, be sure to install it before moving on!

1. Clone or download our GitHub repository
2. In a terminal window, navigate to the directory you saved this repository on.
3. Run `pip install -r requirements.txt` in your terminal window to make sure that all of the necessary Python packages are installed. 
4. In your terminal window, navigate to the `vokeur` folder.
5. Use `python3 manage.py runserver` to get started. 

If you want to view, change or add data to the models, go to: `http://127.0.0.1:8000/admin`.
Check `vokeur/website/views.py` (superuser) for the login details.

## Product video
A video walkthrough of this webapplication can be found via [this link](https://youtu.be/qxGKKuQUWag).
The video was recorded on a computer because, in my opinion, this gives a better overview of the content of the web application. Of course it is still possible to open it on a smartphone.

## Screenshots Computer (MacBook)
##### Homepage
![](doc/e1.png)
##### Kieswijzer begin
![](doc/e2.png)
##### Kieswijzer vragen
![](doc/e3.png)
##### Kieswijzer uitslag
![](doc/e4.png)
##### Verenigingen Leiden
![](doc/e5.png)
##### Vereniging uit Leiden
![](doc/e6.png)
##### Vereniging uit Leiden (Mail)
![](doc/e7.png)
##### Vereniging uit Leiden (Maps)
![](doc/e8.png)
##### Woordenboek
![](doc/e9.png)
##### Contact informatie
![](doc/e10.png)

## Screenshots Smartphone (iPhone)
![](doc/iphone1.PNG)
![](doc/iphone2.PNG)
![](doc/iphone3.PNG)

## Copyright Statement

##### Copyright Notice
Nobody else can use, copy, distribute, or modify my work without being at risk of take-downs, shake-downs, or litigation.
I am the only person who owns the rights to the materials in this repository! 

Copyright (c) 2019 - Lars de Roos.

##### Sources of external code, images and other materials 
Google Maps API is implemented under the Google Maps Platform License Agreement. Copyright (c) 2019 - Google.
This version was used: [link](https://developers.google.com/maps/documentation/javascript/adding-a-google-map?hl=nl).

Hover.css is made available under a MIT license. Copyright (c) 2017 - Ian Lunn.
`Vokeur/website/static/website/hover-min.css`

90's Cursor Effects is made available under a MIT license. Copyright (c) 2016 - Tim Holman.
`Vokeur/website/static/website/mouse.js`

The text effect "flash", which can be found in `Vokeur/website/static/website/styles.scss`, is from [this link](https://codepen.io/FrankieDoodie/pen/dgVGad).

The text effect "spinner", which can be found in `Vokeur/website/static/website/styles.scss`, is from [this link](https://canary---yellow.com). 

All images in `Vokeur/website/media` are from the facebook pages or websites of the used associations.

## Author
Lars de Roos

## Acknowledgements
Thanks to Marijn Jansen for all the guidance and advice I received during the development of this project. I also want to thank everyone who was involved in the organization of the minor Programming semester 2.
