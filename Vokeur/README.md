# Vo-keur 

Lars de Roos | Web Apps Project

### Overview of all relevant files in the /vokeur folder:
#### manage.py
This is the file which runs the entire website via `python3 manage.py runserver`. 

### Overview of all relevant files in the /website folder:
#### /static/website/
This folder contains the following files:

- script.js (which contains the javascript that makes this project work as it should).
- mouse.js (which contains the javascript that makes the mouse shoot beer).
- styles.scss, styles.css (which makes the project look a whole lot better).
- hover-min.css (which makes the buttons do crazy things).

#### /templates
This folder contains the following files:

- layout.html (the layout for all pages, including the navbar and background).
- index.html (the main page for users).
- kieswijzer.html (the 'kieswijzer').
- verenigingen.html and vereniging.html (the pages where all 'verenigingen' can be found).
- woorden.html (the 'woordenboek').
- contact.html (the contact info page).

#### /media
This folder contains all images used for the 'verenigingen'.

#### admin.py and models.py
This is where all models are created and activated to create a database/dataset.

#### urls.py
This is where all urls are created.

#### views.py
This is the main python file, which consists of all the important python code to get everything working.
