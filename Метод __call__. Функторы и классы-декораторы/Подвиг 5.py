class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ('ol', 'ul') else 'ul'

    def __call__(self, *args, **kwargs):
        return '\n'.join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', args[0]), f'</{self.type_list}>'])

    """
    def __call__(self, *args, **kwargs):
        for i in range(len(args[0])):
            args[0][i] = f'<li>{args[0][i]}</li>'
        if self.type_list == 'ol':
            return "<ol>" + "\n" + "\n".join(args[0]) + "\n" + '</ol>'
        return "<ul>" + "\n" + "\n".join(args[0]) + "\n" + '</ul>'
    """




lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)