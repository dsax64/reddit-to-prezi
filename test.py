
from ParseReddit import ParseReddit
from xml_generator.xml_generator import XmlGenerator

pr = ParseReddit.ParseReddit('http://www.reddit.com/r/dadjokes/comments/24gmom/dad_joke_about_yoga/')
reddit_dict = pr.get_reddit_dict()

xml_generator = XmlGenerator(reddit_dict)
print xml_generator.generate_xml()
