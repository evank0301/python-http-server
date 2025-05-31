from server.httpserver import HttpServer
from server.utils.rest.response import Response


if __name__ == "__main__":
    server = HttpServer("", 8080)

    @server.get_mapping("/hello")
    def say_hello():
        return_string = "Hello Server\n"
        return Response(
            "200 OK",
            "Content-Type: text/html; charset=UTF-8\r\n"
            f"Content-Length: {len(return_string)}\r\n",
            return_string,
        )

    @server.get_mapping("/goodbye")
    def say_goodbye():
        return_string = "Goodbye Server\n"
        return Response(
            "200 OK",
            "Content-Type: text/html; charset=UTF-8\r\n"
            f"Content-Length: {len(return_string)}\r\n",
            return_string,
        )

    server.start()

    say_hello()
