import requests

res = requests.post("http://127.0.0.1:8000/agent")

print(res.text)
print(res.status_code)
print(res.headers)
print(res.json())
