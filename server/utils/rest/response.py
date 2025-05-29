class Response:

    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self):
        return (
            f"HTTP/1.1 {self.status}\r\n"
            + self.headers
            + "\r\n"
            + self.body
        )
