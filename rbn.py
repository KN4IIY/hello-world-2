#! /usr/bin/python3

from requests_html import HTML, HTMLSession

# with open('Reverse-Beacon-Network.html') as html_file:
#     source = html_file.read()
#     html = HTML(html=source)

session = HTMLSession()
r = session.get('http://reversebeacon.net/nodes/')
r.html.render()
# tbody = r.html.find('tbody', first=True)
print()
# tr = tbody.find('tr', first=True)

# td = tr.find('td')
# callsign = td
# print(f'Callsign = {td[0].text}, Gridsquare = {td[2].text}, Status = {td[8].text}')
