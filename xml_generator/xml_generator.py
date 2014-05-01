
from lxml import etree
from prezi_xml_helpers import PreziXmlHelpers


class XmlGenerator():

    def __init__(self, data):
        self.data = data
        self.xml_data = etree.Element('zuiprezi')
        self.zui_table = etree.SubElement(self.xml_data, 'zui-table')

    def generate_xml(self):
        self._initiate_base_xml()
        self._parse_json_object(self.data)
        return etree.tostring(self.xml_data)

    def _initiate_base_xml(self):
        PreziXmlHelpers.generate_version_node(self.xml_data, 1)
        PreziXmlHelpers.generate_autoplay_node(self.zui_table, '4000')

        # TODO figure out a bound algorithm
        # TODO make this more descriptive
        PreziXmlHelpers.generate_bounds_node(self.zui_table, (0.0, 0.0), (100.0, 100.0))

    def _parse_json_object(self, data):
        self._parse_thread(data, self.zui_table)

    def _parse_thread(self, data, parent_node):
        if isinstance(data, dict):
            for key in data.keys():
                sub_node = etree.SubElement(parent_node, 'test_' + str(key))
                if not isinstance(data[key], dict):
                    sub_node.text = unicode(data[key])
                self._parse_thread(data[key], sub_node)

if __name__ == '__main__':
    xml_generator = XmlGenerator({"0": {"child": {"0": "testy", "1": "test"}}})
    print xml_generator.generate_xml()
