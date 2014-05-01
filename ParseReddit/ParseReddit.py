import urllib2
from bs4 import BeautifulSoup
import simplejson


class ParseReddit(object):

    def __init__(self, reddit_url):
        self.reddit_url = reddit_url

    def get_json(self):
        dict = self.parse_url()
        return simplejson.dumps(dict, sort_keys=True, indent=4 * ' ')

    def parse_url(self):
        soup_parsed_data = self.get_html_soup_data()
        commentarea = self.get_comment_thread(soup_parsed_data)
        return self.get_entries(commentarea)

    def get_html_soup_data(self):
        response = urllib2.urlopen(self.reddit_url)
        html = response.read()
        soup_parsed_data = BeautifulSoup(html)
        return soup_parsed_data

    def get_comment_thread(self, thread, thread_type='commentarea'):
        return thread.find("div", class_=thread_type)

    def get_entries(self, thread):
        if thread.contents:
            dict = {}
            i = 0
            commentstable = thread.find("div", class_="sitetable")
            for comments in commentstable.find_all("div", class_="comment", recursive=False):
                entry = comments.find("div", class_="entry").find(
                    "div", class_="md").get_text('\n').rstrip().encode('utf-8')
                child = self.get_comment_thread(comments, 'child')
                dict[i] = {'entry': entry, 'child': self.get_entries(child)}
                i += 1
            return dict
        else:
            return None

if __name__ == '__main__':
    reddit_parser = ParseReddit('http://www.reddit.com/r/gaming/comments/24f97g/tranquility/')
    print reddit_parser.get_json()
