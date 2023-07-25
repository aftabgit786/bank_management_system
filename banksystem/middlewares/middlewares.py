import datetime


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            username = request.user.username

            log_format = f"[{datetime.datetime.now()}] User: {username}, Method: {request.method}, Path: {request.path}\n"
            with open('middlewares.log', 'a') as file_write:
                file_write.write(log_format)

        return response
