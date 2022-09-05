'''
class Permission - класс для работы с правами доступа ОС Android

Дополнительные сторонние модули для обработки файлов
    android
    pyjnius

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# module
# api_version - определение версии SDK программного обеспечения
from android import api_version
# autoclass - импорт java классов
# JavaException - работа с исключениями java классов
from jnius import autoclass, cast, JavaException
# *****************************************************************************************
# Permission - класс для работы с правами доступа ОС Android
class Net:
    '''
    class Permission - класс для работы с правами доступа ОС Android\n
    методы:\n
        None\n
    '''
    # ---------------------------------------------------------------------------
    # vars
    pass
    # ---------------------------------------------------------------------------
    # Задать разрешения для ОС Aandrois
    def permission_set(self, permissions_arr: list[str]) -> (None|str):
        '''
        Eng:\n
        Set permissions for Android OS.\n
        Rus:\n
        Задать разрешения для ОС Aandrois.\n
        '''
        # if 'android' == platform:
        if hasattr(__import__('sys'), 'getandroidapilevel'):
            try:
                pass
            except JavaException as e:
                return 'EXCEPT JAVA: ' + str(e)
            except BaseException as e:
                return 'EXCEPT PYTHON: ' + str(e)
        else:
            # return 'Данный метод не реализован ...'
            return 'This method is not implemented ...'
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    # method
    pass
# *****************************************************************************************