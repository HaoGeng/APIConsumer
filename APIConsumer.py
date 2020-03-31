import sys
import requests
import json

def send_get_request(URL):
    r = requests.get(URL)
    return r.json()

def send_post_request(URL, data):
    r = requests.post(URL, data)
    return r.json()

def send_put_request(URL, data):
    r = requests.put(URL, data)
    return r.json()

def find_posts_by_id(posts, id_key, id):
    return [post for post in posts if(post[id_key] == id)]

def print_operation_output(index, line_message, posts_list={}):
    print('{0}. {1}'.format(index, line_message))
    count = 1
    for post in posts_list:
        print('     Title {0} {1}'.format(count, post['title']))
        count += 1

API_ENDPOINTS = {
    'posts': 'https://jsonplaceholder.typicode.com/posts',
    'user': 'https://jsonplaceholder.typicode.com/users/5',
    'post': 'https://jsonplaceholder.typicode.com/posts/14'
}

# operation 1
posts = send_get_request(API_ENDPOINTS['posts'])
print_operation_output(1, 'Post titles:', posts)

# operation 2
user = send_get_request(API_ENDPOINTS['user'])
email = user['email']
print_operation_output(2, 'Email: {0}'.format(email))

# operation 3
new_post = {
    'userId': '5',
    'id': '555',
    'title': 'I passed the test!',
    'body': 'I passed the test!'
}
post_id = send_post_request(API_ENDPOINTS['posts'], new_post)
print_operation_output(3, 'New post id:{0}'.format(post_id['id']))

# oepration 4
posts_uid_5 = find_posts_by_id(posts, 'userId', 5)
print_operation_output(4, 'Post titles by user 5:', posts_uid_5)

# operation 5
post_pid_14 = find_posts_by_id(posts, 'id', 14)[0]
post_pid_14['title'] = 'I passed the test!'
response = send_put_request(API_ENDPOINTS['post'], post_pid_14)
print_operation_output(5, 'Response:')
print(json.dumps(response, indent=4))
