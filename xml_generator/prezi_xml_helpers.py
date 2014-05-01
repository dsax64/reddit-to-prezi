
from lxml import etree


class PreziXmlHelpers(object):

    @staticmethod
    def generate_autoplay_node(xml_node, delay):
        autoplay_node = etree.SubElement(xml_node, 'autoplay')
        delay_node = etree.SubElement(autoplay_node, 'delay')
        delay_node.text = delay

    @staticmethod
    def generate_bounds_node(xml_node, bounds, dimensions):
        etree.SubElement(xml_node, 'bounds',
                         x=str(bounds[0]), y=str(bounds[1]),
                         width=str(dimensions[0]), height=str(dimensions[1]))

    @staticmethod
    def generate_version_node(xml_node, version):
        version_node = etree.SubElement(xml_node, 'version')
        version_node.text = str(version)
