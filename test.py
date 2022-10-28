import sys

if sys.version_info < (3, 0):
    from urllib2 import urlopen
else:
    from urllib.request import Request, urlopen

import io
from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import urllib
import os

request_site = Request(url="http://via.placeholder.com/150/92c952", 
	headers={
		"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"sec-fetch-user": "?1",
		"sec-fetch-dest": "document",
		"sec-fetch-site": "none",
		"sec-fetch-mode": "navigate",
		"upgrade-insecure-requests": "1",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en,en-US;q=0.9,ru;q=0.8",
		"cache-control": "max-age=0",
		"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "Android",
		"method": "GET"
		})
fd = urlopen(request_site)
print (fd.read())
f = io.BytesIO(fd.read())

ct = ColorThief(f)
#print(ct.get_color(quality=1))
dominant_color = ct.get_color(quality=1)

#plt.imshow([[dominant_color]])
#plt.show()

palette = ct.get_palette(color_count=5)
#plt.imshow([[palette[i] for i in range(5)]])
#plt.show()

for color in palette:
	#print(color)
	print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")


