'''
class Design - класс для манипуляции (действия) с объектами kivy

Дополнительные сторонние модули для обработки файлов
    kivy

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# Design - манипуляции (действия) с объектами kivy
class Design:
    '''
    class Design - класс для манипуляции (действия) с объектами kivy\n
    методы:\n
        button_disable(self, buttton) -> None\n
        button_enable(self, buttton) -> None\n
        change_text(self, label, text) -> None\n
    '''
    # ---------------------------------------------------------------------------
    # отключение кнопки (объект Button) при нажатии
    def button_disable(self, buttton) -> None:
        '''
        Eng:\n
        Disabling a button (Button object) when pressed.\n
        :param buttton: a copy of the Button object.\n
        Rus:\n
        Отключение кнопки (объект Button) при нажатии.\n
        :параметр buttton: копия объекта Button.\n
        '''
        buttton.disabled = True
    # ---------------------------------------------------------------------------
    # включение кнопки (объект Button) при нажатии
    def button_enable(self, buttton) -> None:
        '''
        Eng:\n
        Enabling a button (Button object) when pressed.\n
        :param buttton: a copy of the Button object.\n
        Rus:\n
        Включение кнопки (объект Button) при нажатии.\n
        :параметр buttton: копия объекта Button.\n
        '''
        buttton.disabled = False
    # ---------------------------------------------------------------------------
    # изменение текстовой информации (объект Label)
    def change_text(self, label, text) -> None:
        '''
        Eng:\n
        Changing text information (Label object).\n
        :param text: a copy of the Label object.\n
        Rus:\n
        Изменение текстовой информации (объект Label).\n
        :параметр text: копия объекта Label.\n
        '''
        label.text = text
    # ---------------------------------------------------------------------------
    # Methods
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    pass
# *****************************************************************************************