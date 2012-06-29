##We The People API##
This is a sample API for the We The People petition application run on WhiteHouse.gov.

##The API##
WeThePeopleAPI is a Django Application with an implementation of the Django REST Framework (the "api" app). 

###GET and POST###
Interact with the API by browsing to (or making requests with):
	http://your-domain.com/petitions/
	http://your-domain.com/petitions/{petition-id}/
	http://your-domain.com/petitions/{petition-id}/signatures/
	http://your-domain.com/petitions/{petition-id}/signatures/{signature-id}

The Django REST Framework has an extremely friendly interface to interact with this data, providing a graphical means to submit both GET and POST requests. Further, data can be pulled and pushed in various formats easily specified in the URL by appending a value such as ?format=json

###

###Install###

The proper Django environment can be easily configured by using the PIP python package manager and the requirements.txt file, read more here: http://en.wikipedia.org/wiki/Pip\_(python).

####Requirements.txt####
	Django==1.4
	URLObject==2.0.2
	argparse==1.2.1
	distribute==0.6.24
	djangorestframework==0.3.3
	wsgiref==0.1.2
	yolk==0.4.3

##Read More##
1.	http://cfasummercodeparty.wikispaces.com/Whitehouse+Petitions+API
2.	https://etherpad.mozilla.org/7flI23NLtC
3.	Based on this: http://www.dizzey.com/development/building-restful-api-with-django/
4.	And that: http://django-rest-framework.org/examples/blogpost.html
5.	Part of: http://oahack.wikispaces.org/
