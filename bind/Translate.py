# *****************************************************************************************
# Translate - автоматическая локализация программы на родной язык
class Translate:
    # ---------------------------------------------------------------------------
    # словарь руского и английского языка
    translate = {
        'about': [
            '[b][color=#2F4F4F]РАЗРАБОТЧИК И АВТОР:[/color][/b]\n' +
                    '[color=#808080]Максим Романенко (Red Alert)[/color]\n' +
                '[b][color=#2F4F4F]ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ:[/color][/b]\n' +
                    '[color=#808080]свободное и распространяется\n' +
                    'по лицензии MIT[/color]\n' +
                '[b][color=#2F4F4F]ИНСТРУМЕНТЫ РАЗРАБОТКИ:[/color][/b]\n' +
                    '[color=#808080]python (python.org), kivy (kivy.org),\n' +
                    'json (json.org), debian (debian.org),\n' +
                    'vscode (code.visualstudio.com),\n' +
                    'git (git-scm.com)[/color]\n' +
                '[b][color=#2F4F4F]КОД ПРОГРАММЫ:[/color][/b]\n' +
                    '[color=#808080]github.com/mer-group/infoos[/color]\n' +
                '[b][color=#2F4F4F]КОНТАКТЫ:[/color][/b]\n' +
                    '[color=#808080]i@mer-group.ru\n' +
                    'github.com/mer-group[/color]',

            '[b][color=#2F4F4F]DEVELOPER AND AUTHOR:[/color][/b]\n' +
                    '[color=#808080]Maxim Ramanenka (Red Alert)[/color]\n' +
                '[b][color=#2F4F4F]SOFTWARE:[/color][/b]\n' +
                    '[color=#808080]free and distributed\n' +
                    'under the MIT license[/color]\n' +
                '[b][color=#2F4F4F]DEVELOPMENT TOOLS:[/color][/b]\n' +
                    '[color=#808080]python (python.org), kivy (kivy.org),\n' +
                    'json (json.org), debian (debian.org),\n' +
                    'vscode (code.visualstudio.com),\n' +
                    'git (git-scm.com)[/color]\n' +
                '[b][color=#2F4F4F]PROGRAM CODE:[/color][/b]\n' +
                    '[color=#808080]github.com/mer-group/infoos[/color]\n' +
                '[b][color=#2F4F4F]CONTACTS:[/color][/b]\n' +
                    '[color=#808080]i@mer-group.ru\n' +
                    'github.com/mer-group[/color]'
        ],
        'intro': [
            'Данная программа предназначена для получения информации об аппаратном обеспечении и операционной системе устройства.',
            'This program is designed to obtain information about the hardware and operating system of the device.'
        ],
        'info': [
            'ИНФО',
            'INFO'
        ],
        'info_install_name': [
            'Имя установщика',
            'Installer name'
        ],
        'close': [
            'ЗАКРЫТЬ',
            'CLOSE'
        ],
        'history': [
            'ИСТОРИЯ',
            'HISTORY'
        ],
        'clear': [
            'ОЧИСТИТЬ ИСТОРИЮ',
            'CLEAR HISTORY'
        ],
        'vibro': [
            'ВИБРАЦИОННЫЙ ОТКЛИК',
            'VIBRATION RESPONSE'
        ],
        'length': [
            'ДЛИНА ИСТОРИИ',
            'HISTORY LENGTH'
        ],
        'round': [
            'ОКРУГЛЕНИЕ ЧИСЕЛ',
            'ROUNDING NUMBERS'
        ],
        'menu': [
            'МЕНЮ',
            'MENU'
        ],
        'name_pkg': [
            'Имя пакета приложения',
            'App package name'
        ],
        'settings': [
            'НАСТРОЙКИ',
            'SETTINGS'
        ],
        'sdk': [
            'Версия SDK',
            'SDK version'
        ]
    }
    # ---------------------------------------------------------------------------
    # переводит строку в английский или русский язык
    def get_translate(self, lang: str, name: str) -> str:
        try:
            if (lang.lower() in 'russianрусский'):
                return self.translate[name][0]
            else:
                return self.translate[name][1]
        except (KeyError):
            return 'KeyError'
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    print('+++++get_translate+++++')
    print(Translate().get_translate('en', 'info'))
    print(Translate().get_translate('en', 'error'))
# *****************************************************************************************