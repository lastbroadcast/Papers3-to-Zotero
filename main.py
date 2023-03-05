# Cleans up xml exported by Papers3, ready for import into Zotero

import re

#paths of input (Papers3 exported) and output xml files:
input_file = './PapersLibraryXML.xml'
output_file = './PapersLibraryXML_Cleaned.xml'

# add undesired text and replacements here, in format of 'find': 'replacement'
# (use '' for deletion)
replacements = {
    'file://localhost/Volumes/Shared%20Folders/AllFiles': '', #deletes this string from all paths
    '%20': ' ' #replaces '%20' with a space
}

#add undesired xml tags here:
kill_tags = [
    'accession-num',
    'auth-address',
    'related-urls',
    'publisher',
    'periodical',
    'custom3'
]

with open(input_file, 'r') as open_file:
    xml = open_file.read()

#replace undesired text
print('Now replacing text.')
for i, j in replacements.items():
        xml = xml.replace(i, j)

#remove undesired xml tags
for tag in kill_tags:
    print('Now killing tag: ' + tag)

    pattern = '<' + tag + '>.+?</' + tag + '>'

    while True:
        z = re.search(pattern, xml)
        if z:
            span = z.span()
            xml_start = xml[:span[0]]
            xml_end = xml[span[1]:]
            xml = xml_start + xml_end
        else:
            break

with open(output_file, 'w') as open_file:
    open_file.write(xml)

print('Done!')



