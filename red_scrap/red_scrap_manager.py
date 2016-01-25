
import os
import click

# os.system('scrapy crawl indeed -a job=python -a state=ca')

# @click.option('--spider', prompt='your name')
# @click.option('--job', prompt=True)
# @click.option('--state', prompt=True)
@click.command()
@click.option('--spider', prompt='Your spider name please', type=str)
@click.option('--job', prompt='Your job you are looking for please',type=str)
@click.option('--state', prompt='Your state', type=str)
def crawl(spider, job, state):
    '''

    This will be the manager/dashboard of the scraping module. The main aim is to provide an option for the user
    or programmer that will task whichever spider is called with the job posting and state. For instance if
    someone wanted to call the indeed spider, from this Dashbord they would call "red_scrap_manager" then in the
    options they would indicate "indeed", job = "python"  and state = "CA".
    This dashboard will also have access to the utilities sections or util function where the user can clean up all
    the data and chart what is needed. Think of this as the front page of the app.
    :param spider: str, this is the name of the spider to be called. Always starts with an uppercase letter do "indeed"
    is actually "Indeed". Similar to all other spiders listed below:
    [Dice]-parses the Dice job board
    [Descriptor]- clicks on the links and parses all the information for the front page of the job.
    :param job:str, The job that you are looking for .
    :param state:str, The state where you will be located
    :return: Calls the spiders into action through an OS process

    '''
    click.echo("you have chosen %s %s %s" %(spider, job, state))
    os.system('scrapy crawl %s -a job=%s -a state=%s' % (spider, job, state))

crawl()

#     # os.system('scrapy crawl %s -a job=%s -a state=%s' % (spider_name, job, state))
#
# # crawl('indeed', 'python', 'ca')
# if __name__=='main':
#     crawl()