
from lxml import etree


# TODO akos.hochrein think a way of removing side effects
class PreziXmlHelpers(object):

    @staticmethod
    def generate_autoplay_node(xml_node, delay):
        autoplay_node = etree.SubElement(xml_node, 'autoplay')
        delay_node = etree.SubElement(autoplay_node, 'delay')
        delay_node.text = str(delay)

    @staticmethod
    def generate_bounds_node(xml_node, bounds, dimensions):
        etree.SubElement(xml_node, 'bounds',
                         x=str(bounds[0]), y=str(bounds[1]),
                         width=str(dimensions[0]), height=str(dimensions[1]))

    @staticmethod
    def generate_version_node(xml_node, version):
        version_node = etree.SubElement(xml_node, 'version')
        version_node.text = str(version)

    @staticmethod
    def generate_type_node(xml_node, type):
        type_node = etree.SubElement(xml_node, 'type')
        type_node.text = type

    @staticmethod
    def generate_size_node(xml_node, dimensions):
        size_node = etree.SubElement(xml_node, 'size')
        w_node = etree.SubElement(size_node, 'w')
        w_node.text = str(dimensions['w'])
        h_node = etree.SubElement(size_node, 'h')
        h_node.text = str(dimensions['h'])

    @staticmethod
    def generate_width_node(xml_node, dimensions):
        w_node = etree.SubElement(xml_node, 'width')
        w_node.text = str(dimensions['w'])

    @staticmethod
    def generate_height_node(xml_node, dimensions):
        h_node = etree.SubElement(xml_node, 'height')
        h_node.text = str(dimensions['h'])

    @staticmethod
    def generate_text_node(xml_node, text, alignment):
        paragraph_node = etree.SubElement(xml_node, 'p', align=alignment)
        text_node = etree.SubElement(paragraph_node, 'text')
        text_node.text = text

    @staticmethod
    def generate_object_node(xml_node):
        pass


class ObjectNode(object):

    def __init__(self, parent_node, id, node_type, dimensions):
        return etree.SubElement(parent_node, 'object',
                                id=str(id),
                                type=str(node_type),
                                x=str(dimensions['x']),
                                y=str(dimensions['y']),
                                s=str(dimensions['s']))


class FrameNode(ObjectNode):

    def __init__(self, parent_node, id, node_type, dimensions, frame_type):
        frame_node = super(FrameNode, self).__init__(parent_node, id, node_type, dimensions)
        PreziXmlHelpers.generate_type_node(frame_node, frame_type)
        PreziXmlHelpers.generate_size_node(frame_node, dimensions)


class TextNode(ObjectNode):

    def __init__(self, parent_node, id, node_type, dimensions, text, alignment):
        text_node = super(TextNode, self).__init__(parent_node, id, node_type, dimensions)
        PreziXmlHelpers.generate_width_node(text_node, dimensions)
        PreziXmlHelpers.generate_height_node(text_node, dimensions)
        PreziXmlHelpers.generate_text_node(text_node, text, alignment)


class ImageNode(ObjectNode):
    pass


class Thread(object):

    def __init__(self):
        pass
