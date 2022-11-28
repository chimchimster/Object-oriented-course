class Viber:
    sms_damp = list()


    @classmethod
    def add_message(cls, msg):
        cls.sms_damp.append(msg)



    @classmethod
    def remove_message(cls, msg):
        cls.sms_damp.pop(cls.sms_damp.index(msg))

    @classmethod
    def set_like(cls, msg):
        if not msg.fl_like:
            msg.fl_like = True
        else:
            msg.fl_like = False

    @classmethod
    def show_last_message(cls, number):
        return cls.sms_damp[:-number]

    @classmethod
    def total_messages(cls):
        return len(cls.sms_damp)


class Message:

    def __init__(self, text):
        self.text = text
        self.fl_like = False




msg = Message("Всем привет!")
Viber.add_message(msg)

Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.set_like(msg)

for i in Viber.sms_damp:
    print(i.__dict__)