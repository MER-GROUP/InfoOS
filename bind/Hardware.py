# *****************************************************************************************
# platform - определение операционки
from kivy.utils import platform
# *****************************************************************************************
# если ОС Android, то загрузить следующие модули
if 'android' == platform:
    # ---------------------------------------------------------------------------
    # autoclass - импорт java классов
    # JavaException - работа с исключениями java классов
    from jnius import autoclass, JavaException
    Context = autoclass('android.content.Context')
    PackageManager = autoclass('android.content.pm.PackageManager')
    ApplicationInfo = autoclass('android.content.pm.ApplicationInfo')
    # ---------------------------------------------------------------------------
    # plyer - работа с железом устройства
    # vibrator - управление вибрацией устройства
    from plyer import vibrator
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# Hardware - манипуляции (действия) с железом устройства
class Hardware:
    # ---------------------------------------------------------------------------
    # вибрация устройство на ОС - Android
    def vibrator_android(self, n):
        if 'android' == platform:
            try:
                vibrator.vibrate(n)
            except JavaException as e:
                pass
            except BaseException as e:
                pass
        else:
            pass
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    pass
# *****************************************************************************************