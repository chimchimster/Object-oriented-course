class AppStore:
    apps = list()

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.pop(self.apps.index(app))

    def block_application(self, app):
        Application.blocked = True

    def total_apps(self):
        return len(self.apps)

class Application:
    blocked = False
    def __init__(self, name):
        self.name = name


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)

#store.remove_application(app_youtube)