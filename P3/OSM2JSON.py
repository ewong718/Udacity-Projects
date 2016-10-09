# This python code converts an OSM file into a JSON structured file
# The shape_element function is based off of James Kao's website https://jameskao.me/tag/openstreetmap/
# This function has been retweaked to fix a small bug that I found in his code


import xml.etree.ElementTree as ET
from datetime import datetime
import re
import json

fname = 'syracuse-corrected.osm'
outputFile = 'syracuse.json'

# Function to rearrange structure of XML OSM document into JSON format
def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way":
        node['type'] = element.tag

        # Parse attributes
        for attrib in element.attrib:

            # Data creation details
            if attrib in ["version", "changeset", "timestamp", "user", "uid"]:
                if 'created' not in node:
                    node['created'] = {}
                node['created'][attrib] = element.get(attrib)

            # Parse location
            elif attrib in ['lat', 'lon']:
                lat = float(element.attrib.get('lat'))
                lon = float(element.attrib.get('lon'))
                node['pos'] = [lat, lon]

            # Parse the rest of attributes
            else:
                node[attrib] = element.attrib.get(attrib)

        # Process tags
        for tag in element.iter('tag'):
            key = tag.attrib['k']
            value = tag.attrib['v']

            # Tags with single colon and beginning with addr
            if key.startswith('addr'):
                if 'address' not in node:
                    node['address'] = {}
                kl = key.split(':')
                if len(kl) == 2:
                    sub_attr = kl[1]
                    node['address'][sub_attr] = value
                elif key == 'address':
                    node['address']['address'] = value
                else:
                    node[key] = value

        # All other tags that don't begin with "addr"
            elif not key.startswith('addr'):
                if key not in node:
                    node[key] = value
            else:
                node["tag:" + key] = value

        # Process nodes
        for nd in element.iter('nd'):
            if 'node_refs' not in node:
                node['node_refs'] = []
            node['node_refs'].append(nd.attrib['ref'])

        return node
    else:
        return None

# Load OSM file, get all elements
ET.parse(fname)
tree = ET.parse(fname)

root = tree.getroot()
elements = root.findall('./')

# Convert XML to JSON and write to output file
with open(outputFile, 'w') as fp:
    for element in elements:
        json_element = shape_element(element)
        if json_element:
            json.dump(json_element, fp, indent=4)
