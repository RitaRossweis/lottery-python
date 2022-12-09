import os
import sys
import os.path

'''
gtj 打包路径问题,通常打包成单一运行文件exe后,运行时会将程序解压到临时文件夹(解压路径),此时如果程序中有引用txt或QSS都会在解压路径,所以要引用前
1.先将工作路径变为解压路径
    os.chdir(base_path(''))

2.要对程序所在路径进行读写
    os.chdir(os.getcwd())
'''


def base_path(path):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    return os.path.join(application_path, path)


application_path = base_path('')  # 这是解压路径