import re
import json
import html
from xml.dom import minidom

def getNodeText(node):
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

xmldoc = minidom.parse('industries.xml')
itemlist = xmldoc.getElementsByTagName('Item')
data = {}

for item in itemlist:
 itemId = item.getAttribute('id')
 if re.match(r'[A-Z]', itemId):
    data[itemId] = {}
    for label in item.getElementsByTagName('LabelText'):
     #   if label.getAttribute('language') == 'DE':
     #       print(getNodeText(label) )
        data[itemId][label.getAttribute('language')] = getNodeText(label)

with open('dist/industries.json', 'w') as json_file:
    json_file.write(json.dumps(data))
