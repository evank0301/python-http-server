from server.httpserver import HttpServer


def say_hello():
    print("Hello")


if __name__ == "__main__":
    server = HttpServer("", 8080)
    server.add_route("GET", "/hello", say_hello)
    server.start()
