# *****************************************************************************************
# platform - определение операционки
from kivy.utils import platform
# *****************************************************************************************
# если ОС Android, то загрузить следующие модули
if 'android' == platform:
    # ---------------------------------------------------------------------------
    # autoclass - импорт java классов
    # JavaException - работа с исключениями java классов
    from jnius import autoclass, cast, JavaException
    # ---------------------------------------------------------------------------
    #
    #
    #
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    # ---------------------------------------------------------------------------
    #
    #
    #
    Activity = cast('android.app.Activity', PythonActivity.mActivity) 
    # ---------------------------------------------------------------------------
    # информация о приложении (программе)
    # (public abstract class Context extends Object)
    # https://developer.android.com/reference/android/content/Context
    # Context = autoclass('android.content.Context')
    Context = cast('android.content.Context', Activity.getApplicationContext())
    # ---------------------------------------------------------------------------
    # дополнительная информация о приложении (программе)
    # (public abstract class PackageManager extends Object)
    # https://developer.android.com/reference/android/content/pm/PackageManager
    PackageManager = autoclass('android.content.pm.PackageManager')
    # ---------------------------------------------------------------------------
    # информация о том, как было установлено приложение
    # (public final class InstallSourceInfo extends Object implements Parcelable)
    # https://developer.android.com/reference/android/content/pm/InstallSourceInfo
    # This class added in API level 30.
    # Этот класс введен в API level 30.
    # InstallSourceInfo = autoclass('android.content.pm.InstallSourceInfo')
    # ---------------------------------------------------------------------------
    #
    #
    #
    ApplicationInfo = autoclass('android.content.pm.ApplicationInfo')
    # ---------------------------------------------------------------------------
    # информация об ОС Android
    # (public static class Build.VERSION extends Object)
    # https://developer.android.com/reference/android/os/Build.VERSION
    VERSION = autoclass('android.os.Build$VERSION')
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
    # SDK_INT:
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
    # getPackageName():
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
                return 'EXCEPT JAVA: ' + str(e)
            except BaseException as e:
                return 'EXCEPT PYTHON: ' + str(e)
        else:
            # return 'Данный метод не реализован ...'
            return 'This method is not implemented ...'
    # ---------------------------------------------------------------------------
    # Android:
    # getPackageManager():
    #   Return PackageManager instance to find global package information.
    #   Возвращает объект PackageManager, чтобы найти глобальную информацию о пакете.
    #   https://developer.android.com/reference/android/content/Context#getPackageManager()
    #
    # getInstallerPackageName(String packageName):
    #   Retrieve the package name of the application that installed a package. 
    #   This identifies which market the package came from.
    #   Показывает установщик данного приложения.
    #   Это позволяет определить с какого рынка (магазина) установленно данное приложение.
    #   https://developer.android.com/reference/android/content/pm/PackageManager#getInstallerPackageName(java.lang.String)
    #   This method was deprecated in API level 30.
    #   Этот метод устарел на уровне API 30.
    #   Use - getInstallSourceInfo(String packageName) if API 30 and higher.
    #   Используйте - getInstallSourceInfo(String packageName) если API 30 и выше.
    #
    # getInstallSourceInfo(String packageName):
    #   Retrieves information about how a package was installed or updated.
    #   Извлекает информацию о том, как был установлен или обновлен пакет.
    #   This method added in API level 30.
    #   Этот метод введен в API level 30.
    #   https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo(java.lang.String)
    #
    # getInstallingPackageName():
    #   The name of the package responsible for the installation 
    #    (the installer of record), or null if not available.
    #   Имя пакета, ответственного за установку (установщик пакета), 
    #    или null, если он недоступен.
    #   This method added in API level 30.
    #   Этот метод введен в API level 30.
    #   https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInstallingPackageName()
    #
    # getPackageName():
    #   Return the name of this application's package.
    #   Возвращает имя пакета этого приложения.
    #   https://developer.android.com/reference/android/content/Context#getPackageName()
    def package_name_installer_show(self) -> str:
        if 'android' == platform:
            try:
                if (30 > int(self.sdk_show())):
                    return str(
                        Context.getPackageManager().getInstallerPackageName(
                            str(
                                Context.getPackageName()
                            )
                        )
                    )
                else:
                    return str(
                        Context.getPackageManager().getInstallSourceInfo(
                            str(
                                Context.getPackageName()
                            )
                        ).getInstallingPackageName()
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