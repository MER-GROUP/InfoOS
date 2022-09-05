'''
module Access - класс для работы с правами доступа ОС Android

Дополнительные сторонние модули для обработки файлов
    android
    pyjnius

Реализация функций модуля - Макс Романенко (Red Alert) - 2022г.

Функции:\n
    permission_set(permissions_arr: list[str]) -> (None|str)\n

Инструкция:\n
    Не забываем добавить все Permissions в файл buildozer.spec\n
    # (list) Permissions\n
    android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE, VIBRATE, INSTALL_PACKAGES\n

Расшифровка некоторых Permissions:\n
    READ_EXTERNAL_STORAGE - разрешить чтение файлов на устройстве\n
    WRITE_EXTERNAL_STORAGE - разрешить запись файлов на устройстве\n
    VIBRATE - разрешить вибрацию устройства\n
    INSTALL_PACKAGES - разрешить доступ к установленным пакетам (API 30 и выше)\n
    INTERNET - разрешить доступ в интернет\n

Пример создания массива Permissions:\n
    perms = ['Permission.WRITE_EXTERNAL_STORAGE',\n
            'Permission.READ_EXTERNAL_STORAGE',\n
            'Permission.VIBRATE',\n
            'Permission.INSTALL_PACKAGES',\n
            'Permission.INTERNET']\n
'''
# *****************************************************************************************
# доступность функций вне модуля
__all__ = ('permission_set')
# *****************************************************************************************
# module
# if 'android' == platform:
if hasattr(__import__('sys'), 'getandroidapilevel'):
    # api_version - определение версии SDK программного обеспечения
    from android import api_version
    # permissions - права доступа на чтение и запись файлов
    from android.permissions import Permission, request_permissions, check_permission
    # autoclass - импорт java классов
    # JavaException - работа с исключениями java классов
    from jnius import autoclass, cast, JavaException
# *****************************************************************************************
# vars
# if 'android' == platform:
if hasattr(__import__('sys'), 'getandroidapilevel'):
    # словарь Permission
    API_DICT = {'Permission.WRITE_EXTERNAL_STORAGE': Permission.WRITE_EXTERNAL_STORAGE,
        'Permission.READ_EXTERNAL_STORAGE': Permission.READ_EXTERNAL_STORAGE,
        'Permission.VIBRATE': Permission.VIBRATE,
        'Permission.INSTALL_PACKAGES': Permission.INSTALL_PACKAGES, # API 30
        'Permission.INTERNET': Permission.INTERNET}
    # список Permission
    API_ALL = list()
    API_30 = [Permission.INSTALL_PACKAGES]
# for tests
else:
    API_ALL = ['Permission.WRITE_EXTERNAL_STORAGE',
            'Permission.READ_EXTERNAL_STORAGE',
            'Permission.VIBRATE',
            'Permission.INSTALL_PACKAGES', # API 30
            'Permission.INTERNET']
    API_30 = ['Permission.INSTALL_PACKAGES']
# ---------------------------------------------------------------------------
# Задать разрешения для ОС Android
def permission_set(permissions_arr: list[str]) -> (None|str):
    '''
    Eng:\n
    Set permissions for Android OS.\n
    Rus:\n
    Задать разрешения для ОС Aandrois.\n
    '''
    # if 'android' == platform:
    if hasattr(__import__('sys'), 'getandroidapilevel'):
        try:
            # algorithm
            # конвертация Permission
            __converter_str_to_permission(permissions_arr)
            # определить права доступа
            # API 30 и больше + Permission которые добавлены в API 30
            # и Permission которые не менялись в API
            if (30 <= api_version):
                perms = API_ALL
            # API 29 и меньше + и Permission которые не менялись в API
            else:              
                perms = list(set(API_ALL).difference(set(API_30)))             
            # Получить права доступа на чтение и запись
            while __permissions_check(perms)!= True:
                request_permissions(perms)
        except JavaException as e:
            return 'EXCEPT JAVA: ' + str(e)
        except BaseException as e:
            return 'EXCEPT PYTHON: ' + str(e)
    else:
        # return 'Данный метод не реализован ...'
        return 'This method is not implemented ...'
# *****************************************************************************************
# конвертация текстовой строки Permission в объект Permission
def __converter_str_to_permission(permissions_arr: list[str]) -> None:
    for perm in permissions_arr:
        API_ALL.append(API_DICT[perm])
# *****************************************************************************************
# проверить права доступа на доступ
def __permissions_check(self, perms) -> None:
    for perm in perms:
        if check_permission(perm) != True:
            return False
    return True
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    # method
    '''
    # Пересечение множеств: метод intersection()
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {3, 4, 6, 7, 8}
    myset3 = myset1.intersection(myset2)
    print(myset3)
    '''
    # test1
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {3, 4, 6, 7, 8}
    myset3 = myset1.intersection(myset2)
    print(bool(myset3))
    # test2
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {6, 7, 8}
    myset3 = myset1.intersection(myset2)
    print(bool(myset3))
    # test3
    myset = set(API_ALL).intersection(set(API_30))
    print(bool(myset))
    '''
    # Разность множеств: метод difference()
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {3, 4, 6, 7, 8}
    myset3 = myset1.difference(myset2)
    print(myset3)
    '''
    # test4
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {3, 4, 6, 7, 8}
    myset3 = myset1.difference(myset2)
    print(myset3)
    # test5
    myset = set(API_ALL).difference(set(API_30))
    print(myset)
    print(list(myset))
# *****************************************************************************************