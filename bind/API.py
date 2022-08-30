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
    # api_version - определение версии SDK программного обеспечения
    from android import api_version
    # ---------------------------------------------------------------------------
    # получает путь к внутреннему хранилицу в Android
    from android.storage import primary_external_storage_path
    # ---------------------------------------------------------------------------
    # PythonActivity - ссылка на Java Activity, в которой запущено приложение, 
    # она хранится в загрузчике Kivy PythonActivity
    # PythonActivity is provided by the Kivy bootstrap app in python-for-android
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    # ---------------------------------------------------------------------------
    # PythonActivity.mActivity - хранит ссылку на текущее выполняемое действие
    # Нам это нужно для доступа к службам
    # The PythonActivity.mActivity stores a reference to the currently running activity
    # We need this to access services
    # android.app.Activity - взаимоднйствие окна/gui с пользовательским действием
    # (public class Activity extends ContextThemeWrapper implements LayoutInflater.Factory2, 
    # Window.Callback, KeyEvent.Callback, View.OnCreateContextMenuListener, ComponentCallbacks2)
    # https://developer.android.com/reference/android/app/Activity
    Activity = cast('android.app.Activity', PythonActivity.mActivity) 
    # ---------------------------------------------------------------------------
    # Информация о приложении (программе)
    # (public abstract class Context extends Object)
    # https://developer.android.com/reference/android/content/Context
    # Context = autoclass('android.content.Context')
    # Activity.getApplicationContext() - возвращает ссылку на актиыный класс Context
    # Activity.getApplicationContext() - returns a reference to the active Context class
    Context = cast('android.content.Context', Activity.getApplicationContext())
    # ---------------------------------------------------------------------------
    # Дополнительная информация о приложении (программе)
    # (public abstract class PackageManager extends Object)
    # https://developer.android.com/reference/android/content/pm/PackageManager
    PackageManager = autoclass('android.content.pm.PackageManager')
    # ---------------------------------------------------------------------------
    # Информация о том, как было установлено приложение
    # (public final class InstallSourceInfo extends Object implements Parcelable)
    # https://developer.android.com/reference/android/content/pm/InstallSourceInfo
    # This class added in API level 30.
    # Этот класс введен в API level 30.
    if 30 <= api_version: 
        InstallSourceInfo = autoclass('android.content.pm.InstallSourceInfo')
    # ---------------------------------------------------------------------------
    # Информация о конкретном приложении (программе)
    # (public class ApplicationInfo extends PackageItemInfo implements Parcelable)
    # https://developer.android.com/reference/android/content/pm/ApplicationInfo
    ApplicationInfo = autoclass('android.content.pm.ApplicationInfo')
    # ---------------------------------------------------------------------------
    # Информация об ОС Android
    # (public static class Build.VERSION extends Object)
    # https://developer.android.com/reference/android/os/Build.VERSION
    VERSION = autoclass('android.os.Build$VERSION')
    # ---------------------------------------------------------------------------
    # Работа с локализацией ОС Android
    # (public final class Locale extends Object implements Cloneable, Serializable)
    # https://developer.android.com/reference/java/util/Locale
    Locale = autoclass('java.util.Locale')
    # ---------------------------------------------------------------------------
    # Абстрактное представление путей к файлам и каталогам
    # (public class File extends Object implements Serializable, Comparable<File>)
    # https://developer.android.com/reference/java/io/File
    File = autoclass('java.io.File')
    # ---------------------------------------------------------------------------
    # plyer - работа с железом устройства
    # vibrator - управление вибрацией устройства
    # https://github.com/kivy/plyer/blob/master/plyer/facades/vibrator.py
    from plyer import vibrator
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# API - манипуляции (действия) с API опепационных систем
class API:
    # ---------------------------------------------------------------------------
    # Android:
    # getPackageName() -> abstract String:
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
    # getPackageManager() -> abstract PackageManager:
    #   Return PackageManager instance to find global package information.
    #   Возвращает объект PackageManager, чтобы найти глобальную информацию о пакете.
    #   https://developer.android.com/reference/android/content/Context#getPackageManager()
    #
    # getInstallerPackageName(String packageName) -> abstract String:
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
    # getInstallSourceInfo(String packageName) -> InstallSourceInfo:
    #   Retrieves information about how a package was installed or updated.
    #   Извлекает информацию о том, как был установлен или обновлен пакет.
    #   This method added in API level 30.
    #   Этот метод введен в API level 30.
    #   https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo(java.lang.String)
    #
    # getInstallingPackageName() -> String:
    #   The name of the package responsible for the installation 
    #    (the installer of record), or null if not available.
    #   Имя пакета, ответственного за установку (установщик пакета), 
    #    или null, если он недоступен.
    #   This method added in API level 30.
    #   Этот метод введен в API level 30.
    #   https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInstallingPackageName()
    #
    # getPackageName() -> abstract String:
    #   Return the name of this application's package.
    #   Возвращает имя пакета этого приложения.
    #   https://developer.android.com/reference/android/content/Context#getPackageName()
    def package_name_installer_show(self) -> str:
        if 'android' == platform:
            try:
                # if (30 > int(self.sdk_show())):
                if (30 > api_version):
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
                return 'EXCEPT JAVA: ' + str(e)
            except BaseException as e:
                return 'EXCEPT PYTHON: ' + str(e)
        else:
            # return 'Данный метод не реализован ...'
            return 'This method is not implemented ...'
    # ---------------------------------------------------------------------------
    # Android:
    # getDataDir() -> abstract File:
    #   Returns the absolute path to the directory on the filesystem 
    #   where all private files belonging to this app are stored.
    #   Возвращает абсолютный путь к каталогу в файловой системе, 
    #   где хранятся все личные файлы, принадлежащие этому приложению.
    #   https://developer.android.com/reference/android/content/Context#getDataDir()
    #
    # getAbsolutePath() -> String:
    #   Returns the absolute path of this file.
    #   Возвращает абсолютный путь к этому файлу.
    #   https://developer.android.com/reference/java/io/File#getAbsolutePath()
    def path_absolute_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    Context.getDataDir().getAbsolutePath()
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
    # getPackageCodePath() -> abstract String:
    #   Return the full path to this context's primary Android package.
    #   Верните полный путь к этому конкретному основному пакету Android.
    #   https://developer.android.com/reference/android/content/Context#getPackageCodePath()
    #   По этому пути хранится копия приложения - base.apk
    #   A copy of the application is stored on this path - base.apk
    def path_full_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    Context.getPackageCodePath()
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
    # getFilesDir() -> abstract File:
    #   Returns the absolute path to the directory on the filesystem where files 
    #   created with openFileOutput(String, int) are stored.
    #   Возвращает абсолютный путь к каталогу в файловой системе, 
    #   в котором хранятся файлы, созданные с помощью openFileOutput(String, int).
    #   https://developer.android.com/reference/android/content/Context#getFilesDir()
    #
    # getAbsolutePath() -> String:
    #   Returns the absolute path of this file.
    #   Возвращает абсолютный путь к этому файлу.
    #   https://developer.android.com/reference/java/io/File#getAbsolutePath()
    def path_files_app_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    Context.getFilesDir().getAbsolutePath()
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
    # primary_external_storage_path() -> String:
    #   gets the path to the internal storage in Android.
    #   получает путь к внутреннему хранилицу в Android.
    #   https:?
    def path_to_primary_external_storage_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    primary_external_storage_path()
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
    # fileList() -> abstract String[]:
    #   Returns an array of strings naming the private files associated 
    #   with this Context's application package.
    #   Возвращает массив строк, именующих личные файлы, 
    #   связанные с этим пакетом приложений Contexts.
    #   https://developer.android.com/reference/android/content/Context#fileList()
    def files_app_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    '\n'.join(Context.fileList())
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
    # getDefault() -> static Locale:
    #   Gets the current value of the default locale for this instance 
    #   of the Java Virtual Machine.
    #   Возвращает текущее значение языкового стандарта по умолчанию 
    #   для данного экземпляра виртуальной машины Java.
    #   https://developer.android.com/reference/java/util/Locale#getDefault()
    #
    # getDisplayLanguage() -> String:
    #   Returns a name for the locale's language that is appropriate 
    #   for display to the user.
    #   Возвращает имя языка локали, подходящее для отображения пользователю.
    #   https://developer.android.com/reference/java/util/Locale#getDisplayLanguage()
    def language_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    Locale.getDefault().getDisplayLanguage()
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
    # SDK_INT -> static final int:
    #   The SDK version of the software currently running on this hardware device.
    #   Версия SDK программного обеспечения, запущенного в настоящее время 
    #    на этом аппаратном устройстве.
    #   https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT
    def sdk_show(self) -> str:
        if 'android' == platform:
            try:
                return str(
                    'VERSION.SDK_INT: ' + str(VERSION.SDK_INT) + '\n' +
                    'api_version: ' + str(api_version)
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
    # vibrator.vibrate(n) -> None:
    #   Ask the vibrator to vibrate for the given period.
    #   :param time: Time to vibrate for, in seconds. Default is '0.5'.
    #   Попросите вибратор вибрировать в течение заданного периода времени.
    #   :param time: Время для вибрации в секундах. Значение по умолчанию равно '0.5'.
    #   https://github.com/kivy/plyer/blob/master/plyer/facades/vibrator.py
    #
    # vibrator.exists() -> None:
    #   Check if the device has a vibrator. Returns True or False.
    #   Проверьте, есть ли в устройстве вибратор. Возвращает значение True или False.
    #   https://github.com/kivy/plyer/blob/master/plyer/facades/vibrator.py
    def vibrator_run(self, time=0.5) -> bool:
        '''
        Ask the vibrator to vibrate for the given period.

        :param time: Time to vibrate for, in seconds. Default is '0.5'.
        '''
        if 'android' == platform:
            try:
                if vibrator.exists():
                    vibrator.vibrate(time)
                    return True
                else:
                    return False
            except JavaException as e:
                return 'EXCEPT JAVA: ' + str(e)
            except BaseException as e:
                return 'EXCEPT PYTHON: ' + str(e)
        else:
            # return 'Данный метод не реализован ...'
            return 'This method is not implemented ...'
    # ---------------------------------------------------------------------------
    # Methods
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    pass
# *****************************************************************************************