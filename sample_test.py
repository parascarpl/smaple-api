# importing the requests library
import requests
import logging


logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
# api-endpoint
URL = "https://reqres.in/api/users?page=2"

r = requests.get(url = URL, verify=False)

# extracting data in json format
data = r.json()

logging.info(data)

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=False)
