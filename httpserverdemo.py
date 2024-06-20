import http.server
import socketserver
PORT=9000
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",PORT),Handler) as httpd:
    print("serveing at port",PORT)
    httpd.serve_forever()