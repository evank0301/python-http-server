import socket

from .utils.rest.request import Request
from .utils.rest.response import Response


class HttpServer:

    def __init__(self, route, port):
        self.route = route
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.routes = {}

    def _parse_request(self, request):
        split_request = request.split("\r\n")
        route_info = split_request[0]
        split_route_info = route_info.split(" ")
        return Request(split_route_info[0], split_route_info[1], split_request[-1])

    def add_route(self, method, route, function):
        route_tuple = (method, route)
        if route_tuple in self.routes:
            print(f"Overriding exisitng mapping for {method} at {route}")
        print(f"Exposing {route} for {method} operations")
        self.routes[route_tuple] = function

    def _handle_request(self, request):
        if (request.get_method(), request.get_route()) in self.routes:
            return self.routes[(request.get_method(), request.get_route())]()
        else:
            print(
                f"{request.get_route()} is NOT exposed for {request.get_method()} operations"
            )
            return Response(
                "404 NOT FOUND",
                "Content-Type: text/html; charset-UTF-8\r\n" "Content-Length: 18\r\n",
                "No Route Available",
            )

    def start(self):
        self.server_socket.bind((self.route, self.port))
        self.server_socket.listen(1)

        while True:

            client_socket, address = self.server_socket.accept()

            print("Connected with " + address[0] + ":" + str(address[1]))
            request_obj = self._parse_request(client_socket.recv(1024).decode("utf-8"))
            response_obj = self._handle_request(request_obj)

            client_socket.sendall(str(response_obj).encode("utf-8"))
            client_socket.close()
