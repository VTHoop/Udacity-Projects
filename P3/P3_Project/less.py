import xml.dom.minidom
import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

xml_fname = 'sample.osm'

def count_tags(filename):
    tag_dict = defaultdict(int)
    for event, elem in ET.iterparse(filename):
        tag_dict[elem.tag] += 1
    return tag_dict

tags = count_tags(xml_fname)
pprint.pprint(tags)


xml = xml.dom.minidom.parse(xml_fname) # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
print pretty_xml_as_string