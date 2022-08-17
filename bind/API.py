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
    # ---------------------------------------------------------------------------
    # информация о приложении (программе)
    # (public abstract class Context extends Object)
    # https://developer.android.com/reference/android/content/Context
    Context = autoclass('android.content.Context')
    # ---------------------------------------------------------------------------
    #
    #
    #
    PackageManager = autoclass('android.content.pm.PackageManager')
    # ---------------------------------------------------------------------------
    #
    #
    #
    ApplicationInfo = autoclass('android.content.pm.ApplicationInfo')
    # ---------------------------------------------------------------------------
    # информация об ОС Android
    # (public static class Build.VERSION extends Object)
    # https://developer.android.com/reference/android/os/Build.VERSION
    VERSION = autoclass('android.os.Build.VERSION')
    # ---------------------------------------------------------------------------
    # plyer - работа с железом устройства
    # vibrator - управление вибрацией устройства
    from plyer import vibrator
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# API - манипуляции (действия) с API опепационных систем
class API:
    # ---------------------------------------------------------------------------
    # Android:
    #   The SDK version of the software currently running on this hardware device.
    #   Версия SDK программного обеспечения, запущенного в настоящее время 
    #    на этом аппаратном устройстве.
    #   https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT
    def sdk_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    VERSION.SDK_INT
                    )
            except JavaException as e:
                return str(e)
            except BaseException as e:
                return str(e)
        else:
            # return 'Данный метод не реализован ...'
            return 'This method is not implemented ...'
    # ---------------------------------------------------------------------------
    # Android:
    #   Return the name of this application's package.
    #   Возвращает имя пакета этого приложения.
    #   https://developer.android.com/reference/android/content/Context#getPackageName()
    def package_name_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    Context.getPackageName()
                    )
            except JavaException as e:
                return str(e)
            except BaseException as e:
                return str(e)
        else:
            # return 'Данный метод не реализован ...'
            return 'This method is not implemented ...'
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    pass
# *****************************************************************************************