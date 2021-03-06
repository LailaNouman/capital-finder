from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        print(url_components)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(dic)
        definitions = []
        if 'word' in dic:
            word = dic['word']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + word)
            data = r.json()
            for word_data in data:
                definition = f"The capital of {word} is {word_data['capital'][0]}"
                definitions.append(definition)

            message = str(definitions)

        else:
            message = "Please provide me with a word = name of a country"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return