import os
import hashlib
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver


class CachingHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Path to the file you want to serve
        file_path = 'index.html'
        
        # Check if the file exists
        if not os.path.exists(file_path):
            self.send_error(404, "File Not Found")
            return
        
        # Get the file's last modified time
        file_mtime = os.path.getmtime(file_path)
        
        # Generate ETag based on file content (MD5 hash of the file)
        with open(file_path, 'rb') as file:
            file_content = file.read()
            etag = hashlib.md5(file_content).hexdigest()
        
        # Convert the file's last modified time to a formatted string
        last_modified = self.date_time_string(file_mtime)
        
        # Check if the client sent "If-None-Match" (ETag) or "If-Modified-Since" headers
        if 'If-None-Match' in self.headers:
            client_etag = self.headers['If-None-Match']
            if client_etag == etag:
                # If the ETag matches, send a 304 Not Modified response
                self.send_response(304)
                self.send_header('ETag', etag)
                self.send_header('Last-Modified', last_modified)
                self.end_headers()
                return

        if 'If-Modified-Since' in self.headers:
            client_mtime = self.headers['If-Modified-Since']
            client_mtime = time.mktime(time.strptime(client_mtime, "%a, %d %b %Y %H:%M:%S GMT"))
            if file_mtime <= client_mtime:
                # If the file hasn't been modified since the client last checked
                self.send_response(304)
                self.send_header('ETag', etag)
                self.send_header('Last-Modified', last_modified)
                self.end_headers()
                return
        
        # If the file has been modified or no conditional request, send the file
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('ETag', etag)
        self.send_header('Last-Modified', last_modified)
        self.end_headers()
        
        # Send the file content
        self.wfile.write(file_content)


def run(server_class=HTTPServer, handler_class=CachingHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving HTTP caching server at http://localhost:{port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run(port=8080)

