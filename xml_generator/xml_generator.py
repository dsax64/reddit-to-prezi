
from lxml import etree
from prezi_xml_helpers import PreziXmlHelpers, FrameNode, TextNode

import random


class XmlGenerator():

    def __init__(self, data):
        self.thread = data
        self.xml_thread = etree.Element('zuiprezi')
        self.zui_table = etree.SubElement(self.xml_thread, 'zui-table')
        self.counter = 0

    def generate_xml(self):
        self._initiate_base_xml()
        self._parse_json_object(self.thread)
        return etree.tostring(self.xml_thread)

    def _initiate_base_xml(self):
        PreziXmlHelpers.generate_version_node(self.xml_thread, 1)
        PreziXmlHelpers.generate_autoplay_node(self.zui_table, 4000)

        # TODO figure out a bound algorithm
        # TODO akos.hochrein create a Dimensions class
        PreziXmlHelpers.generate_bounds_node(self.zui_table,
                                             (0.0, 0.0),
                                             (100.0, 100.0))

    def _parse_json_object(self, thread):
        self._parse_thread(thread)

    # TODO omfg refactor
    def _parse_thread(self, thread):
        if isinstance(thread, dict):
            for key in thread.keys():
                if key == 'entry':
                    current_id = '0_' + str(random.randint(1, 100000))
                    dimensions = {'x': self.counter * 8000,
                                  'y': 0,
                                  's': 10 / float(self.counter + 1),
                                  'w': 800,
                                  'h': 800}
                    FrameNode(self.zui_table,
                              current_id,
                              'button',
                              dimensions,
                              'circle')
                    TextNode(self.zui_table,
                             current_id,
                             'text',
                             dimensions,
                             thread[key].decode('utf-8'),
                             'center')
                    self.counter += 1
                self._parse_thread(thread[key])

if __name__ == '__main__':
    xml_generator = XmlGenerator({"0": {"child": {"0": {"child": {}, "entry": "test text 10"}, "1": {"child": {}, "entry": "test"}}, "entry": "test text 00"}})
    print xml_generator.generate_xml()
