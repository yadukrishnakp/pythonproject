from http.server import HTTPServer, BaseHTTPRequestHandler


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        a = (self.date_time_string())
        b = self.client_address[0]
        c = self.command
        d = self.path
        e = self.client_address[1]


def main():
    port = 8000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, requestHandler)
    print('server running on port %s' % port)
    server.serve_forever()


if __name__ == "__main__":
    main()