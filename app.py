from server.httpserver import HttpServer
from server.utils.rest.response import Response


def say_hello():
    return_string = "Hello Server\n"
    return Response(
        "200 OK",
        "Content-Type: text/html; charset=UTF-8\r\n"
        f"Content-Length: {len(return_string)}\r\n",
        return_string,
    )


if __name__ == "__main__":
    server = HttpServer("", 8080)
    server.add_route("GET", "/hello", say_hello)
    server.start()
