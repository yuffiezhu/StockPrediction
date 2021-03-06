import sys
import csv


class ReadNews:

    def __init__(self):
        # RedditNews.csv contains news from 2008-06-08 to 2016-07-01
        self.news = []
        with open('RedditNews.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.news.append(row)

    # Read Files and get all the news published on the given date
    def get_news(self, date):
        news_on_date = []
        for entry in self.news:
            if date in entry["Date"]:
                news_on_date.append(entry["News"])
        return news_on_date
