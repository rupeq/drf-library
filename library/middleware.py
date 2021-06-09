import random


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['HTTP-X-Test'] = random.randint(0, 100000)
        return response
