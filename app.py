from server.httpserver import HttpServer

if __name__ == "__main__":
    server = HttpServer("", 8080)
    server.start()
