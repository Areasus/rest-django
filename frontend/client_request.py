import requests

endpoint ="https://httpbin.org/"
endpoint= "https://httpbin.org/anything"


point= requests.get(endpoint)
print("status:",point.status_code)
print(point.text)
print(point.json())