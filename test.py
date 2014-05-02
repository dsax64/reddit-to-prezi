
from ParseReddit import ParseReddit
from xml_generator.xml_generator import XmlGenerator

pr = ParseReddit.ParseReddit('http://www.reddit.com/r/Python/comments/24id80/any_quirky_python_projects_to_hack_on/')
reddit_dict = pr.get_reddit_dict()

xml_generator = XmlGenerator(reddit_dict)
print xml_generator.generate_xml()
