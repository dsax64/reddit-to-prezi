
import json
from lxml import etree


class JsonParser():
    def __init__(self, json_data):
        self.json_data = json_data
        self.xml_data = etree.Element('root')

    def generate_xml(self):
        self._parse_json_object(self.json_data)
        return etree.tostring(self.xml_data)

    def _parse_json_object(self, json_data):
        _json_data = json.loads(self.json_data)
        self._parse_thread(_json_data, self.xml_data)

    def _parse_thread(self, json_data, parent_node):
        if isinstance(json_data, dict):
            for key in json_data.keys():
                sub_node = etree.SubElement(parent_node, "test_" + str(key))
                if not isinstance(json_data[key], dict):
                    sub_node.text = unicode(json_data[key])
                self._parse_thread(json_data[key], sub_node)

if __name__ == '__main__':
    json_parser = JsonParser('{"0":{"child":{"0":"testy","1":"test"}}}')
    print json_parser.generate_xml()
