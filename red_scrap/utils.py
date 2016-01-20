import os
import codecs
import glob
from nltk import FreqDist
from nltk.corpus import stopwords
import nltk
from nltk import pos_tag as pt
from bs4 import BeautifulSoup

loose_words = [
    'dice', 'job', 'password', 'dice.com', 'email', 'message', 'use', 'sign', 'please', 'san', 'address',
    'jose', 'robert', 'half'
]
class UtilCleanUp(object):

    def __init__(self):
        self.file2 = codecs.open('new1.txt', mode='w', encoding='utf-8')
        self.PATH = os.path.abspath(os.path.dirname('__file__'))
        self.SYMBOL = "\\"

    def cleanse_html(self):
        for f in glob.glob('*.html'):
            html_file = '{h}{s}{y}'.format(h=self.PATH, s=self.SYMBOL, y=f)
            self.html = open(html_file).read()

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

#
# class CountFreq(UtilCleanUp):
class CountFreq(object):
    def __init__(self, *args, **kwargs):
        self.txtfile = codecs.open('new1.txt', encoding='utf-8')
        self.stop_words = stopwords.words('english')
        self.clean_words = []
        self.loose_words = loose_words

    def clean_text(self):
        stop = self.stop_words
        text = self.txtfile
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
        self.fdist.plot(75, cumulative=False)
        return self.fdist


if __name__ == '__main__':
    # util = UtilCleanUp()
    # util.cleanse_html()
    freq = CountFreq()
    freq.clean_text()
    print freq.word_freq()
