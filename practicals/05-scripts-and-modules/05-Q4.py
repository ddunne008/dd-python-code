import requests
import sys


url = sys.argv[1]
response = requests.get(url)
if response.status_code == 200:
    print("The web address: ", url, "is a valid URL")
else:
    print("The web address: ", url, "is not a valid URL")





