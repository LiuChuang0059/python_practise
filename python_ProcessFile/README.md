# 文件处理

## 1  读写文件

### 1 读取文件

#### 1 文件路径
> 1 文件在程序文件目录 或者目录下的文件夹
使用相对路径打开文件
> 2 文件在其他文件夹  提供绝对路径
'c:\Users\ehmatthes\other_files'

#### 2 read
.read():读取文件内容 储存字符串在变量中
.readlines(): 读取每一行，储存在列表里
储存在别的变量下 可在with调用文件语句外 使用

#### 3 with
```python
with open(filename,'w') as file_object:

首先执行open('output', 'w')，返回一个文件对象；
调用这个文件对象的__enter__方法，并将__enter__方法的返回值赋值给变量f；
执行with语句体，即with语句包裹起来的代码块；
不管执行过程中是否发生了异常，执行文件对象的__exit__方法，在__exit__方法中关闭文件。
这里的关键在于open返回的文件对象实现了__enter__和__exit__方法。一个实现了__enter__和__exit__方法的对象就称之为上下文管理器。

```

###2  写入文件
> 只能将字符串写入文本，数值数据需先转换 str（）


### 4 创建文件夹
```python
import os 
os.makedirs('C:\\Liu\\Chuang\\o')
###创建多层文件夹
```

### 5 os.path 模块 ： 文件名和文件路径

#### 1 绝对路径 和相对路径
```python
os.path.abspath('.') ##'.'对应着当前路径
os.path.isabs()# 判断是否为绝对路径
os.path.basename('')## 文件名
os.path.dirname('')## 文件路径名
os.path.split('')## t同时获得 文件名和路径的元组 的
```

#### 2 查看文件和文件夹 内容 
```python
os.path.getsize('') ###返回文件的字节数
os.listdir('')## 返回路径下的所有文件
###利用个循环 可以计算 路径下所有文件 总字节数
```

#### 3 检查路径的有效性
```python
os.path.exists()  ### 检测路径是否存在
os.path.isdir('')###path 存在 并且是一个文件夹
os.path.isfile('')  ### path 存在 并且是一个文件
```



### 6 用 shelve 模块 保存变量 (二进制文件)
```python
import shelve 
shelfFile= shelve.open('mydata')
Men=['Liu','Chuang','chuang'] 
## 类似于字典 有keys  有values 
shelfFile['man']=Men
shelfFile.close()
```


### 7 pprint.pformat（） 函数保存变量  创建py 文件
```python
import pprint
cats=[{'name':'Liu','Age':'16'},{'name':'Chuang','age':'12'}]
fileCat=open('mycat.py','w')
fileCat.write('cats =' + pprint.pformat(cats) + '\n')## pprint 返回字符串
fileCat.close()

#导入python 脚本
import mycat
mycat.cats
mycat.cats[0]
### 只有基本数据类型 整形 浮点型 字符串 列表 字典 作为简单文本写入
```


## 2 组织文件
### 1 shutil 模块

#### 1 复制文件和文件夹
```python
import os,shutil

os.chdir('C:\\') ## 更爱当前目录
shutil.copy('sourse','destination')  #！！！ 返回一个字符串 被复制文件的路径
### 如果 destination 是一个文件名  ，复制文件的新名字  否则 原名

shutil.copytree("c:\\a","c:\\a_backup") ###复制整个文件夹 以及他包括的文件以及文件夹
### 相当于备份 a
```

#### 2  文件和文件夹的移动
```python
shutil.move('sourse','destination')
```
* 1 des为文件夹 则文件 移入文件夹 保存原有的文件名 ！！！ 很可能和源文件冲突覆盖
* 2 des 为文件名  则将文件移动到文件夹并且 更改名字
```python
shutil.move("C:\\bacon.txt","C:\\eggs\\new_bacon.txt")
```

* 3 如果目录下没有文件夹 所以假定des指定的是一个文件而不是文件夹，
```python
bacon.txt ##文本文件改名为 eggs 无扩展名
```

#### 3 永久删除文件和文件夹
```python
os.unlink(path)## 删除路径的文件
os.rmdir(path)## 删除路径的空文件夹
os.rmtree(path) ## 删除文件夹以及其包含的所有文件和文件夹
```

#### 4 文件删除到 回收站 ： send2trash
```python
import send2trash
send2trash.send2trash("")
```

### 2 遍历目录树：  处理文件夹中的每一个文件
```python
import os 
for folderName,subfolders,filenames in os.walk("C:\\"):
    print(folderName)
os.walk()###返回三个值 1 当前文件夹的字符串 2 当前文件夹的子文件夹 字符串列表 3 当前文件夹的文件字符串列表
```

### 3 zipfile模块 压缩 文件
#### 1 读取 ZIP文件
```python
import zipfile ,os
os.chdir(r'C:\Users\dell\Desktop\summer_camp\LAMDA')
liuzip=zipfile.ZipFile('Liu.zip')
names=liuzip.namelist()
for name in names:
    print(name.decode('utf-8'))###?如何打印中文 待解决
    
LiuInfo=liuzip.getinfo('spam.txt')
LiuInfo.file_size
LiuInfo.compress_size

"""
import os

inpath = 'G:\Android\MyAndroid\UI设计'
uipath = unicode(inpath,"utf-8")  ##对路径进行utf-8编码

list = os.listdir(uipath)   ##获得文件目录列表

for each in list:   ##遍历list列表
   print(each.encode('utf-8'))   ##将该目录下文件名全部打印出来

import codecs 
f = codecs.open('text.text','r+',encoding='utf-8')#必须事先知道文件的编码格式，这里文件编码是使用的utf-8 
content = f.read()#如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将将会产生错误 
f.write('你想要写入的信息') 
f.close()

import chardet  
# 获取文件编码类型  
def get_encoding(file):  
    # 二进制方式读取，获取字节数据，检测类型  
    with open(file, 'rb') as f:  
        return chardet.detect(f.read())['encoding']  
 
file_name = 'my.ini'  
encoding = get_encoding(file_name)  
print(encoding)
"""
```

#### 2 从zip中解压缩
```python
liuzip.extractall('A')  # 全部解压  可以传入一个文件夹名称  解压缩到 文件夹目录 
liuzip.extract('B.txt',A)## 单个解压到指定目录
```

#### 3 创建压缩文件
```python
import zipfile
new_zip=zipfile.ZipFile('new.zip','w')
new_zip.write('spam.txt',compress_type=zipfile.ZIP_DEALATED)
##'w'写入会擦除原有内容 ‘a’添加
new_zip.close()
```
