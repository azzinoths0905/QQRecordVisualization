from unittest import TestCase
from wordCloud import WordCloud


class TestWordCloud(TestCase):
    def test__get_data(self):
        wc = WordCloud()
        print(wc.process())
