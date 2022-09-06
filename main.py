# *****************************************************************************************
# +++++++++++++++++++++++++++++++++++++ ИНФОРМАЦИЯ ++++++++++++++++++++++++++++++++++++++++
# InfoOS - информация об устройстве и ОС
# *****************************************************************************************
# версия проекта
__version__ = '1.00'
# *****************************************************************************************
# ++++++++++++++++++++++++ РАБОТА С ПРАВАДИ ДОСТУПА ВЕР1 ANDROID ++++++++++++++++++++++++++
# собственные модули
# Модуль для работы с правами доступа ОС Android
from merlib.android.Access import permission_set
perms = ['Permission.WRITE_EXTERNAL_STORAGE',
        'Permission.READ_EXTERNAL_STORAGE',
        'Permission.VIBRATE',
        'Permission.INSTALL_PACKAGES']
permission_set(perms)
# *****************************************************************************************
# ++++++++++++++++++++++++ РАБОТА С ПРАВАДИ ДОСТУПА ВЕР2 ANDROID ++++++++++++++++++++++++++
# # если ОС Android, то загрузить следующие модули
# if hasattr(__import__('sys'), 'getandroidapilevel'):
#     # ----------------------------------------------------------------------
#     # модуль plyer - работа с железом устройства
#     # from plyer import vibrator
#     # ----------------------------------------------------------------------
#     # api_version - определение версии SDK программного обеспечения
#     from android import api_version
#     # ----------------------------------------------------------------------
#     # permissions - права доступа на чтение и запись файлов
#     from android.permissions import Permission, request_permissions, check_permission
#     # ----------------------------------------------------------------------
#     # vars - права доступа которые нужно установить
#     perms_arr_str = ['Permission.WRITE_EXTERNAL_STORAGE',
#                 'Permission.READ_EXTERNAL_STORAGE',
#                 'Permission.VIBRATE',
#                 'Permission.INSTALL_PACKAGES']
#     # ----------------------------------------------------------------------
#     # vars
#     # словарь Permission
#     API_DICT = {'Permission.WRITE_EXTERNAL_STORAGE': Permission.READ_EXTERNAL_STORAGE,       
#         'Permission.INSTALL_PACKAGES': Permission.INSTALL_PACKAGES, # API 30
#         'Permission.INTERNET': Permission.INTERNET,
#         'Permission.VIBRATE': Permission.VIBRATE,
#         'Permission.WRITE_EXTERNAL_STORAGE': Permission.WRITE_EXTERNAL_STORAGE,}
#     # списки Permission
#     API_ALL = list()
#     API_30 = ['Permission.INSTALL_PACKAGES']
#     # ----------------------------------------------------------------------
#     # конвертация текстовой строки Permission в объект Permission
#     def converter_str_to_permission(perms_arr_str: list[str]) -> None:
#         for perm in perms_arr_str:
#             API_ALL.append(API_DICT[perm])
#     # ----------------------------------------------------------------------
#     # разделение прав доступа по API и конвертация Permission
#     # API 30 и больше + Permission которые добавлены в API 30
#     # API 29 и меньше + Permission которые не менялись в API
#     if (30 <= api_version):
#         converter_str_to_permission(perms_arr_str)
#     else:              
#         converter_str_to_permission(list(set(perms_arr_str).difference(set(API_30))))
#     # ----------------------------------------------------------------------  
#     # проверить права доступа
#     def check_permissions(perms):
#         for perm in perms:
#             if check_permission(perm) != True:
#                 return False
#         return True         
#     # ----------------------------------------------------------------------           
#     # Получить права доступа на чтение и запись
#     while check_permissions(API_ALL)!= True:
#         request_permissions(API_ALL)
#     # ----------------------------------------------------------------------
# *****************************************************************************************
# ++++++++++++++++++++++++ РАБОТА С ПРАВАДИ ДОСТУПА ВЕР3 ANDROID ++++++++++++++++++++++++++
# # глобальная переменная
# # разрешен ли доступ на чтение и запись файлов
# is_access_open = True

# # если ОС Android, то загрузить следующие модули
# if hasattr(__import__('sys'), 'getandroidapilevel'):
#     # ----------------------------------------------------------------------
#     # модуль plyer - работа с железом устройства
#     # from plyer import vibrator
#     # ----------------------------------------------------------------------
#     # api_version - определение версии SDK программного обеспечения
#     from android import api_version
#     # ----------------------------------------------------------------------
#     # permissions - права доступа на чтение и запись файлов
#     from android.permissions import Permission, request_permissions, check_permission

#     # проверить права доступа
#     def check_permissions(perms):
#         for perm in perms:
#             if check_permission(perm) != True:
#                 is_access_open = False
#                 return False
#         return True

#     # определить права доступа
#     if 30 > api_version:
#         perms = [Permission.WRITE_EXTERNAL_STORAGE, 
#                 Permission.READ_EXTERNAL_STORAGE]
#     else:
#         perms = [Permission.WRITE_EXTERNAL_STORAGE, 
#                 Permission.READ_EXTERNAL_STORAGE, 
#                 Permission.INSTALL_PACKAGES]
        
#     # Получить права доступа на чтение и запись
#     while check_permissions(perms)!= True:
#         request_permissions(perms)
#     # ----------------------------------------------------------------------
# *****************************************************************************************
# ++++++++++++++++++++++++++++++ РАБОТА С ФАЙЛОВОЙ СИСТЕМОЙ +++++++++++++++++++++++++++++++
# собственные модули
# Работа с директориями и файлами ОС
from merlib.fs.File import File
pre_file = File()
directory_downloads = pre_file.file_get_path_to_downloads()
# *****************************************************************************************
# ++++++++++++++++++++++++++++++ РАБОТА С ЛОГИРОВАНИЕМ ++++++++++++++++++++++++++++++++++++
# включить/отключить логирование
if True:
    # работа с логированием
    import logging
    # настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        # level=logging.WARNING,
        # level=logging.ERROR,
        # level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        filename = directory_downloads + 'debug.log' \
                    if hasattr(__import__('sys'), 'getandroidapilevel') \
                    else './debug.log', 
        filemode = 'w'
        # handlers=[
        #     logging.FileHandler("/storage/emulated/0/Download/debug.log"), # for Android
        #     logging.FileHandler("debug.log"), # for other OS
        #     logging.StreamHandler()
        # ]
    )
# *****************************************************************************************
# ++++++++++++++++++++++++++++++ ИМПОРТ МОДУЛЕЙ KIVY ++++++++++++++++++++++++++++++++++++++
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# работа с экраном
from kivy.uix.screenmanager import Screen
# выпадающее меню из кнопок
from kivy.uix.dropdown import DropDown
# свойства объекта (виджета)
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
# определение ОС
from kivy.utils import platform
# *****************************************************************************************
# ++++++++++++++++++++++++++++++ ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ++++++++++++++++++++++++++++++++++++
# глобальные переменные
# является ли ОС - android
os_is_android = True
# *****************************************************************************************
# ++++++++++++++++++++++++++++++ ИМПОРТ МОДУЛЕЙ KIVY ++++++++++++++++++++++++++++++++++++++
# если не ОС не android, то применить следующие настройки
if not 'android' == platform:
    # конфигурация приложения kv
    from kivy.config import Config
    # задаем размеры окна статически
    Config.set('graphics', 'width', '640')
    Config.set('graphics', 'height', '480')
    # запрещаем изменение размеров окна
    Config.set('graphics','resizable', False)
    # является ли ОС - android
    os_is_android = False
# *****************************************************************************************
# ++++++++++++++++++++++++++++++ РАБОТА С ФАЙЛОВОЙ СИСТЕМОЙ +++++++++++++++++++++++++++++++
# Работа с директориями и файлами ОС
# listdir - показывает файлы в конкретной папке
from os import listdir
# Работа с директориями и файлами ОС
from os.path import dirname, join
# Работа с директориями и файлами ОС
from pathlib import Path
# Класс Builder - закрузчик языка KV Lang
from kivy.lang import Builder
# Builder.load_file(str(Path(join(dirname(__file__), './design/'))))
# записываем директорию в переменную kv_path
folder = './design/'
kv_path = str(Path(join(dirname(__file__), folder)))
# загрузить все файлы .kv по отдельности
for file in listdir(kv_path):
    kv_path_file = str(Path(join(kv_path, file)))
    Builder.load_file(kv_path_file)
# *****************************************************************************************
# +++++++++++++++++++++++++++++++++++ РАБОТА С ANDROID ++++++++++++++++++++++++++++++++++++
# собственные модули
# Работа с директориями и файлами ОС
from merlib.fs.File import File
file = File()
# Design - манипуляции (действия) с объектами kivy
from bind.Design import Design
# Hardware - манипуляции (действия) с железом устройства
from bind.Hardware import Hardware
# Translate - автоматическая локализация программы на родной язык
from bind.Translate import Translate
# *****************************************************************************************
# ++++++++++++++++++++++++++++++ РАБОТА С ВЫПАДАЮЩИМ МЕНЮ +++++++++++++++++++++++++++++++++
# декоратор для DropDown
# выпадающее кнопочное меню
class CustomDropDown(DropDown):
    pass
# *****************************************************************************************
# ++++++++++++++++++++++++++++++++++ ДИЗАЙН ПРОГРАММЫ +++++++++++++++++++++++++++++++++++++
# Действия программы и дизайн
class Info(BoxLayout):
    # ---------------------------------------------------------------------------
    '''root widget'''
    # ---------------------------------------------------------------------------
    # vars
    pass
    # ---------------------------------------------------------------------------
    # methods
    # конструктор класса Info
    def __init__(self, **kw):
        super().__init__(**kw)
        self.dropdown = CustomDropDown()
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# ++++++++++++++++++++++++++++++++++ РАБОТА С ПРОШРАММОЙ ++++++++++++++++++++++++++++++++++
# Окно программы
class InfoApp(App, Design, Hardware):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    # vars
    is_android = BooleanProperty(os_is_android)
    menu_str = StringProperty(
        Translate().get_translate(file.file_get_local_language(), 'menu')
    )
    api_str = StringProperty(
        Translate().get_translate(file.file_get_local_language(), 'intro')
    )
    # ---------------------------------------------------------------------------
    # kivy vars
    title = 'Info OS'
    # ---------------------------------------------------------------------------
    # Kivi constructor
    def build(self):
        return Info()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# ++++++++++++++++++++++++++++++++++++ ТЕСТ ПРОГРАММЫ +++++++++++++++++++++++++++++++++++++
# запуск программы
# вся программа логируется (в финальной версии отключите логирование программы)
if __name__ == '__main__':
    # ---------------------------------------------------------------------------
    InfoApp().run()
    # ---------------------------------------------------------------------------
    # делаем обработку ошибок и исключений и выводим на экран
    # info_os = InfoApp()
    # try:
    #     info_os.run()
    # except (AttributeError) as e:
    #     error = 'ERROR: ' + str(e)
    #     print(error)
    #     info_os.stop()
    #     # exit(1)
    # except (Exception) as e:
    #     error = 'ERROR: ' + str(e)
    #     print(error)
    #     info_os.api_str = error
    #     info_os.run()
    # ---------------------------------------------------------------------------
# *****************************************************************************************