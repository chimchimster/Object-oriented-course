class Router:
    def __init__(self):
        self.buffer = list()
        self.linked = dict()

    def link(self, server):
        self.linked[server.ip] = server
        server.router = self

    def unlink(self, server):
        s = self.linked.pop(server.ip, False)
        if s:
            server.router = None

    def send_data(self):
        for d in self.buffer:
            if d.ip in self.linked:
                self.linked[d.ip].buffer.append(d)
        self.buffer.clear()


class Server:
    ip = 0

    def __init__(self):
        self.buffer = list()
        self.ip = Server.ip
        Server.ip += 1
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)


    def get_data(self):
        buf = self.buffer.copy()
        self.buffer.clear()
        return buf

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
print(msg_lst_from)
msg_lst_to = sv_to.get_data()
print(msg_lst_to)
