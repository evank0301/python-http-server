import socket

from .utils.rest.request import Request
from .utils.rest.router import RequestRouter


class HttpServer:

    def __init__(self, route, port):
        self.route = route
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _parse_request(self, request):
        split_request = request.split("\r\n")
        route_info = split_request[0]
        split_route_info = route_info.split(" ")
        return Request(split_route_info[0], split_route_info[1], split_request[-1])

    def start(self):
        self.server_socket.bind((self.route, self.port))
        self.server_socket.listen(1)

        while True:

            client_socket, address = self.server_socket.accept()

            print("Connected with " + address[0] + ":" + str(address[1]))
            request_obj = self._parse_request(client_socket.recv(1024).decode("utf-8"))
            RequestRouter.handle_request(request_obj)

            response_line = "HTTP/1.1 200 OK\r\n"
            response_headers = (
                "Content-Type: text/html; charset=UTF-8\r\n" "Content-Length: {}\r\n"
            )
            response_body = "<html><body><h1>Hello, World!</h1></body></html>\r\n"
            http_response = (
                response_line
                + response_headers.format(len(response_body))
                + "\r\n"
                + response_body
            )

            client_socket.sendall(http_response.encode("utf-8"))
            client_socket.close()
