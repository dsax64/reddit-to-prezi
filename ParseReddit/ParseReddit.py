import urllib2
from bs4 import BeautifulSoup


class ParseReddit(object):

    def __init__(self, reddit_url):
        self.reddit_url = reddit_url

    def get_reddit_dict(self):
        return self._parse_url()

    def _parse_url(self):
        soup_parsed_data = self._get_html_soup_data()
        commentarea = self._get_comment_thread(soup_parsed_data)
        return self._get_comments(commentarea)

    def _get_html_soup_data(self):
        response = urllib2.urlopen(self.reddit_url)
        html = response.read()
        soup_parsed_data = BeautifulSoup(html)
        return soup_parsed_data

    def _get_comment_thread(self, thread, thread_type='commentarea'):
        return thread.find("div", class_=thread_type)

    def _get_comments(self, thread):
        if thread.contents:
            return self._parse_thread(thread)
        else:
            return None

    def _parse_thread(self, thread):
        dict = {}
        i = 0
        comments = self._get_comments_table(thread)
        for comment in comments:
            entry, child = self._parse_single_comment(comment)
            dict[i] = {'entry': entry, 'child': self._get_comments(child)}
            i += 1
        return dict

    def _get_comments_table(self, thread):
        site_table = thread.find("div", class_="sitetable")
        comments_table = site_table.find_all("div", class_="comment", recursive=False)
        return comments_table

    def _parse_single_comment(self, thread_entry):
            entry = thread_entry.find("div", class_="entry").find(
                "div", class_="md").get_text('\n').rstrip().encode('utf-8')
            child = self._get_comment_thread(thread_entry, 'child')
            return entry, child
