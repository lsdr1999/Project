# Vo-keur 

Lars de Roos | Web Apps Project


Create a report (REPORT.md), based on your design document, containing important decisions that you’ve made, e.g. where you changed your mind during the past weeks. This is how you show the reviewer that you actually understand what you have done.


#### Introduction
The number of students who join student associations has been falling for a long time. This is due to poor publicity and the costs of membership. Yet on the internet the question is often asked "Which student association suits me?". This web application has been designed to respond to this. It serves as a guide for student associations, to find the perfect match as a (future) student!
![](doc/e4.png)

#### Technical design
For the first part of the technical design I like to refer to the `README.md` which is located in `/Vokeur`. This describes very briefly what can be found in each file or folder. 
Mainly the files that can be found in `/Vokeur/website/` are important. This is because this folder contains the `models.py` and `views.py` files. These are briefly explained below.

##### models.py

In models.py you can find the models that were used to store data and use it later. The following models have been created:

- Vragen, 
	- This model contains the questions that are used in the 'kieswijzer'.
- Antwoorden, 
	- This model contains the answer options
	- This model is linked to the 'Vragen' model.
- Stad, 
	- This model contains the cities that are part of this website (Groningen, Rotterdam, Leiden and Utrecht).
- Verenigingen, 
	- This model is the largest and is also the most important.
	- It contains all the information that is needed about an association in order to subsequently be able to make an overview (for example as in `verenigingen.html`) and also to distinguish in the 'kieswijzer' 
	- This is also the model that will be used most by the admin when new associations need to be added
	- This model is linked to the 'Stad' model.
- Verant, 
	- Short for 'Vereniging antwoord'	
	- This is the second most important model
	- It contains the associations' answers to the 'kieswijzer'
	- This model must also be adjusted by the admin when a new association is added
	- This model is linked to both the 'Steden' and 'Verenigingen' models and of course also to the 'Vragen' and 'Antwoorden' models. 
- Letter, 
	- This model contains the letters a to z, these are used for the dictionary.
- Woorden,
	- Short for 'Woordenboek'
	- This model contains all student words with their meaning
	- This model is linked to the 'Letter' model, because it was initially thought that it would be 'easy' to navigate through the words in this way (more on this later).

##### views.py

In views.py, the data that comes from models.py is used to render website components (html-pages). views.py consists of the following components:

- superuser,
	- A superuser account will be created here (if none already exists). This person becomes admin and can change models and add data.

- index,
	- The Homepage is loaded with this function. The information from the Stad model is included so that the drop-down menus of Kieswijzer and Verenigingen work.

- kieswijzer,
	- The 'Kieswijzer' page is loaded in this function. Because the 'kieswijzer' page is specific to a city, the name (of the city) is given as an argument. Subsequently almost all models are used to provide the 'kieswijzer' with the correct information. The 'kieswijzer' is mainly composed via JavaScript (`/website/static/website/script.js`) and uses 'uitslag' as a function to extract data from the models and compare this to generate a top 5 of 'best matches' (if there are 5 associations in that city).

- uitslag,
	- With this function, the data (unique per city, because the data from the 'kieswijzer' itself is sent here) that is sent from the Verant model to the 'kieswijzer' via a JsonResponse. This function actually serves to link the website and server, and thus the exchange of the data of the 'kieswijzer', filled in by the user, and of the answers entered by the associations.

- verenigingen,
	- The 'Verenigingen' page is loaded in this function.
Because the 'verenigingen' page is specific to a city, the name (of the city) is given as an argument. The models Verenigingen and Stad are used to present the right information regarding the associations.

- vereniging,
	- The 'Vereniging' page is loaded in this function.
Because the 'verenigingen' page is specific to a vereniging, the name (of the url, which is the short version of the name of the association) is given as an argument. The models Verenigingen and Stad are used to present the right information regarding the specific association.

- woorden,
	- Being probably the most fun function in views.py, this function loads the 'Woordenboek' page. The Letter and Woorden models are used to present the list of student words. Good luck learning them...

- contact,
	- The 'Contact' page is loaded with this function. The information from the Stad model is included so that the drop-down menus of Kieswijzer and Verenigingen work.

#### Challenges

When I look back on my DESIGN.md document I notice how much it matches the current product. The sketches are still accurate, except for the fact that an extra html page has been added ('Woordenboek'). Eventually an API was used, namely that of Google Maps. The tables for the database are also very similarly constructed, also here with the difference that new models have been introduced for the 'Woordenboek' page. The links between the tables have become slightly different, many ForeingKeys have been used to be able to use data among themselves and to make it unique. That is why the 'Verant' model was created (as a sort of ultimate gathering of all important parts of the database).
Below are some larger decisions that arise from the PROCESS.md:

Week 1 day 2: The public that I want to reach with the website are mainly (future) students. It can also be relavant for others, for example to get an overview of all associations that can be found in a certain city. We came to the conclusion that it fills a sort of gap, which of course is very nice since it can actually make a contribution.

Week 1 day 4: Larger choices with regard to the 'kieswijzer' have already been taken here. Consideration has already been given to the structure, presentation (transitions/slides), saving of data, performing comparisons and adding answers to associations. Because I started this so quickly, it helped a lot with setting up the 'kieswijzer'.

Week 2 day 2: Structuring associations and building a fully functional html, in which reference is made to a generated html per association and making a start with the 'kieswijzer' if there is time left this week. Those were the goals, the first of which was achieved fairly quickly. After consultation, it was later decided to opt for "Bootstrap Cards". This was decided because this would be a nice representation of the associations.

Week 2 day 4: Hopefully it will soon be possible to display the address via the Google Maps API. In addition, it is possible to send an email to the relevant association via the website. Both additions were successful.

Week 3 day 1: On this day the associations pages were completed, the Google API added and the 'kieswijzer' further thought out. For example, the following was now clear with regard to the 'kieswijzer': questions had to be consecutive/as a kind of quiz, be able to save data and perform comparison with associations in order to arrive at the 'best match'.

Week 3 day 2:
After quickly finding out that making such a quiz is not very easy, I chose to finish all other functionalities first. New modals have been built for the dictionary page and a large amount of data has been added (manually).

Week 3 day 3:
Extensive checks have been made to see why modals were displayed behind the other content, this is highly dependent on the type of browser. Safari can't handle it as it turns out. In addition, the entire layout of all parts of the website has been completed, texts are neatly centered and the display for an iPhone/smartphone has been optimized.

Week 3 day 5:
Today I have been able to fully focus on completing the 'kieswijzer'. Data can be stored via an Ajax request (JSON) and the data from the database is also sent via JSON to the website. The last part is now the comparison, with which I could make a start.

Week 4 day 1:
On the first day of this last week, I had to make sure that the comparison would actually give an outcome. After a short time programming it turned out to work. All the TODOs that I had prepared in previous weeks were therefore achieved.
I found out that a few optional goals from previous weeks were no longer necessary/feasible, these can be found at the `FutureWork` section of this document. For that reason there is now 'always' a beer mouse, the email styling has been adapted to a simple 'name and message' and no large pieces of text have been typed to support the whole (the website speaks for itself).

Week 4 day 2:
Today I have added over 20 associations, which together took almost 6 hours. This immediately made it clear that it would be unwise to keep this way of collecting data if there was more interest in developing this website. It also appeared that some associations had so little information available that it was decided not to add the association in question. In two cases it was not immediately possible to view the contribution, for this reason the 'standard amount' of € 100 was introduced.

Week 4 day 3:
Together with my tutor, I made sure that the website came online. For this we used Heroku. After everything was optimized and cleaned up, the website was shared with more than 30 people who could all provide feedback. For example, several people soon pointed out that the dictionary was not easy enough to read, which is why it was immediately adjusted.

#### Challenges - Conclusion
The choices that arise from the above challenges have led to progress. If a function was superfluous, it was immediately removed. Was a piece of design not as well thought or did it not work on smaller screens? Get rid of it!
In this way I have always been able to maintain the right prioritization in order to arrive at a fully working end product. In PROPOSAL.md you can read that a chat function could become optional, this idea was never worked on again. Simply because it does not belong to the website. It was very good in this respect to do things differently than was initially planned, but as mentioned earlier: many parts went perfectly according to plan and for that reason the end product looks very much like the initial DESIGN.md file.
There have been no major trade-offs, but in `FutureWork` I describe some nicer/better/smarter solutions and additions. If I had more time I would have added more associations to hand in an even better Proof-of-Concept. Other additions that would be possible with more time (and maybe even money) can be found again in `FutureWork`. Finally, I want to emphasize how proud and happy I am with my end product. We learned from CS50 that you have to see where you end up compared to YOURSELF. I had never believed that it would be possible for me to program and launch a completely self-designed website...

#### FutureWork
##### Additions

- Associations can create an account, add their details (name, story, photo) and fill in the 'kieswijzer'. This way it can become possible to add much more (correct) data in a shorter time.
- "What do the associations think", offering the option to see in the 'kieswijzer' what certain associations think of the position.
- Saving users' data in order to generate a ranking about "how often has an association been ranked highest".
- Share results directly, via Insta, Whatsapp and the like, with a certain format.
- Add "About me", "That you give people the feeling that this is not done by some old bag". - said a fellow student.
- Create Order_by query so that people can generate their own overview in `verenigingen.html`.

##### Adjustments

- Brassen, “Niet alleen 1vs1, maar ook bij een inval, waarbij een hele vereniging op bezoek komt bij een andere vereniging (volgens mij altijd op afspraak) en dan probeert de 'gast' de bar over te nemen van de 'gastheer' oftewel gewoon hooligans Ajax VS hooligans Feyenoord”. - said a fellow student.
- Opt for GeoCoding (from Address to coordinates via Google Maps instead of manually) since figuring out lat / lng coordinates takes a lot of unnecessary time when you have to add an association as admin.
- Make 'Woordenboek' navigable using letters (modal is already made).
- Slider on/off for JavaScript with beer-shower, so the beer-mouse does not always have to be present.
- Make the city unique in admin so that the combination of Groningen + Minerva is not automatically possible.


