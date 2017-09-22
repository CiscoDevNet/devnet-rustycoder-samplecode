# import functions from the request library
import requests, json

#r = requests.get('url',auth=('user','pass'))

r = requests.get('http://0.0.0.0:8080/api/devices')

print("print r\n", r)
print("\nprint r.status_code\n", r.status_code)
print("\nprint r.headers\n", r.headers)
print("\nprint r.headers['content-type']\n", r.headers['content-type'])
print("\nprint r.text\n", r.text)
