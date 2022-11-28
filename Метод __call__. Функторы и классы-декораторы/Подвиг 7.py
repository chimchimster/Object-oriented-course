class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            m = request.get('method', 'GET')
            f = request.get('method', 'POST')
            if m in self.methods and m == 'GET':
                    return self.get(func, request)
            elif f in self.methods and f == 'POST':
                    return self.post(func, request)
            return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "POST", "url": "contact.html"})
print(res)

@Handler(methods=('POST'))
def index(request):
    return "index"

assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"