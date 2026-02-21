import requests


"""
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

if response.ok:
    data = response.json()
    print("Post title:", data["title"])
else:
    print("Error:", response.text)

"""


"""
url = "https://reqres.in/api/users"
params = {"page": 1} # instead of manually inputting into url

response = requests.get(url, params = params)
print("Final URL:", response.url) #shows ?page=2

response.raise_for_status() #raise error for 4xx/5xx
data = response.json()
print("Page:", data["page"])
for user in data["data"]:
    print(user["email"])
"""


"""
url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title" : "Hello from Python",
    "body" : "This is a test",
    "userId" : 1,
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
data = response.json()
print(data)

"""


"""
try:
    response = requests.get("https://httpbin.org/delay/3", timeout=1)
    reponse.raise_for_status()
    print("Success:", response.json())
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
"""


TOKEN = "jifo2j3our2930r9uf9hwoim390309fj9eopj0983hyfoidnolih2o93fhjoejwof"
BASE_URL = "https://api.x.com/2/users/by/username/Blabla"

headers = {
    "Authorization": f"Bearer {TOKEN}",
}

response = requests.get(BASE_URL, headers=headers)

print("Status code:", response.status_code)
print("URL:", response.url)

try:
    data = response.json()
    print(data)
except ValueError:
    print("Response is not JSON")
    print(response.text)
