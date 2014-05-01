
from lxml import etree
from prezi_xml_helpers import PreziXmlHelpers

import random


class XmlGenerator():

    def __init__(self, data):
        self.data = data
        self.xml_data = etree.Element('zuiprezi')
        self.zui_table = etree.SubElement(self.xml_data, 'zui-table')
        self.counter = 0

    def generate_xml(self):
        self._initiate_base_xml()
        self._parse_json_object(self.data)
        return etree.tostring(self.xml_data)

    def _initiate_base_xml(self):
        PreziXmlHelpers.generate_version_node(self.xml_data, 1)
        PreziXmlHelpers.generate_autoplay_node(self.zui_table, 4000)

        # TODO figure out a bound algorithm
        # TODO make this more descriptive
        PreziXmlHelpers.generate_bounds_node(self.zui_table,
                                             (0.0, 0.0),
                                             (100.0, 100.0))

    def _parse_json_object(self, data):
        self._parse_thread(data)

    # TODO omfg refactor
    def _parse_thread(self, data):
        if isinstance(data, dict):
            for key in data.keys():
                if key == 'entry':
                    current_id = '0_' + str(random.randint(1, 100000))
                    frame_node = etree.SubElement(self.zui_table, 'object',
                                                  id=current_id,
                                                  x=str((self.counter + 1) * 8000),
                                                  y="0",
                                                  s="10",
                                                  type='button')
                    type_node = etree.SubElement(frame_node, 'type')
                    type_node.text = 'circle'
                    size_node = etree.SubElement(frame_node, 'size')
                    w_node = etree.SubElement(size_node, 'w')
                    w_node.text = '800'
                    h_node = etree.SubElement(size_node, 'h')
                    h_node.text = '800'

                    text_node = etree.SubElement(self.zui_table, 'object',
                                                 id=current_id,
                                                 x=str((self.counter + 1) * 8000),
                                                 y="0",
                                                 s="18",
                                                 type='text')
                    w_node = etree.SubElement(text_node, 'width')
                    w_node.text = '220'
                    h_node = etree.SubElement(text_node, 'height')
                    h_node.text = '28'

                    p_node = etree.SubElement(text_node, 'p',
                                              align='center')
                    t_node = etree.SubElement(p_node, 'text')

                    t_node.text = data[key].decode('utf-8')
                    self.counter += 1
                self._parse_thread(data[key])

if __name__ == '__main__':
    xml_generator = XmlGenerator({"0": {"child": {"0": {"child": {}, "entry": "test text 10"}, "1": {"child": {}, "entry": "test"}}, "entry": "test text 00"}})
    print xml_generator.generate_xml()
