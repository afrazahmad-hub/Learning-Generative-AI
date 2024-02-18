import requests

res = requests.post("http://127.0.0.1:8000/id", json={"name":"Afraz"})

print(res.json())
print(res.status_code)
print(res.text)
print(res.headers)