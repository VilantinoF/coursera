import json
import urllib.request, urllib.parse, urllib.error
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

# Parse JSON
result = 0
info = json.loads(data)
print('Count User: ', len(info['comments']))
for item in info['comments']:
    result += int(item['count'])
print(result)