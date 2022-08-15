'''
class File - класс для обработки файлов

Дополнительные стандартные модули для обработки файлов
    shutil
    sys
    os.path
    os
    stat
    pathlib

Реализация методов класса - Максим Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# модуль для легкого копирования файлов и папок
# shutil.copyfileobj - копирование файлового объекта
# shutil.rmtree - удаление непустой папки/директории с носителя
import shutil
# модуль для работы с вводом и выводом в консоль
# sys.stdout - вывод информации в терминал (консоль)
# sys.platform - определение иммени платформы (операционной системы)
import sys
# импортируем молуль os.path
# dirname - определяем текущую директорию
# join - объеденяем директорию + файл (правильный путь файла)
# exists - проверяет существует ли файл или директория
from os.path import dirname, join, exists
# импортируем молуль os
# os.stat(<file>).st_mode - получить состояние (права доступа) файла/папки в виде числа
# os.path.join(Path.home(), "Downloads") - получить путь/директорию к папке Downloads
import os
# импортируем молуль os
# remove - удаляет указанный файл
# listdir - получает все файлы и папки в текущей директории
# chmod - управление правами доступа у файлам и директориям
# mkdir - создание директории/папки
# rmdir - удаляет пустую папку/директорию
from os import remove, listdir, chmod, mkdir, rmdir
# импортируем молуль stat (работа с разрешениями прав доступа файлов и папок)
# stat.filemode - получить состояние (права доступа) файла/папки в виде строки (rwx)
# stat.S_IMODE - получить состояние (права доступа) файла/папки в виде числа (777)
# stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO - права доступа rwxrwxrwx (весь доступ разрешен)
# stat.S_ENFMT - права доступа -----S--- (весь доступ запрещен)
import stat
# импортируем молуль pathlib
# Path - задает путь к файлу
# Path.unlink - отмена связи или удаление файла по указанному пути
from pathlib import Path
# импортируем молуль locale - Сервисы интернационализации
import locale
# *****************************************************************************************
# класс для работы с файлом
class File:
    '''
    class File - класс для обработки файлов
    методы:
        file_console_print_file_utf8(file: str, curdir: str = __file__) -> None     ##########+
        file_console_print_list(arr: list) -> None                                  ##########+
        file_create(file: str, curdir: str = __file__) -> bool                      ##########+
        file_create_dir(dir: str, curdir: str = __file__) -> bool                   ##########+
        file_delete(file: str, curdir: str = __file__) -> bool                      ##########+
        file_delete_empty_folder(dir: str, curdir: str = __file__) -> bool          ##########+
        file_delete_full_folder(dir: str, curdir: str = __file__) -> bool           ##########+
        file_exists(file: str, curdir: str = __file__) -> bool                      ##########+
        file_exists_dir(dir: str, curdir: str = __file__) -> bool                   ##########+
        file_init_dir(folder: str, dir: str, curdir: str = __file__) -> str         ##########+
        file_init_name(folder: str, filename: str, curdir: str = __file__) -> str   ##########+
        file_get_current_dir_files() -> list[str]                                   ##########+
        file_get_dir_files(dir: str, curdir: str = __file__) -> list[str]           ##########+
        file_get_current_access_dir_in_str() -> list[str]                           ##########+
        file_get_current_access_dir_in_int() -> list[int]                           ##########+
        file_get_installer() -> str                                                 ##########+
        file_get_path_to_downloads() -> str                                         ##########+
        file_get_local_language() -> str                                            ##########+
        file_set_access_open_all(name: str, curdir: str = __file__) -> bool         ##########+
        file_set_access_close_all(name: str, curdir: str = __file__) -> bool        ##########+
        file_read(file: str, curdir: str = __file__) -> list[str]                   ##########+ 
        file_read_utf8(file: str, curdir: str = __file__) -> list[str]              ##########+ 
        file_write(file: str, arr: list, curdir: str = __file__) -> None            ##########+  
        file_write_append(file: str, arr: list, curdir: str = __file__) -> None     ##########+ 
        file_write_dict(file: str, dictor: dict, curdir: str = __file__) -> None    ##########+           
    '''
    # ---------------------------------------------------------------------------
    # вывод в консоль содержимого файла содержащий текст в utf-8 кодировке 
    # (аналог type filename в cmd.exe)
    def file_console_print_file_utf8(self, file: str, curdir: str = __file__) -> None:
        '''
        file_console_print_file_utf8(file: str, curdir: str = __file__) -> None\n                
                вывод в консоль содержимого файла содержащий\n        
                    текст в utf-8 кодировке\n                         
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть,\n    
                    прочитать и вывести в консоль\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n    
        примеры:\n
                file = File()\n 
                file.file_print_console_utf8('./temp/dict.txt', __file__)\n         
        '''
        try:
            # определить имя файла
            file_name = self.file_init_name('', file, curdir)
            # открыть файл, скопировать содержимое в консоль (терминал)
            with open(file_name, 'r', encoding='utf-8') as f:
                shutil.copyfileobj(f, sys.stdout)
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # вывод в консоль содержимого списка (list)
    def file_console_print_list(self, arr: list) -> None:
        '''
        file_console_print_list(arr: list) -> None\n                      
                вывод в консоль содержимого списка (list)\n           
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                arr: list - список для вывода в консоль\n 
        примеры:\n 
                file = File()\n 
                file.file_list_print_console([1, 2, 3])\n          
        '''
        try:
            for line in arr:
                # print(line.strip())
                # print(repr(line))
                # print(line, end='')
                print(line)
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # создать пустой файл
    def file_create(self, file: str, curdir: str = __file__) -> bool:
        '''
        file_create(file: str, curdir: str = __file__) -> bool\n                      
                создает пустой файл\n             
                возвращаемое значение - bool (True - создано, False - ошибка)\n    
        параметры:\n                                                
                file: str - имя файла которое неоходимо создать\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примеры:\n 
                file = File()\n 
                file.file_create('./temp/test1.txt', __file__) # True\n 
                file.file_create('./temp/test2.txt', __file__) # True\n 
                file.file_create('./temp/max/test2.txt', __file__) # False\n                     
        '''
        try:
            # инициализировать полное имя файла не нужно
            # т.к. оно инициализируется в file_write
            # создать файл и записать пустой список
            if self.file_write(file, list(), curdir) is None:
                return True
            else:
                return False
        except (Exception) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # создать указанную директорию
    def file_create_dir(self, dir: str, curdir: str = __file__) -> bool:
        '''
        file_create_dir(dir: str, curdir: str = __file__) -> bool\n                      
                создает указанную директорию\n             
                возвращаемое значение - bool (True - создано, False - ошибка)\n    
        параметры:\n                                                
                dir: str - имя директории которое неоходимо создать\n 
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примеры:\n    
                file = File()\n 
                file.file_create_dir('./temp/', __file__)\n 
                file.file_create_dir('./temp/test1/', __file__)\n 
                file.file_create_dir('./temp/test2/', __file__)\n 
                file.file_create_dir('./temp/test2/test3/', __file__))\n                  
        '''
        try:
            # определить имя создаваемой директории
            dir_name = self.file_init_dir(dir, '', curdir)
            # создать директорию
            mkdir(dir_name)
            return True
        except (Exception) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # удаление файла с носителя
    def file_delete(self, file: str, curdir: str = __file__) -> bool:
        '''
        file_delete(file: str, curdir: str = __file__) -> bool\n                      
                удаление файла с носителя\n             
                возвращаемое значение - bool (True - удалено, False - ошибка)\n    
        параметры:\n                                                
                file: str - имя файла которое неоходимо удалить с носителя\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примеры:\n    
                file = File()\n 
                file.file_delete('./temp/write.txt', __file__)\n                         
                file.file_delete('./temp/write2.txt', __file__)\n                         
        '''
        try:
            try:
                # определить имя удаляемого файла
                file_name = self.file_init_name('', file, curdir)
                # delete file
                remove(file_name)
                # return
                return True
            except(FileNotFoundError, OSError) as e:
                # определить имя удаляемого файла
                file_name = self.file_init_name('', file, curdir)
                # указывает путь у файлу
                file_name_path = Path(file_name)
                # удаляем файл
                file_name_path.unlink()
                # return
                return True
        except (FileNotFoundError, OSError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # удаление пустой директории с носителя
    def file_delete_empty_folder(self, dir: str, curdir: str = __file__) -> bool:
        '''
        file_delete_empty_folder(dir: str, curdir: str = __file__) -> bool\n                      
                удаление пустой директории с носителя\n             
                возвращаемое значение - bool (True - удалено, False - ошибка)\n    
        параметры:\n                                                
                dir: str - имя пустой директории которое\n   
                    неоходимо удалить с носителя\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примеры:\n    
                file = File()\n 
                file.file_delete_empty_folder('./temp/test1/', __file__)\n                         
                file.file_delete_empty_folder('./temp/test2/', __file__)\n                         
                file.file_delete_empty_folder('./temp/test3/', __file__)\n                         
        '''
        try:
            # определить имя удаляемой пустой директории
            dir_name = self.file_init_dir(dir, '', curdir)
            # delete folder
            rmdir(dir_name)
            return True
        except (OSError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # удаление непустой директории с носителя
    # также удаляет пустую директорию
    def file_delete_full_folder(self, dir: str, curdir: str = __file__) -> bool:
        '''
        file_delete_full_folder(dir: str, curdir: str = __file__) -> bool\n                      
                удаление непустой директории с носителя\n  
                    (также удаляет пустую директорию)\n            
                возвращаемое значение - bool (True - удалено, False - ошибка)\n    
        параметры:\n                                                
                dir: str - имя непустой директории которое\n   
                    неоходимо удалить с носителя\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примеры:\n    
                file = File()\n 
                file.file_delete_full_folder('./temp/test1/', __file__)\n                         
                file.file_delete_full_folder('./temp/test2/', __file__)\n                                               
        '''
        try:
            # определить имя удаляемой директории
            dir_name = self.file_init_dir(dir, '', curdir)
            # delete folder
            shutil.rmtree(dir_name)
            return True
        except (Exception) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # проверка существование файла
    def file_exists(self, file: str, curdir: str = __file__) -> bool:
        '''
        file_exists(file: str, curdir: str = __file__) -> bool\n                      
                проверяет существование файла\n          
                возвращаемое значение - bool (True - существует, False - ошибка)\n    
        параметры:\n                                                
                file: str - имя файла для проверки\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примеры:\n 
                file = File()\n 
                file.file_exists('./temp/test2.txt', __file__)\n 
                file.file_exists('./temp/test3.txt', __file__)\n                     
        '''
        try:
            # определить имя файла
            file_name = self.file_init_name('', file, curdir)
            # проверка существования файла
            if exists(file_name):
                return True
            else:
                return False
        except (Exception) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # проверка существования директории
    def file_exists_dir(self, dir: str, curdir: str = __file__) -> bool:
        '''
        file_exists_dir(dir: str, curdir: str = __file__) -> bool\n                      
                проверяет существование директории \n          
                возвращаемое значение - bool (True - существует, False - ошибка)\n    
        параметры:\n                                                
                dir: str - имя директории для проверки\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примеры:\n 
                file = File()\n 
                file.file_exists_dir('./temp/test2/', __file__)\n 
                file.file_exists_dir('./temp/test3/', __file__)\n                      
        '''
        try:
            # определить имя директории
            dir_name = self.file_init_dir(dir, '', curdir)
            # проверка существования директории
            # if exists(dir_name):
            if self.file_exists(dir_name):
                return True
            else:
                return False
        except (Exception) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # инициализация полной директории
    def file_init_dir(self, folder: str, dir: str, curdir: str = __file__) -> str:
        '''
        file_init_dir(folder: str, dir: str, curdir: str = __file__) -> str\n   
                инициализация полной директории\n                                       
                возвращаемое значение - str (строка)\n                
        параметры:\n                                                
                folder: str - создать директорию в текущей директории\n    
                dir: str - создать директорию в директории folder\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n
        примечание:\n
                вызов метода с пустыми параметрами folder='' и dir=''\n
                    инициализирует текущую директорию\n
                данный метод не используйте с методами данного класса\n
                    т.к. он в других методах вызывается по умолчанию\n
        примеры:\n
                file = File()\n
                dir1 = file.file_init_dir('./temp/', './test/', __file__)\n
                dir2 = file.file_init_dir('./temp/', '', __file__)\n
                dir3 = file.file_init_dir('', './test/', __file__)\n
                dir4 = file.file_init_dir('', '', __file__) # текущая директория\n
        '''
        try:
            # определяем текущую директорию, гбе будет храниться файл
            CURRENT_DIR = dirname(curdir)
            # задаем имя папки (директории)
            FOLDER = folder
            # задаем имя директории в директории folder
            DIR = dir
            # объединяем текущую директорию и созданные директории
            FILE_DIR = str(Path(join(CURRENT_DIR, FOLDER + DIR)))
            # возвращаеи полное имя соданной директории
            try:
                # создаем свое исключение
                class file_init_dir_ERROR(BaseException):
                    pass
                # if android
                if hasattr(sys, 'getandroidapilevel'):
                    return FILE_DIR + '/'
                # if linux and freebsd and macosx
                elif (sys.platform.startswith("linux") or 
                        sys.platform.startswith("linux2") or
                        sys.platform.startswith("freebsd") or
                        sys.platform == "darwin"):
                    return FILE_DIR + '/'
                # if windows
                elif sys.platform in ("win", "win32", "win64", "cygwin"):
                    return FILE_DIR + '\\'
                # if unknown
                else:
                    try:
                        raise file_init_dir_ERROR
                    except (file_init_dir_ERROR) as e:
                        return (str(e) + ' OS is unknown')
            except (BaseException) as e:
                return str(e)
        except (BaseException) as e:
            return str(e)        
    # ---------------------------------------------------------------------------
    # инициализация полного имени файла (директория + имя файла)
    def file_init_name(self, folder: str, filename: str, curdir: str = __file__) -> str:
        '''
        file_init_name(folder: str, filename: str, curdir: str = __file__) -> str\n   
                инициализация полного имени файла\n                   
                    (директория + имя файла)\n                        
                возвращаемое значение - str (строка)\n                
        параметры:\n                                                
                folder: str - создать директорию в текущей директории\n    
                filename: str - создать файл в директории folder\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n  
        примечание:\n
                данный метод не используйте с методами данного класса\n
                    т.к. он в других методах вызывается по умолчанию\n
        примеры:\n
                file = File()\n
                dir1 = file.file_init_name('', './test.txt', __file__)\n
                dir2 = (file.file_init_name('./temp/', './test.txt', __file__)\n
                dir3 = (file.file_init_name('./temp/test/', './test.txt', __file__)\n
                dir4 = (file.file_init_name('', '', __file__) # произойдет исключение\n
        '''
        try:
            # определяем текущую директорию, гбе будет храниться файл
            CURRENT_DIR = dirname(curdir)
            # задаем имя папки (директории)
            FOLDER = folder
            # задаем имя файла для чтения/записи данных
            FILENAME = filename
            # объединяем текущую директорию и файл
            FILE_PATH = str(Path(join(CURRENT_DIR, FOLDER + FILENAME)))
            # определяем тип FILE_PATH
            # print('FILE_PATH :', type(FILE_PATH))
            # возвращаеи полное имя файла (директория + имя файла)
            if filename is None or '' == filename:
                raise BaseException('file name not specified (не указано имя файла)')
            else:
                return FILE_PATH
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # получить все файлы и папки в текущей директории
    def file_get_current_dir_files(self) -> list[str]:
        '''
        file_get_current_dir_files() -> list[str]\n              
                получает все файлы и папки в текущей директории\n             
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                            
                нет параметров\n 
        примеры:\n 
                file = File()\n 
                arr = file.file_get_current_dir_files()\n                                       
        '''
        try:
            files_arr = listdir()
            return files_arr
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # получить все файлы и папки в указанной директории
    def file_get_dir_files(self, dir: str, curdir: str = __file__) -> list[str]:
        '''
        file_get_dir_files(dir: str, curdir: str = __file__) -> list[str]\n               
                получает все файлы и папки в указанной директории\n           
                возвращаемое значение - list[str] (список строк)\n                
        параметры:\n                                                
                dir: str - имя директории которую необходимо показать\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n   
        примеры:\n 
                file = File()\n 
                arr = file.file_get_dir_files('./temp/', __file__)\n                
                arr = file.file_get_dir_files('', __file__)\n                
        '''
        try:
            # определить имя директории
            dir_name = self.file_init_dir(dir, '', curdir)
            # получить все файлы и папки в указанной директории
            files_arr = listdir(dir_name)
            return files_arr
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # получить все установленные права доступа файлов в текущей директории
    # в виде str (rwx)
    def file_get_current_access_dir_in_str(self) -> list[str]:
        '''
        file_get_current_access_dir_in_str() -> list[str]\n                       
                получает все установленные права доступа файлов\n 
                    в текущей директории в виде str (rwx)\n 
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                              
                нет параметров\n
        примеры:\n 
                file = File()\n 
                arr = file.file_get_current_access_dir_in_str()\n                         
        '''
        try:
            # массив установленных разрешений для файлов и папок
            access_arr = list()
            # заполняем массив установленныз разрешений для файлов и папок
            for file in self.file_get_current_dir_files():
                # Определим установленные разрешения в виде букв -rwx
                access_arr.append(stat.filemode(os.stat(file).st_mode))
            # return
            return access_arr
        except(BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # получить все установленные права доступа файлов в текущей директории
    # в виде int (777)
    def file_get_current_access_dir_in_int(self) -> list[int]:
        '''
        file_get_current_access_dir_in_int() -> list[int]\n                       
                получает все установленные права доступа файлов\n 
                    в текущей директории в виде int (777)\n 
                возвращаемое значение - list[int] (список чисел)\n    
        параметры:\n                                              
                нет параметров\n
        примеры:\n 
                file = File()\n 
                arr = file.file_get_current_access_dir_in_int()\n                         
        '''
        try:
            # массив установленных разрешений для файлов и папок
            access_arr = list()
            # заполняем массив установленныз разрешений для файлов и папок
            for file in self.file_get_current_dir_files():
                # Определим установленные разрешения в виде чисел - int (777)
                access_arr.append(stat.S_IMODE(os.stat(file).st_mode))
            # return
            return access_arr
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # получить установщик данного файла
    def file_get_installer(self) -> str:
        '''
        file_get_installer() -> str\n                       
                получает установщик данного файла\n 
                возвращаемое значение - str (строка)\n 
        возвращаемое значение для android\n 
                com.google.android.packageinstaller - установка с телефона\n 
                com.android.vending - установка с 'google play market'\n 
                com.amazon.venezia - установка с amazon.com\n 
        возвращаемое значение для остальных ОС\n 
                unknown - источник установки неизвестен\n 
        параметры:\n                                              
                нет параметров\n
        примеры:\n 
                file = File()\n 
                installer = file.file_get_installer()\n                        
        '''
        try:
            # создаем свое исключение
            class file_get_installer_ERROR(BaseException):
                pass
            # if android
            if hasattr(sys, 'getandroidapilevel'):
                # получить установщик данного файла
                from jnius import autoclass, JavaException
                try:
                    Context = autoclass('android.content.Context')
                    # получить установщик данного файла
                    return str(
                        Context.getPackageManager().getInstallerPackageName(
                            str(Context.getPackageName())
                            )
                        )
                except (BaseException) as e:
                    return ('BaseException: ' + str(e))
                except (JavaException) as e:
                    return ('JavaException: ' + str(e))
            # if linux and freebsd and macosx
            elif (sys.platform.startswith("linux") or 
                    sys.platform.startswith("linux2") or
                    sys.platform.startswith("freebsd") or
                    sys.platform == "darwin"):
                return 'unknown'
            # if windows
            elif sys.platform in ("win", "win32", "win64", "cygwin"):
                return 'unknown'
            # if unknown
            else:
                try:
                    raise file_get_installer_ERROR
                except (file_get_installer_ERROR) as e:
                    return (str(e) + ' OS is unknown')
                # return 'unknown'
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # получить директорию к папке Downloads
    def file_get_path_to_downloads(self) -> str:
        '''
        file_get_path_to_downloads() -> str\n                       
                получает директорию к папке Downloads\n 
                возвращаемое значение - str (строка)\n   
        параметры:\n                                              
                нет параметров\n
        примеры:\n 
                file = File()\n 
                path = file.file_get_path_to_downloads()\n                        
        '''
        try:
            # создаем свое исключение
            class file_get_path_to_downloads_ERROR(BaseException):
                pass
            # if android
            if hasattr(sys, 'getandroidapilevel'):
                # получить Download путь к каталогу в Android
                from android.storage import primary_external_storage_path
                dir = primary_external_storage_path()
                # downloads_path = os.path.join(dir, './Download/')
                downloads_path = str(Path(join(dir, './Download/'))) + '/'
                return downloads_path
            # if linux and freebsd and macosx
            elif (sys.platform.startswith("linux") or 
                    sys.platform.startswith("linux2") or
                    sys.platform.startswith("freebsd") or
                    sys.platform == "darwin"):
                # downloads_path = str(Path.home()/"Downloads")
                # downloads_path = str(os.path.join(Path.home(), "Downloads"))
                downloads_path = None
                if ('ru' == self.file_get_local_language()):
                    downloads_path = str(Path(join(Path.home(), "./Загрузки/"))) + '/'
                else:
                    downloads_path = str(Path(join(Path.home(), "./Downloads/"))) + '/'
                return downloads_path
            # if windows
            elif sys.platform in ("win", "win32", "win64", "cygwin"):
                # работа с реестром windows
                import winreg
                sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
                downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
                downloads_path_win = None
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                    downloads_path_win = winreg.QueryValueEx(key, downloads_guid)[0]
                downloads_path = str(Path(downloads_path_win)) + '\\'
                return downloads_path
            # if unknown
            else:
                try:
                    raise file_get_path_to_downloads_ERROR
                except (file_get_path_to_downloads_ERROR) as e:
                    return (str(e) + ' OS is unknown')
                # return 'unknown'
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # получить установленный по умолчанию язык операционной системы
    def file_get_local_language(self) -> str:
        '''
        file_get_local_language() -> str\n                       
                получает установленный по умолчанию язык операционной системы\n 
                возвращаемое значение - str (строка)\n   
        параметры:\n                                              
                нет параметров\n
        примеры:\n 
                file = File()\n 
                lang = file.file_get_local_language()\n                          
        '''
        try:
            # создаем свое исключение
            class file_get_local_language_ERROR(BaseException):
                pass
            # if android
            if hasattr(sys, 'getandroidapilevel'):
                # Получение языка установленного в системе
                from jnius import autoclass
                language = autoclass("java.util.Locale").getDefault().getDisplayLanguage()
                return language
            # if linux and freebsd and macosx
            elif (sys.platform.startswith("linux") or 
                    sys.platform.startswith("linux2") or
                    sys.platform.startswith("freebsd") or
                    sys.platform == "darwin"):
                language = locale.getdefaultlocale()[0].split('_')[0]
                return language
            # if windows
            elif sys.platform in ("win", "win32", "win64", "cygwin"):
                import ctypes
                windll = ctypes.windll.kernel32
                windll.GetUserDefaultUILanguage()
                language = locale.windows_locale[windll.GetUserDefaultUILanguage()].split('_')[0]
                return language
            # if unknown
            else:
                try:
                    raise file_get_local_language_ERROR
                except (file_get_local_language_ERROR) as e:
                    return (str(e) + ' OS is unknown')
                # return 'unknown'
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # разрешить весь доступ к указанному файлу/директории
    # работает только с файлофой системой unix (ext и т.д.)
    def file_set_access_open_all(self, name: str, curdir: str = __file__) -> bool:
        '''
        file_set_access_open_all(name: str, curdir: str = __file__) -> bool\n                      
                разрешает весь доступ к указанному файлу/директории\n             
                возвращаемое значение - bool (True - доступ разрешен, False - ошибка)\n    
        параметры:\n                                                
                name: str - имя папки/директории к которому нужно разрешить доступ\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n   
        примеры:\n 
                file = File()\n 
                file.file_set_access_open_all('./temp/test2.txt', __file__)\n 
                file.file_set_access_open_all('./temp/test2/', __file__)\n                       
        '''
        try:
            # определить имя файла/директории
            dir_file_name = self.file_init_name('', name, curdir)
            # определяем текущие права файла
            # permissions = os.stat(dir_file_name).st_mode
            # Convert a file's mode to a string of the form '-rwxrwxrwx'
            # permissions = stat.filemode(permissions)
            # задаем новые права доступа к файлу (разрешаем доступ)
            new_permissions = stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO
            chmod(dir_file_name, new_permissions)
            return True
        except (PermissionError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # запретить весь доступ к указанному файлу/директории
    # работает только с файлофой системой unix (ext и т.д.)
    def file_set_access_close_all(self, name: str, curdir: str = __file__) -> bool:
        '''
        file_set_access_close_all(name: str, curdir: str = __file__) -> bool\n                      
                запрещает весь доступ к указанному файлу/директории\n             
                возвращаемое значение - bool (True - доступ запрещен, False - ошибка)\n    
        параметры:\n                                                
                name: str - имя папки/директории к которому нужно запретить доступ\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n   
        примеры:\n 
                file = File()\n 
                file.file_set_access_close_all('./temp/test1.txt', __file__)\n 
                file.file_set_access_close_all('./temp/test2.txt', __file__)\n 
                file.file_set_access_close_all('./temp/test1/', __file__)\n 
                file.file_set_access_close_all('./temp/test2/', __file__)\n                         
        '''
        try:
            # определить имя файла/директории
            dir_file_name = self.file_init_name('', name, curdir)
            # определяем текущие права файла
            # permissions = os.stat(dir_file_name).st_mode
            # Convert a file's mode to a string of the form '-rwxrwxrwx'
            # permissions = stat.filemode(permissions)
            # задаем новые права доступа к файлу (запрещаем доступ)
            new_permissions = stat.S_ENFMT
            chmod(dir_file_name, new_permissions)
            return True
        except (PermissionError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # чтение содержимого файла построчно
    def file_read(self, file: str, curdir: str = __file__) -> list[str]:
        '''
        file_read(file: str, curdir: str = __file__) -> list[str]\n                         
                читает информацию из файла построчно\n                
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    и прочитать\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n   
        примеры:\n 
                file = File()\n 
                arr = file.file_read('./temp/dict.txt', __file__)\n                           
        '''
        try:
            # определить имя файла
            file_name = self.file_init_name('', file, curdir)
            # открыть файл и прочитать построчно
            with open(file_name, 'r') as f:
                return f.readlines()
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # чтение содержимого файла содержащий текст в utf-8 кодировке
    def file_read_utf8(self, file: str, curdir: str = __file__) -> list[str]:
        '''
        file_read_utf8(file: str, curdir: str = __file__) -> list[str]\n                    
                читает информацию из файла в utf-8 кодировке\n        
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    и прочитать\n 
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n   
        примеры:\n 
                file = File()\n 
                arr = file.file_read_utf8('./temp/dict.txt', __file__)\n                           
        '''
        try:
            # определить имя файла
            file_name = self.file_init_name('', file, curdir)
            # var
            str_byte = None
            # открыть файл и прочитать текст в utf-8 кодировке
            with open(file_name, 'r', encoding='utf-8') as f:
                # shutil.copyfileobj(f, str_byte.extend)
                str_byte = f.read().encode('utf-8')
            # print(repr(str(str_byte, 'utf-8')))
            return str(str_byte, 'utf-8').split('\n')
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # запись содержимого списка (list) в файл
    def file_write(self, file: str, arr: list, curdir: str = __file__) -> None:
        '''
        file_write(file: str, arr: list, curdir: str = __file__) -> None\n                  
                запись содержимого списка (list) в файл\n             
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    для записи содержимого списка\n           
                arr: list - список для записи в файл\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n   
        примеры:\n 
                file = File()\n 
                file.file_write('./temp/write.txt', ['test', 'rom', 'max'], __file__)\n                
        '''
        try:
            # определить имя файла
            file_name = self.file_init_name('', file, curdir)
            # в списке к концу строк добавляем \n (переход на новую строку)
            for i in range(len(arr)):
                arr[i] += '\n'
            # создаем файл и записываем содержимое списка
            with open(file_name, 'w') as f:
                f.writelines(arr)
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # дозапись содержимого списка (list) в файл
    def file_write_append(self, file: str, arr: list, curdir: str = __file__) -> None:
        '''
        file_write_append(file: str, arr: list, curdir: str = __file__) -> None\n                  
                дозапись содержимого списка (list) в файл\n             
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    для дозаписи содержимого списка\n           
                arr: list - список для дозаписи в файл\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n   
        примеры:\n 
                file = File()\n 
                file.file_write_append('./temp/write.txt', ['1', '2', '3'], __file__)\n  
                file.file_write_append('./temp/write.txt', [4, 5, 6], __file__) # error\n               
        '''
        try:
            # определить имя файла
            file_name = self.file_init_name('', file, curdir)
            # в списке к концу строк добавляем \n (переход на новую строку)
            for i in range(len(arr)):
                arr[i] += '\n'
            # открываем файл и дозаписываем содержимое списка
            with open(file_name, 'a') as f:
                f.writelines(arr)
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # запись содержимого словаря (dict) в файл
    def file_write_dict(self, file: str, dictor: dict, curdir: str = __file__) -> None:
        '''
        file_write_dict(file: str, dictor: dict, curdir: str = __file__) -> None\n          
                запись содержимого словаря (dict) в файл\n            
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    для записи содержимого словаря\n          
                dictor: dict - словарь для записи в файл\n
                curdir: str = __file__ - параметр по умолчанию,\n
                    который нужно передавать явно если данный класс вложен (nested),\n
                    __file__ - путь данного файла в текущей директории (magic method)\n    
        примеры:\n 
                file = File()\n 
                file.file_write_dict('./temp/dict.txt', dict(max='ramanenka', lara='croft'), __file__)\n          
        '''
        try:
            # определить имя файла
            file_name = self.file_init_name('', file, curdir)
            # создать файл и записать содержимое словаря (хэш таблицы)
            with open(file_name, 'w') as f:
                for k,v in dictor.items():
                    f.write(f'{k} {v}\n')
        except (BaseException) as e:
            return str(e)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тест
# если не модуль, то выполнить
if __name__ == '__main__':
    # функция для тестов
    def main():
        # ---------------------------------------------------------------------------
        # создаем объект file
        file = File()
        # ---------------------------------------------------------------------------
        # инициализация полной директории
        print('******************инициализация полной директории******************')
        print('++++++++++(file_init_dir(folder: str, dir: str, curdir: str = __file__) -> str) -> str)++++++++++')
        print(file.file_init_dir('./temp/', './test/', __file__))
        print(file.file_init_dir('./temp/', '', __file__))
        print(file.file_init_dir('', './test/', __file__))
        print(file.file_init_dir('', '', __file__))
        # ---------------------------------------------------------------------------
        # инициализация полного имени файла (директория + имя файла)
        print('******************инициализация полного имени файла (директория + имя файла)******************')
        print('++++++++++(file_init_name(folder: str, filename: str, curdir: str = __file__) -> str)++++++++++')
        print(file.file_init_name('', './test.txt', __file__))
        print(file.file_init_name('./temp/', './test.txt', __file__))
        print(file.file_init_name('./temp/test/', './test.txt', __file__))
        print(file.file_init_name('', '', __file__))
        # ---------------------------------------------------------------------------
        # создать указанную директорию
        print('******************создать указанную директорию******************')
        print('++++++++++(file_create_dir(dir: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_create_dir('./temp/', __file__))
        print(file.file_create_dir('./temp/test1/', __file__))
        print(file.file_create_dir('./temp/test2/', __file__))
        print(file.file_create_dir('./temp/test2/test3/', __file__))
        # ---------------------------------------------------------------------------
        # создать пустой файл
        print('******************создать пустой файл******************')
        print('++++++++++(file_create(file: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_create('./temp/test1.txt', __file__))
        print(file.file_create('./temp/test2.txt', __file__))
        print(file.file_create('./temp/max/test2.txt', __file__))
        # ---------------------------------------------------------------------------
        # запись содержимого списка (list) в файл
        print('******************запись содержимого списка (list) в файл******************')
        print('++++++++++(file_write(file: str, arr: list, curdir: str = __file__) -> None)++++++++++')
        print(file.file_write('./temp/write.txt', ['test', 'rom', 'max'], __file__))
        # ---------------------------------------------------------------------------
        # дозапись содержимого списка (list) в файл
        print('******************дозапись содержимого списка (list) в файл******************')
        print('++++++++++(file_write_append(file: str, arr: list, curdir: str = __file__) -> None)++++++++++')
        print(file.file_write_append('./temp/write.txt', ['1', '2', '3'], __file__))
        print(file.file_write_append('./temp/write.txt', ['4', '5', '6'], __file__))
        # ---------------------------------------------------------------------------
        # запись содержимого словаря (dict) в файл
        print('******************запись содержимого словаря (dict) в файл******************')
        print('++++++++++(file_write_dict(file: str, dictor: dict, curdir: str = __file__) -> None)++++++++++')
        print(file.file_write_dict('./temp/dict.txt', dict(max='ramanenka', lara='croft'), __file__))
        # ---------------------------------------------------------------------------
        # вывод в консоль содержимого списка (list)
        print('******************вывод в консоль содержимого списка (list)******************')
        print('++++++++++(file_console_print_list(arr: list) -> None)++++++++++')
        file.file_console_print_list([1, 2, 3])
        # ---------------------------------------------------------------------------
        # вывод в консоль содержимого файла содержащий текст в utf-8 кодировке 
        print('******************вывод в консоль содержимого файла содержащий текст в utf-8 кодировке******************')
        print('++++++++++(file_console_print_file_utf8(file: str, curdir: str = __file__) -> None)++++++++++')
        file.file_console_print_file_utf8('./temp/dict.txt', __file__)
        # ---------------------------------------------------------------------------
        # чтение содержимого файла построчно
        print('******************чтение содержимого файла построчно******************')
        print('++++++++++(file_read(file: str, curdir: str = __file__) -> list[str])++++++++++')
        print(file.file_read('./temp/dict.txt', __file__))
        # ---------------------------------------------------------------------------
        # чтение содержимого файла содержащий текст в utf-8 кодировке
        print('******************чтение содержимого файла содержащий текст в utf-8 кодировке******************')
        print('++++++++++(file_read_utf8(file: str, curdir: str = __file__) -> list[str])++++++++++')
        print(file.file_read_utf8('./temp/dict.txt', __file__))
        # ---------------------------------------------------------------------------
        # запретить весь доступ к указанному файлу/директории
        print('******************запретить весь доступ к указанному файлу/директории******************')
        print('++++++++++(file_set_access_close_all(name: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_set_access_close_all('./temp/test1.txt', __file__))
        print(file.file_set_access_close_all('./temp/test2.txt', __file__))
        print(file.file_set_access_close_all('./temp/test1/', __file__))
        print(file.file_set_access_close_all('./temp/test2/', __file__))
        # ---------------------------------------------------------------------------
        # разрешить весь доступ к указанному файлу/директории
        print('******************разрешить весь доступ к указанному файлу/директории******************')
        print('++++++++++(file_set_access_open_all(name: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_set_access_open_all('./temp/test2.txt', __file__))
        print(file.file_set_access_open_all('./temp/test2/', __file__))
        # ---------------------------------------------------------------------------
        # получить установленный по умолчанию язык операционной системы
        print('******************получить установленный по умолчанию язык операционной системы******************')
        print('++++++++++(file_get_local_language() -> str)++++++++++')
        print(file.file_get_local_language())
        # ---------------------------------------------------------------------------
        # получить директорию к папке Downloads
        print('******************получить директорию к папке Downloads******************')
        print('++++++++++(file_get_path_to_downloads() -> str)++++++++++')
        print(file.file_get_path_to_downloads())
        # ---------------------------------------------------------------------------
        # получить установщик данного файла
        print('******************получить установщик данного файла******************')
        print('++++++++++(file_get_installer() -> str)++++++++++')
        print(file.file_get_installer())
        # ---------------------------------------------------------------------------
        # получить все установленные права доступа файлов в текущей директории в виде int (777)
        print('******************получить все установленные права доступа файлов в текущей директории в виде int (777)******************')
        print('++++++++++(file_get_current_access_dir_in_int() -> list[int])++++++++++')
        print(file.file_get_current_access_dir_in_int())
        # ---------------------------------------------------------------------------
        # получить все установленные права доступа файлов в текущей директории в виде str (rwx)
        print('******************получить все установленные права доступа файлов в текущей директории в виде str (rwx)******************')
        print('++++++++++(file_get_current_access_dir_in_str() -> list[str])++++++++++')
        print(file.file_get_current_access_dir_in_str())
        # ---------------------------------------------------------------------------
        # получить все файлы и папки в указанной директории
        print('******************получить все файлы и папки в указанной директории******************')
        print('++++++++++(file_get_dir_files(dir: str, curdir: str = __file__) -> list[str])++++++++++')
        print(file.file_get_dir_files('./temp/', __file__))
        print(file.file_get_dir_files('', __file__))
        # ---------------------------------------------------------------------------
        # получить все файлы и папки в текущей директории
        print('******************получить все файлы и папки в текущей директории******************')
        print('++++++++++(file_get_current_dir_files() -> list[str])++++++++++')
        print(file.file_get_current_dir_files())
        # ---------------------------------------------------------------------------
        # проверка существования директории
        print('******************проверка существования директории******************')
        print('++++++++++(file_exists_dir(dir: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_exists_dir('./temp/test2/', __file__))
        print(file.file_exists_dir('./temp/test3/', __file__))
        # ---------------------------------------------------------------------------
        # проверка существование файла
        print('******************проверка существование файла******************')
        print('++++++++++(file_exists(file: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_exists('./temp/test2.txt', __file__))
        print(file.file_exists('./temp/test3.txt', __file__))
        # ---------------------------------------------------------------------------
        # удаление файла с носителя
        print('******************удаление файла с носителя******************')
        print('++++++++++(file_delete(file: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_delete('./temp/write.txt', __file__))
        print(file.file_delete('./temp/write2.txt', __file__))
        # ---------------------------------------------------------------------------
        # удаление пустой директории с носителя
        print('******************удаление пустой директории с носителя******************')
        print('++++++++++(file_delete_empty_folder(dir: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_delete_empty_folder('./temp/test1/', __file__))
        print(file.file_delete_empty_folder('./temp/test2/', __file__))
        print(file.file_delete_empty_folder('./temp/test3/', __file__))
        # ---------------------------------------------------------------------------
        # удаление непустой директории с носителя
        print('******************удаление непустой директории с носителя******************')
        print('++++++++++(file_delete_full_folder(dir: str, curdir: str = __file__) -> bool)++++++++++')
        print(file.file_delete_full_folder('./temp/test1/', __file__))
        print(file.file_delete_full_folder('./temp/test2/', __file__))
        # ---------------------------------------------------------------------------
    # выполнить тест
    main()
# *****************************************************************************************