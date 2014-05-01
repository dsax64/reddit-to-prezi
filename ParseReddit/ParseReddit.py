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
        return self.get_comments(commentarea)

    def get_html_soup_data(self):
        response = urllib2.urlopen(self.reddit_url)
        html = response.read()
        soup_parsed_data = BeautifulSoup(html)
        return soup_parsed_data

    def get_comment_thread(self, thread, thread_type='commentarea'):
        return thread.find("div", class_=thread_type)

    def get_comments(self, thread):
        if thread.contents:
            return self.parse_thread(thread)
        else:
            return None

    def parse_thread(self, thread):
        dict = {}
        i = 0
        comments = self.get_comments_table(thread)
        for comment in comments:
            entry, child = self.parse_single_comment(comment)
            dict[i] = {'entry': entry, 'child': self.get_comments(child)}
            i += 1
        return dict

    def get_comments_table(self, thread):
        site_table = thread.find("div", class_="sitetable")
        comments_table = site_table.find_all("div", class_="comment", recursive=False)
        return comments_table

    def parse_single_comment(self, thread_entry):
            entry = thread_entry.find("div", class_="entry").find(
                "div", class_="md").get_text('\n').rstrip().encode('utf-8')
            child = self.get_comment_thread(thread_entry, 'child')
            return entry, child

if __name__ == '__main__':
    reddit_parser = ParseReddit('http://www.reddit.com/r/programming/comments/24frw0/et_the_extraterrestrial1982_atari_2600_source_code/')
    print reddit_parser.get_json()
