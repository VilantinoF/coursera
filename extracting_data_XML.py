import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Parse HTML
address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

#Parse XML
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('count:', len(lst))
result = 0
for item in lst:
    result += (int(item.find('count').text))
print('sum', result)