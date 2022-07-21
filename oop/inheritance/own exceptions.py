class ExceptionPrintSendData(Exception):
    """Класс исключений при отправке данных принтеру"""


class PrintData:
    def print_data(self, data):
        self.send_data(data)
        print(f'печать {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Принтер не отвечает')

    def send_to_print(self, data):
        return False


# p = PrintData()
# p.print_data('123')
