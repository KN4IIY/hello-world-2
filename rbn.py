#! /usr/bin/python3

from requests_html import HTML

with open('Reverse-Beacon-Network.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

tbody = html.find('tbody', first=True)
tr = tbody.find('tr', first=True)
td = tr.find('td')
# callsign = td
print(f'Callsign={td[0].text} Gridsquare={td[2].text} Status={td[8].text}')
