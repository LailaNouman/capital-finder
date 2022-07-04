from http.server import BaseHTTPRequestHandler
import requests
from urllib import parse

class Capital(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        Capital = ""
        if 'country' in dic:
            word = dic['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + word)
            data = r.json()
            for capital in data:
                Capital = capital['capital'][0]

            message = str(Capital)

        else:
            message = "Please provide us a correct country Name"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return