class RequestRouter:

    @staticmethod
    def handle_request(request):

        match request.get_method():
            case "GET":
                print("Received Get Request")

            case "POST":
                print("Received Post Request")

            case _:
                print("Other Methods Not Supported")
