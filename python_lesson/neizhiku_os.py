# coding=utf-8
# 内置库  os
import os
# help(os)#查看os的帮助文档
# print(dir(os))#查看os的属性和方法,返回的是个列表
'''os 系统相关'''
#获取系统名称
print(os.name)#nt-->win
#获取系统的环境变量信息
print(os.environ)#environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'ANDROID_HOME': 'D:\\android-sdk_r24.4.1-windows\\android-sdk-windows', 'APPDATA': 'C:\\Users\\longmin\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LAPTOP-6GSA86E7', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\longmin', 'IDEA_INITIAL_DIRECTORY': 'C:\\Program Files\\JetBrains\\PyCharm 2020.1\\bin', 'JAVA_HOME': 'D:\\java\\jdk', 'LOCALAPPDATA': 'C:\\Users\\longmin\\AppData\\Local', 'LOGONSERVER': '\\\\LAPTOP-6GSA86E7', 'NODE_PATH': 'D:\\nodejs\\node_modules', 'NUMBER_OF_PROCESSORS': '6', 'ONEDRIVE': 'C:\\Users\\longmin\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\longmin\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\longmin\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\pywin32_system32;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;D:\\java\\jdk\\bin;C:\\Users\\longmin\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\;C:\\Users\\longmin\\AppData\\Local\\Programs\\Python\\Python37\\;C:\\Users\\longmin\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files\\JetBrains\\PyCharm 2020.1\\bin;D:\\android-sdk_r24.4.1-windows\\android-sdk-windows\\tools;D:\\android-sdk_r24.4.1-windows\\android-sdk-windows\\platform-tools;D:\\allure-2.14.0\\bin;C:\\Program Files (x86)\\Google\\Chrome\\Application;D:\\Git\\cmd;C:\\Program Files\\dotnet\\;D:\\java\\jdk\\jre\\bin;D:\\java\\jdk\\lib\\tools.jar;D:\\nodejs\\;D:\\nodejs\\node_global;C:\\Users\\longmin\\AppData\\Local\\Programs\\Appium;D:\\MultiScreenCopy\\MultiScreenCopy;D:\\GnuWin32\\bin;C:\\Program Files (x86)\\dotnet\\;D:\\ffmpeg-n4.4.1-2-gcc33e73618-win64-gpl-shared-4.4\\ffmpeg-n4.4.1-2-gcc33e73618-win64-gpl-shared-4.4\\bin;D:\\python27;D:\\python27\\Scripts;D:\\mumu\\emulator\\nemu\\vmonitor\\bin;C:\\Users\\longmin\\scoop\\shims;C:\\Users\\longmin\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\;C:\\Users\\longmin\\AppData\\Local\\Programs\\Python\\Python37\\;C:\\Users\\longmin\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\JetBrains\\PyCharm 2020.1\\bin;;D:\\fiddler;C:\\Users\\longmin\\.dotnet\\tools;C:\\Users\\longmin\\AppData\\Roaming\\npm;C:\\Users\\longmin\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\numpy\\.libs', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD', 'PROCESSOR_LEVEL': '23', 'PROCESSOR_REVISION': '6001', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2020.1\\bin;', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'E:\\py23;C:\\Program Files\\JetBrains\\PyCharm 2020.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend;C:\\Program Files\\JetBrains\\PyCharm 2020.1\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\longmin\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\longmin\\AppData\\Local\\Temp', 'TMPDIR': 'C:\\Users\\Public\\Documents\\Wondershare\\CreatorTemp', 'USERDOMAIN': 'LAPTOP-6GSA86E7', 'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-6GSA86E7', 'USERNAME': 'longmin', 'USERPROFILE': 'C:\\Users\\longmin', 'WINDIR': 'C:\\Windows', 'WXDRIVE_START_ARGS': '--wxdrive-setting=0 --disable-gpu --disable-software-rasterizer --enable-features=NetworkServiceInProcess'})
#获取 指定名称 的环境变量信息
print(os.getenv('path'))#C:\Users\longmin\AppData\Local\Programs\Python\Python37\lib\site-packages\pywin32_system32;C:\ProgramData\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;D:\java\jdk\bin;C:\Users\longmin\AppData\Local\Programs\Python\Python37\Scripts\;C:\Users\longmin\AppData\Local\Programs\Python\Python37\;C:\Users\longmin\AppData\Local\Microsoft\WindowsApps;C:\Program Files\JetBrains\PyCharm 2020.1\bin;D:\android-sdk_r24.4.1-windows\android-sdk-windows\tools;D:\android-sdk_r24.4.1-windows\android-sdk-windows\platform-tools;D:\allure-2.14.0\bin;C:\Program Files (x86)\Google\Chrome\Application;D:\Git\cmd;C:\Program Files\dotnet\;D:\java\jdk\jre\bin;D:\java\jdk\lib\tools.jar;D:\nodejs\;D:\nodejs\node_global;C:\Users\longmin\AppData\Local\Programs\Appium;D:\MultiScreenCopy\MultiScreenCopy;D:\GnuWin32\bin;C:\Program Files (x86)\dotnet\;D:\ffmpeg-n4.4.1-2-gcc33e73618-win64-gpl-shared-4.4\ffmpeg-n4.4.1-2-gcc33e73618-win64-gpl-shared-4.4\bin;D:\python27;D:\python27\Scripts;D:\mumu\emulator\nemu\vmonitor\bin;C:\Users\longmin\scoop\shims;C:\Users\longmin\AppData\Local\Programs\Python\Python37\Scripts\;C:\Users\longmin\AppData\Local\Programs\Python\Python37\;C:\Users\longmin\AppData\Local\Microsoft\WindowsApps;;C:\Program Files\JetBrains\PyCharm 2020.1\bin;;D:\fiddler;C:\Users\longmin\.dotnet\tools;C:\Users\longmin\AppData\Roaming\npm;C:\Users\longmin\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\.libs
print(os.getenv('PATH'))#大小写 都是可以的
#执行系统命令
os.system('pwd')#----》linux系统用
print(os.system('dir'))#-----》win系统
print(os.getcwd())#--->一样可以打印出当前目录的路径E:\py23\python_lesson

'''os 目录相关'''
#获取当前所在的目录
print(os.getcwd())#E:\py23\python_lesson
#切换目录
os.chdir('..')#切换到上一级目录
print(os.getcwd())#E:\py23
#列出当前目录下的所有文件
print(os.listdir())#['.mypy_cache', 'cuowu_yichang.py', 'jihe.py', 'kongzhiliu_if_panduan.py', 'kongzhiliu_xunhuan.py', 'lambda.py', 'liebiao.py', 'neizhiku_os.py', 'neizhi_zhuangshiqi.py', 'python_hanshu.py', 'python_mianduiduixiang.py', 'str_python.py', 'yuanzu.py', 'zidian.py', '__init__.py']
#创建空目录
os.mkdir('kongmulu')#左边就可以看到当前目录下创建了一个叫kongmulu的空目录
#递归创建目录
os.makedirs('a/b/c')#左边就可以看到当前目录下创建了一个递归目录a->b->c
#创建空目录
os.mkdir('kongmulu1')
os.rmdir('kongmulu1')#只能删除空目录，不能删除非空目录
#重命名目录
os.mkdir('hello')
os.rename('hello','demo')#把原本的hello的目录改名叫demo

#删除文件
# 先手动创建一个1.txt文件
os.remove('1.txt')#就可以看见原本的1.txt给删除掉了，这个txt有无内容都可以被删除

'''os 路径相关'''
#返回绝对路径
print(os.path.abspath('./neizhiku_os.py'))#E:\py23\python_lesson\neizhiku_os.py
# basename--->neizhiku_os.py
# dirname--->E:\py23\python_lesson
# 返回文件名
print(os.path.basename('/py23/python_lesson/neizhiku_os.py'))#neizhiku_os.py
# 返回文件路径
print(os.path.dirname('/py23/python_lesson/neizhiku_os.py'))#/py23/python_lesson

# 分割路径
print(os.path.split('/py23/python_lesson/neizhiku_os.py'))#('/py23/python_lesson', 'neizhiku_os.py')
# 切割成元组  一个文件名 一个文件路径

# 拼接路径
print(os.path.join('/py23/python_lesson', 'neizhiku_os.py'))#/py23/python_lesson\neizhiku_os.py


# 判断路径 是否存在
print(os.path.exists('/py23/python_lesson/neizhiku_os.py'))#True
print(os.path.exists('./neizhiku_os.py'))#True
#---->所以的绝对路径 相对路径都是可以判断的

# 判断是否是目录
print(os.path.isdir('/py23/python_lesson'))#True
print(os.path.isdir('/py23/python_lesson/neizhiku_os.py'))#False--->因为这个不是个目录 是个文件的地址

# 判断是否是文件
print(os.path.isfile('/py23/python_lesson/neizhiku_os.py'))#True

#获取文件大小
print(os.path.getsize('./neizhiku_os.py'))#8732--->字节大小
