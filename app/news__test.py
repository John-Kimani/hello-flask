import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Tesk Class to test the behaviour
    '''
    def setUp(self):
        '''
        Set up
        '''
        self.new_news = News(1234, 'Citizen', 'Politics in kenya')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()