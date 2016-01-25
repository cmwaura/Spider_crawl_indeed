import os
import codecs
import glob
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk import pos_tag as pt
from bs4 import BeautifulSoup

loose_words = [
    'dice', 'job', 'password', 'dice.com', 'email', 'message', 'use', 'sign', 'please', 'san', 'address',
    'jose', 'robert', 'half'
]
class UtilCleanUp(object):

    def __init__(self):
        '''
         instantiating the files and then paths that we will use in this process
        '''

        self.file2 = codecs.open('new1.txt', mode='w', encoding='utf-8')
        self.PATH = os.path.abspath(os.path.dirname('__file__'))
        self.SYMBOL = "\\"

    def cleanse_html(self):
        '''
        in this process we will cleanse all the collected html files and gather all the text into one
        text file that will be readily available for use for the next class. Please note one major thing
        is that once the html files are sanitized, they will be removed from  the red_scrap folder so before you
        activate the utility process, if you wanted to take a look at the folder this would be the last time to do
        that
        :return: a new text file format
        '''
        for f in glob.glob('*.html'):
            html_file = '{h}{s}{y}'.format(h=self.PATH, s=self.SYMBOL, y=f)
            self.html = open(html_file).read()
            print html_file
            # return html
            soup = BeautifulSoup(self.html, "lxml")

            for script in soup(["script", "style"]):
                    script.extract()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            self.file2.write(text)
            os.remove(html_file)



class CountFreq(object):
    def __init__(self,  *args, **kwargs):
        self.txt_file = codecs.open('new1.txt', encoding='utf-8')
        self.stop_words = stopwords.words('english')
        self.clean_words = []
        self.loose_words = loose_words

    def clean_text(self):
        '''
        this method will clean all the data in new1.txt as well as transfer the data from a text file to
        a tokenized format that will be readily available for nltk to work with.
        :return: sanitized and tokenized words.
        '''
        stop = self.stop_words
        text = self.txt_file
        for lines in text:
            clean_words = [word for word in lines.lower().split() if word not in stop]
            self.clean_words.append(clean_words)
        self.clean_words = [val for sublist in self.clean_words for val in sublist]
        return self.clean_words

    def word_freq(self):
        '''
        single word frequency without any context. This will result in the top 100 words that will be shown and
        identified as the most repeated words. However, rigorous filtration will be applied to the printed words
        getting rid of words that are not Nouns
        :return: the frequency distribution, obj.
        '''
        classified_text = pt(self.clean_words)
        noun_descriptor = [word for word, pos in classified_text if pos == 'NN']
        revised_noun_descriptor = [word for word in noun_descriptor if word not in self.loose_words]
        self.fdist = FreqDist(revised_noun_descriptor)
        return self.fdist

    def graph_freq(self, cumulative):
        '''

        :param cumulative: Boolean value, when true it graphs the cumulative text score producing a diminishing
        return graph
        :return: a matplotlib graph
        '''

        return self.fdist.plot(100, cumulative=cumulative)




if __name__ == '__main__':
    util = UtilCleanUp()
    util.cleanse_html()
    freq = CountFreq()
    freq.clean_text()
    print freq.word_freq()
    freq.graph_freq(False)
