import requests
import sys

sys.argv = url
requests.get(url)
if requests.get(url).status_code == 200:
    print("The web address: ", url, "is a valid URL")
else:
    print("The web address: ", url, "is not a valid URL")





