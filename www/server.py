#!/bin/sh
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()
    
    def do_POST(self):
        print('[Request method] POST')
        print('[Request headers]\n' + str(self.headers))
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len).decode('utf-8') 

        print('[Request doby]\n' + post_body)
        post_json = json.loads(post_body)
        if post_json["status"] == 1:
            f = open("post_response.json")
            response_body = f.read().encode()
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=UTF-8')
            self.send_header('Content-length', len(response_body))
            self.end_headers()
            self.wfile.write(response_body)
        else:
            response_body = b"Error"
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=UTF-8')
            self.send_header('Content-length', len(response_body))
            self.end_headers()
            self.wfile.write(response_body)
        #print('[Response body]\n' + response_body.decode('utf-8'))



    
host = 'localhost'
port = 8080
httpd = HTTPServer((host, port), MyHandler)
print('serving at port', port)
httpd.serve_forever()