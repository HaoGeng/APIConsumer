import sys
import requests

URL = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(URL)

posts = r.json()

print("1. Post titles:")
payload = {}

count = 1
for post in posts:
    print('Title {0} {1}'.format(count, post['title']))
    if post['id'] == 14:
        payload = post
    count += 1

URL = "https://jsonplaceholder.typicode.com/users/5"
r = requests.get(URL)

user = r.json()

email = user['email']

print("2. Email: {0}".format(email))

URL = "https://jsonplaceholder.typicode.com/posts"
newPayload = {
    'userId': '5',
    'id': '555',
    'title': 'I passed the test!',
    'body': 'I passed the test!'
}
r = requests.post(URL)

pid = r.json()

print("3. New post id: {0}".format(pid))

print("4. Post titles by user 5:")

count = 1
for post in posts:
    if post["userId"] == 5:
        print('Title {0} {1}'.format(count, post['title']))
        count += 1

URL = "https://jsonplaceholder.typicode.com/posts/14"
payload["title"] = "I passed the test!"
r = requests.put(URL, payload)

response = r.json()
print("5. Response:")
print(response)

