from communication import SmsSender


class TestableSmsSender(SmsSender):

    def __init__(self):
        self.__send_method_is_called = False

    def send(self, schedule):
        print('')
        self.__send_method_is_called = True

    def is_send_method_is_called(self):
        return self.__send_method_is_called
