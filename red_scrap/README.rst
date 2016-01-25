Red_Scrap_Spider Documentation
==============================
S.1: Introduction and Background.
---------------------------------

Red scrap spider is a python based command line application with that performs Data scraping and cleaning as well as text handling and visualizing.
The Idea came from the fact that there are so many job boards out there that it becomes cumbersome for a person to actually search through
and come with a smaller subset of jobs out of a huge array of jobs. This application is aimed at making your search easier by scraping all
job applications online and bringing them to  your command line interface for you to view. It also saves the job = [ Title, company, Location,
link] as a JSON format for developers who might want to make a a site through Angular services.

S.1.1: Support
--------------
This application fully supports python 2.7 with full support of python 3.0 coming in the next two weeks.

S.1.2: Installation.
-------------------
all versions (mac, windows)

1. Create a new directory::

            mkdir <directory>
            
**mac OS: This process may seem familiar**

2.  create a virtual env::

            virtualenv venv
      
**Windows:** windows is a little bit trickier than Unix/Mac. I will however guide you in the process step by step.Please note that this guide assumes that you have a current installation of anaconda present. This is important since the utilities of this application will need numpy to run and that tends to be a crinkle in the you-know-what.

2. download pywin.exe and save in on your desktop or C:\
3. create a conda environment with the packages in the requirements file. This may take a while since scrapy has a few dependancies that will also be installed.
4. activate your env.
5. point your conda/pip to your pywin installation and through 'pip install 'c:\pywin.exe' -[path to the installation].


Note: I plan to upload this package to pypi so in the coming future it will just be downloaded via 'pip'

S.1.3: What the application supports.
-------------------------------------
So far the Application supports the following job boards

1) Dice.
2) Indeed.

please submit the job board requests that you would like me to involve and i will add it to the to do list which will be updated every midnight.

S.2.0: Running the spider:
--------------------------
the following steps will show you how to run the job collection spiders and the Description spiders.

S.2.1: How to run the job search spider:
----------------------------------------
This project has a  front end python manager that runs all your back end scripts for your. All you need to do is specify what you where you want them to go and they will be run.  For instance assume we want check for all the python jobs in the dice network in california and we have a limit of 60 jobs::

    #call the Scraping manager and tell him how many jobs you need.
    
    red_scraper_manager --limit=60

you should get a response feedback that says::
    
    #response feedback from the call
    
    your spider name please: Dice # Note the uppercase first letter. It is a spider that asks to be respected else it wont run..          really it wont (try it if you dont believe me.)
    # 2nd response feedback
    
    The Job you are looking for please: Python # sweet
    
    #3rd response feedback
    
    Your State: CA # it doesnt nessecarily need to be your state but a state where you want to work
    #final response before the run will be
    "you have chosen %s %s %s %s" %(spider, job state, limit).

press the 'return' key and watch scrapy do its magic.
Things to note so far:
* red_scrap_manager is a python exec with click functionality so if you are stuck and you would like 
some help ::
    red_scrap_manager --help
    
The documentation of the process should appear on your command line.

S.2.2: Spider supported by name and limit:
------------------------------------------

Caution: word of advice the spider tends to get indulged in the scraping process and sometimes it will overshoot
I am currently working on a solution to that and have it as precise as possible.

S.2.2.1 Dice 
-------------
(job=str, state=str)::
    --limit(Default) = None

Ensure that if you choose dice you enter the limit else the spider will run but nothing will be displayed or stored
as a JSON.

S.2.2.2: Descriptor 
--------------------
(job=str, state=str)::
    --limit(Default) = None

Ensure that if you choose Descriptor you enter the limit else the spider will run but nothing will be displayed or stored
as a HTML file.

S.2.2.3: Indeed 
---------------
(job=str, state=str)::
    --limit is discouraged
Do not add a limit to the indeed spider. Either way it will run all the jobs that are on that specific request and hence limit 
is discouraged. Plus it saves up some typing stamina points.

S.3.0: Processing and storing the files.
----------------------------------------
This section will primarily focus on how files will be stored and also how to process Description files inorder to get the keywords
by frequency.

S.3.1: How files will be stored:
--------------------------------

For all files dealing with job searching ran through the manager will be stored in the root directory as a .JSON format file. The Main reason for this decision was to give all of the job board developers a chance to maybe use those files in any job sites available. The future goal will also be to port those files into a web search engine through PySolr and it seemed like the easier idea at the time.

However if you need an csv format, you could run each individual spider and store the file as an output -csv.  Please refer to the scrapy documentation for more formats on how to store the data

The Future of this project will have the files  stored in a solr environment for indexing.

S.3.2: Processing.
------------------
This section will cover the processing that goes on through the utilities module(utils.py). It will deal with one spider, Descriptor.

S.3.2.1: After running the spider.
----------------------------------

Once you run the 'Descriptor' Spider a couple of things will happen:
* The spider will go to each individual post open it up and scrape all the html files. To speed up the process, it was decided that the files would be stored and processed locally. Not to fear though since after the processing, the OS.remove will remove all the files leaving your computer with no excess html files.
* Once the spider downloads all the files they will be stored in the root directory

S.3.2.2: Analysis
-----------------

Once the files are available the real analysis can begin:

I Clean_up(.html)
-----------------
Lets clean up all the html tags and store all the text in one file. Open your ipython notebook in the root directory::

    >>>import utils
    >>>from utils import UtilCleanUp as up

run up just as a test::

    >>>up
    <class 'utils.UtilCleanUp'> #output
    
instantiate the class::
    >>> clean = UtilCleanUp()

run through the cleanser::
    >>> clean.cleanse_html()

check your root directory and note that all the .html files have disappeared. However a new file has appeared
called 'new1.txt' if you open this file all the html tags will be gone and you will be left with just the text
files.

II Frequency Analysis
----------------------
For this section we will deal with the new file that we have just created('new1.txt')

lets do a couple of imports::
    >>> from utils import CountFreq
    >>> CountFreq
    <class 'utils.CountFreq'>
    >>> Freque = CountFreq()
    # at this point i would like to say that there is all the avilable documentation present and you can access the 
    help line i.e.
    >>> help(Freque)
    #I will go through the simple procedures without any output displayed
    >>> Freque.clean_text()
    >>> Freque.word_freq()
    >>> Freque.graph_freq(cumulative = False)

the end result will be a matplotlib graph that shows the frequency of each word.
if you did::
    >>> Freque.graph_freq(cumulative = True)
    
you would get a graph of diminishing returns or half a parabola

S.Null: TODO:
------------

* Add income vs cost of living analysis for each choice
* Add to Solr
* Create a miniature search engine.
* Increase more tools in the Util section(bigrams, n-grams)

If you want to contribute or have a suggestion that you would like for me to implement, please feel free to message me on here or my email: righteousprophet33@gmail.com

S.Vote: Of Thanks.
------------------
* stack overflow!!!



Cheers and enjoy


    



