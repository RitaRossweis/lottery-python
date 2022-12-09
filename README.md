# 一个抽奖程序

曾用于南京大学电子科学与工程学院2022年迎新晚会抽奖，这个程序是在网络上的一个开源程序的基础上扩展而来的， 其优势在于可以自定义背景图片并正常打包成exe。

# 优势

常规情况下，直接将py文件与外部png文件一起打包成exe，执行会报错。

本程序解决了这个问题，要求是替换图片要保证图片在项目根目录下，或者在代码中修改相对路径

如果将程序打包成exe使用，则要求图片必须与exe位于同一路径

# 软件需求 

编译环境：
Python 3.9

软件包需求：
tkinter
pyinstaller

#  使用方法

测试运行可在main.py中直接运行

打包成exe并运行时，可以在项目路径下打开命令行窗口执行指令
```cmd
pyinstaller -F -w main.py
```
之后可在./dist中找到main.exe，双击运行即可

如果把main.exe分享给其他计算机使用，需要同时把图片分享出去，并保证图片与程序在同一路径下