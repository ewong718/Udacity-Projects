# This code audits the phonenumbers and will try to correct them to the ### ### #### format
# In addition, this code also audits and corrects websites that do not end with a slash at the end of its domain name
# The phonenumbers library is required


import xml.etree.ElementTree as ET
import phonenumbers

fname = 'syracuse.osm'
outputfile =  'syracuse-corrected.osm'

tree = ET.parse(fname)

nodetags = tree.findall('node/tag')
waytags = tree.findall('way/tag')
relationtags = tree.findall('relation/tag')

for idx, tag in enumerate(nodetags):
    if tag.attrib['k'] == 'phone':
        # Get value of phone number
        pn = tag.attrib['v']
        # Check whether phone number matches XXX XXX XXXX format
        if not pn[0:3].isdigit() or pn[3] != ' ' or not pn[4:7].isdigit() or pn[7] != ' ' or not pn[8:12].isdigit() or len(pn) > 12:
            try:
                phone_obj = phonenumbers.parse(pn, 'US')
                # Replace phone number with correct format
                nodetags[idx].attrib['v'] = phonenumbers.format_number(phone_obj, phonenumbers.PhoneNumberFormat.mro).replace('-', ' ')
                #print "Fixed:", pn, nodetags[idx].attrib['v']
            except:
                pass
                #print pn, "Error, possibly not a valid phone number"

for idx, tag in enumerate(waytags):
    # Only top-level domains
    if tag.attrib['v'].endswith(('.com', '.org', '.edu', '.gov', '.mil', '.net', '.int')):
        if tag.attrib['k'] == 'website' and not tag.attrib['v'].endswith('/'):
            waytags[idx].attrib['v'] = tag.attrib['v'] + '/'

tree.write(outputfile)