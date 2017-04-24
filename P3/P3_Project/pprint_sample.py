import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

filename = "sample.osm"

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def count_tags(filename):
    tag_dict = defaultdict(int)
    for event, elem in ET.iterparse(filename):
        tag_dict[elem.tag] += 1
    return tag_dict

def test():
    tags = count_tags(filename)
    pprint.pprint(tags)
    root = get_root(filename)
    first_node = root.find('node')
    pprint.pprint(first_node.text)

test()