'''
class Permission - класс для работы с правами доступа ОС Android

Дополнительные сторонние модули для обработки файлов
    android
    pyjnius

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
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
# Permission - класс для работы с правами доступа ОС Android
class Permission:
    '''
    class Permission - класс для работы с правами доступа ОС Android\n
    методы:\n
        None\n

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
        perms = [Permission.WRITE_EXTERNAL_STORAGE,\n
                Permission.READ_EXTERNAL_STORAGE,\n
                Permission.VIBRATE,\n
                Permission.INSTALL_PACKAGES,\n
                Permission.INTERNET]\n
    '''
    # ---------------------------------------------------------------------------
    # vars
    # список Permission
    # if 'android' == platform:
    if hasattr(__import__('sys'), 'getandroidapilevel'):
        API_ALL = [Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.VIBRATE,
            Permission.INSTALL_PACKAGES,
            Permission.INTERNET]
        API_30 = [Permission.INSTALL_PACKAGES]
    else:
        API_ALL = ['Permission.WRITE_EXTERNAL_STORAGE',
            'Permission.READ_EXTERNAL_STORAGE',
            'Permission.VIBRATE',
            'Permission.INSTALL_PACKAGES',
            'Permission.INTERNET']
        API_30 = ['Permission.INSTALL_PACKAGES']
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
    myset = set(Permission.API_ALL).intersection(set(Permission.API_30))
    print(bool(myset))
# *****************************************************************************************