#!/usr/bin/env python3

import sys
import random
import http.server
import socketserver

HOST = "127.0.0.1"
PORT = random.randint(8000, 65535)

try:
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
except:
    pass

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

if __name__ == '__main__':
    with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
        try:
            print(f"serving at http://{HOST}:{PORT}")
            httpd.serve_forever()
        except:
            print(f"failed to run server at http://{HOST}:{PORT}")
            httpd.shutdown()
            httpd.server_close()

