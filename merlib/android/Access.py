'''
module Access - для работы с правами доступа ОС Android

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
# Задать разрешения для ОС Android
def permission_set(permissions_arr: list[str]) -> (None|str):
    '''
    Eng:\n
        Set permissions for Android OS.\n
    Rus:\n
        Задать разрешения для ОС Aandrois.\n

    Пример создания массива Permissions:\n
        permissions_arr = ['Permission.WRITE_EXTERNAL_STORAGE',\n
                        'Permission.READ_EXTERNAL_STORAGE',\n
                        'Permission.VIBRATE',\n
                        'Permission.INSTALL_PACKAGES']\n

    Не забываем добавить все Permissions в файл buildozer.spec\n
        # (list) Permissions\n
        android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE, VIBRATE, INSTALL_PACKAGES\n
    '''
    if hasattr(__import__('sys'), 'getandroidapilevel'):
        try:
            # ----------------------------------------------------------------------
            # autoclass - импорт java классов
            # JavaException - работа с исключениями java классов
            from jnius import autoclass, cast, JavaException
            # ----------------------------------------------------------------------
            # api_version - определение версии SDK программного обеспечения
            from android import api_version
            # ----------------------------------------------------------------------
            # permissions - права доступа на чтение и запись файлов
            from android.permissions import Permission, request_permissions, check_permission
            # ----------------------------------------------------------------------
            # vars - права доступа которые нужно установить
            # # for tests #############################################
            # perms_arr_str = ['Permission.WRITE_EXTERNAL_STORAGE', ###
            #             'Permission.READ_EXTERNAL_STORAGE',       ###
            #             'Permission.VIBRATE',                     ###
            #             'Permission.INSTALL_PACKAGES']###############
            perms_arr_str = permissions_arr
            # ----------------------------------------------------------------------
            # vars
            # словарь Permission
            API_DICT = {'Permission.WRITE_EXTERNAL_STORAGE': Permission.READ_EXTERNAL_STORAGE,       
                'Permission.INSTALL_PACKAGES': Permission.INSTALL_PACKAGES, # API 30
                'Permission.INTERNET': Permission.INTERNET,
                'Permission.VIBRATE': Permission.VIBRATE,
                'Permission.WRITE_EXTERNAL_STORAGE': Permission.WRITE_EXTERNAL_STORAGE,}
            # списки Permission
            API_ALL = list()
            API_30 = ['Permission.INSTALL_PACKAGES']
            # ----------------------------------------------------------------------
            # конвертация текстовой строки Permission в объект Permission
            def converter_str_to_permission(perms_arr_str: list[str]) -> None:
                for perm in perms_arr_str:
                    API_ALL.append(API_DICT[perm])
            # ----------------------------------------------------------------------
            # разделение прав доступа по API и конвертация Permission
            # API 30 и больше + Permission которые добавлены в API 30
            # API 29 и меньше + Permission которые не менялись в API
            if (30 <= api_version):
                converter_str_to_permission(perms_arr_str)
            else:              
                converter_str_to_permission(list(set(perms_arr_str).difference(set(API_30))))
            # ----------------------------------------------------------------------  
            # проверить права доступа
            def check_permissions(perms):
                for perm in perms:
                    if check_permission(perm) != True:
                        return False
                return True         
            # ----------------------------------------------------------------------           
            # Получить права доступа на чтение и запись
            while check_permissions(API_ALL)!= True:
                request_permissions(API_ALL)
            # ----------------------------------------------------------------------
        except JavaException as e:
            return 'EXCEPT JAVA: ' + str(e)
        except BaseException as e:
            return 'EXCEPT PYTHON: ' + str(e)
    else:
        # return 'Данный метод не реализован ...'
        return 'This method is not implemented ...'
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
    '''
    # Разность множеств: метод difference()
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {3, 4, 6, 7, 8}
    myset3 = myset1.difference(myset2)
    print(myset3)
    '''
    # test3
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {3, 4, 6, 7, 8}
    myset3 = myset1.difference(myset2)
    print(myset3)
    # test4
    # vars
    # словарь Permission
    API_DICT = {'Permission.WRITE_EXTERNAL_STORAGE': 'WRITE_EXTERNAL_STORAGE',
        'Permission.READ_EXTERNAL_STORAGE': 'READ_EXTERNAL_STORAGE',
        'Permission.VIBRATE': 'VIBRATE',
        'Permission.INSTALL_PACKAGES': 'INSTALL_PACKAGES', # API 30
        'Permission.INTERNET': 'INTERNET'}
    # строковый список Permission
    perms_str = ['Permission.WRITE_EXTERNAL_STORAGE',
                'Permission.READ_EXTERNAL_STORAGE',
                'Permission.VIBRATE',
                'Permission.INSTALL_PACKAGES',
                'Permission.INTERNET']
    # список Permission
    API_ALL = list()
    API_30 = ['Permission.INSTALL_PACKAGES']
    # конвертация текстовой строки Permission в объект Permission
    def converter_str_to_permission(perms_str: list[str]) -> None:
        for perm in perms_str:
            API_ALL.append(API_DICT[perm])
    converter_str_to_permission(perms_str)
    # Вывод словаря
    print(f'API_ALL = {API_ALL}')
    # исключаем API 30 c помощью множества
    API_ALL = list(set(perms_str).difference(set(API_30)))
    # Вывод API_ALL
    print(f'API_ALL = {API_ALL}')
# *****************************************************************************************