from urllib.request import urlopen
import json
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/todos/1"
with urlopen(url) as response:
    body = response.read()

todo_item = json.loads(body)
# print(todo_item)

with urlopen("http://www.example.com") as response:
    body = response.read()

# pprint(response.headers)
# pprint(response.headers.items())
# pprint(character_set)
# pprint(decoded_body[:30])

character_set = response.headers.get_content_charset()
decoded_body = body.decode(character_set)

with open("example.html", mode="wb") as html_file:
    html_file.write(body)

with urlopen("https://httpbin.org/json") as response:
    body = response.read()

print(response.headers.get_content_charset())
print(json.loads(body))
