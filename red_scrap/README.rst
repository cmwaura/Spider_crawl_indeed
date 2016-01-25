Red_Scrap_Spider Documentation
==============================
Introduction and Background.
----------------------------

Red scrap spider is a python based command line application with that performs Data scraping and cleaning as well as text handling and visualizing.
The Idea came from the fact that there are so many job boards out there that it becomes cumbersome for a person to actually search through
and come with a smaller subset of jobs out of a huge array of jobs. This application is aimed at making your search easier by scraping all
job applications online and bringing them to  your command line interface for you to view. It also saves the job = [ Title, company, Location,
link] as a JSON format for developers who might want to make a a site through Angular services.

Support
-------
This application fully supports python 2.7 with full support of python 3.0 coming in the next two weeks.

Installation.
-------------
* **Windows:**windows is a little bit trickier than Unix/Mac. I will however guide you in the process step by step.Please note that this guide assumes that you have a current installation of anaconda present. This is important since the utilities of this application will need numpy to run and that tends to be a crinkle in the you-know-what.

1) download pywin.exe and save in on your desktop or C:\
2) create a conda environment with the packages in the requirements file. This may take a while since scrapy has a few dependancies that will also be installed
3) point your conda/pip to your pywin installation and through 'pip install 'c:\pywin.exe' -[path to the installation].

Note: I plan to upload this package to pypi so in the coming future it will just be downloaded via 'pip'

What the application supports.
------------------------------
So far the Application supports the following job boards

1) Dice.
2) Indeed.

please submit the job board requests that you would like me to involve and i will add it to the to do list which will be updated every midnight.

How to run it.
--------------
This project has a  front end python manager that runs all your back end scripts for your. All you need to do is specify what you where you want them to go and they will be run. 



