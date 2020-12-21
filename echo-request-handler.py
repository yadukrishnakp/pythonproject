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
        output = ''
        output += '<html><body>'
        output += '<title>request information</title>'
        output += '<h1>Echo request information</h1>'
        output += '<h3>time and date</h3>'
        output += str(a)
        output += '<h3>client_host</h3>'
        output += str(b)
        output += '<h3>client_host</h3>'
        output += str(e)
        output += '<h3>command</h3>'
        output += str(c)
        output += '<h3>path</h3>'
        output += str(d)
        output += '</body></html>'
        self.wfile.write((output.encode()))


def main():
    port = 8000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, requestHandler)
    print('server running on port %s' % port)
    server.serve_forever()


if __name__ == "__main__":
    main()