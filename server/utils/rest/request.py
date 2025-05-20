class Request:

    def __init__(self, method, route, body):
        self.method = method
        self.route = route
        self.body = body

    def get_method(self):
        return self.method

    def get_route(self):
        return self.route

    def get_body(self):
        return self.body
