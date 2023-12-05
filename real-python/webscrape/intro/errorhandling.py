import ssl
import certifi
import json

from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from urllib.parse import urlencode


def make_request(url, headers=None, data=None):
    request = Request(url, headers=headers or {}, data=data)
    try:
        with urlopen(request, timeout=10) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("request timed out")


if __name__ == '__main__':
    # make_request(
    #     "https://httpstat.us/200",
    #     {"User-Agent": "save-an-animal-scraper"}
    # )
    # make_request(
    #     "https://httpstat.us/403",
    #     {"User-Agent": "save-an-animal-scraper"}
    # )

    # simulate SSL errors
    # make_request("https://superfish.badssl.com/")

    # unverified_context = ssl._create_unverified_context()
    # print(urlopen("https://superfish.badssl.com/", context=unverified_context))
    # certifi_context = ssl.create_default_context(cafile=certifi.where())
    # print(urlopen("https://sha384.badssl.com/", context=certifi_context))

    post_dict = {"Title": "Hello World", "Name": "Real Python"}
    json_string = json.dumps(post_dict)
    print(json_string)
    url_encoded_data = urlencode(post_dict)
    # print(url_encoded_data)
    # post_data = url_encoded_data.encode("utf-8")
    post_data = json_string.encode('utf-8')
    body, response = make_request(
        "https://httpbin.org/anything",
        data=post_data,
        headers={'Content-Type': 'application/json'}
    )
    # print(body.decode('utf-8'))
