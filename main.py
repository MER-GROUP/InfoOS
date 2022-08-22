# *****************************************************************************************
# InfoOS - информация об устройстве и ОС
# *****************************************************************************************
# версия проекта
__version__ = '1.00'
# *****************************************************************************************
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
# глобальные переменные
# является ли ОС - android
os_is_android = True
# *****************************************************************************************
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
# глобальная переменная
# разрешен ли доступ на чтение и запись файлов
is_access_open = True

# если ОС Android, то загрузить следующие модули
if 'android' == platform:
    # ----------------------------------------------------------------------
    # модуль plyer - работа с железом устройства
    # from plyer import vibrator
    # ----------------------------------------------------------------------
    # permissions - права доступа на чтение и запись файлов
    from android.permissions import Permission, request_permissions, check_permission

    # проверить права доступа
    def check_permissions(perms):
        for perm in perms:
            if check_permission(perm) != True:
                is_access_open = False
                return False
        return True

    # определить права доступа
    perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
    # perms = [Permission.WRITE_EXTERNAL_STORAGE, 
    #         Permission.READ_EXTERNAL_STORAGE, 
    #         Permission.INSTALL_PACKAGES]
        
    # Получить права доступа на чтение и запись
    while check_permissions(perms)!= True:
        request_permissions(perms)
    # ----------------------------------------------------------------------
# *****************************************************************************************
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
# декоратор для DropDown
# выпадающее кнопочное меню
class CustomDropDown(DropDown):
    pass
# *****************************************************************************************
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
# запуск программы
# делаем обработку ошибок и исключений и выводим на экран
if __name__ == '__main__':
    # InfoApp().run()
    info_os = InfoApp()
    try:
        info_os.run()
    except (AttributeError) as e:
        error = 'ERROR: ' + str(e)
        print(error)
        info_os.stop()
        # exit(1)
    except (Exception) as e:
        error = 'ERROR: ' + str(e)
        print(error)
        info_os.api_str = error
        info_os.run()
# *****************************************************************************************