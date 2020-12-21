from http.server import HTTPServer, BaseHTTPRequestHandler


class requestHandler(BaseHTTPRequestHandler):










def main():
    port = 8000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, requestHandler)
    print('server running on port %s' % port)
    server.serve_forever()


if __name__ == "__main__":
    main()