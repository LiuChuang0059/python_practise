
# python 基础学习




# 0 基本
* [Python·内置函数](https://docs.python.org/3/library/functions.html)
* [Python.模块](https://pymotw.com/3/)
* [python.代码格式](https://www.python.org/dev/peps/pep-0008/)

> The Software Development Process
* What (Analysis)
* How (Design)
* Do It (Implementation)
* Test (Testing and Debugging)
* Use (Operation or Deployment)
* Maintain (Refinement)

[what is the next.](https://python.swaroopch.com/what_next.html)

### 静态语言 vs 动态语言（待解决）
* 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

* 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
```python
class Timer(object):
    def run(self):
        print('Start...')
```
* 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

> Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。


-------

# 1  完全拷贝 和 复制地址
### 1 list 拷贝
> Remember that if you want to make a copy of a list or such kinds of sequences or complex objects (not simple objects such as integers), then you have to use the slicing operation to make a copy. If you just assign the variable name to another name, both of them will ''refer'' to the same object and this could be trouble if you are not careful.

```python
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist

# I purchased the first item, so I remove it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object

print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different
```

### 2 copy 模块 包含 copy()和 deepcopy()两个函数
```python
import copy
list1=[1,2,3,4,5]
list2=copy.copy(list1)###产生一个新的独立的列表
list3=list1 ##  变量名指向列表
list1.append(7)
print(list1,list2,list3)

list4=[12,3,4,[23,3,4],5]
list5=list4
list6=copy.deepcopy(list4)###完全复制创建新的列表中列表
list7=copy.copy(list4)###只创建了外层 内层还是指向原列表
list4.append(1111)
list4[3].append(22222)
```

-------

# 2  os 目录文件
#### 1 创建目录
> 在Python中可以使用os.mkdir()函数创建目录（创建一级目录）。
```python
os.mkdir(path)

## 其参数path 为要创建目录的路径。
```
* 例如要在D盘下创建hello的目录

```python
>>> import os
>>> os.mkdir('d:\hello')
```

#### 2 os.makedirs（）函数创建多级目录。

* 如在D盘下创建books的目录，books目录下在创建book目录
```python
>>> import os
>>>os.makedirs('d:\\books\\book')
```

#### 3 删除目录
> 在Python中可以使用os.rmdir()函数删除目录。
```python
os.rmdir(path)
其参数path 为要删除的目录的路径。
```
* 例如把D盘下的hmm的目录删除
```python
>>> import os
>>> os.rmdir('d:\hmm') 
```

#### 4 删除多级目录
> 在Python中可以使用os.removedirs()函数删除多级目录。
```python
os.removdirs(path)
# 其参数path 为要删除的多级目录的路径。

```

```python
>>> import os
>>> os.removedirs('d:\\books\\book')
```
**注意：要删除的目录必须是空目录**

#### 5 删除文件
> 在Python中可以使用os.remove()函数删除文件（注意一定是一个文件）。
```python
os.remov(path)
其参数path 为要删除的文件的路径。
```

* 如删除D盘下books目录下book目录中的book.txt的文件


```python
>>> import os
>>>os.remove('d:\\books\\book\\book.txt')
```

#### 6 遍历目录
> 在Python中可以使用os.walk()函数遍历目录。
```python
os.walk(path)
#其参数path 为要遍历的目录，遍历path，返回一个对象，他的每个部分都是一个三元组 ('目录x'，[目录x下的目录list]，目录x下面的文件) 。
如：
```

```python
>>> a=os.walk('d:\\books')
>>> def  fun():
               for i in a:
                        print i
>>> fun()
('d:\\books', ['book'], ['aa.txt'])
('d:\\books\\book', [ ], [ ])
```
#### 7 判断是否为目录
> 在Python中可以使用os.path.isdir()函数判断某一路径是否为目录。
```python
os.path.isdir(path)
#其参数 path为 要进行判断的路径。如果是则返回TRUE,否则返回FALSE。
```
#### 8 判断是否为文件
> 在Python中可以使用os.path.isfile()函数判断某一路径是否为文件。
```python
os.path.isfile(path)
其参数path为要进行判断的路径。如果是则返回TRUE,否则返回FALSE。
```


---------

# 3 Unicode

* 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

* 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
* [服务器字符编码：浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器](https://cdn.liaoxuefeng.com/cdn/files/attachments/001387245979827634fd6204f9346a1ae6358d9ed051666000/0)


* [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets"](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

* [Python Unicode Howto](https://docs.python.org/3/howto/unicode.html)

* [Pragmatic Unicode talk by Nat Batchelder](https://nedbatchelder.com/text/unipain.html)


----------

# 4 正则表达式 regex: 文本描述方法
### 1 创建对象 compile()

```python
import re  #包含所有正则表达式模块

re.compile()#传入字符  返回一个regex对象
re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')##  r--原始字符串
```

### 2 匹配对象  
#### 1 search()  包含第一次搜到的文本

```python
phonenumber_regex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumber_regex.search('my number i s 123-234-4557')
##search搜到返回 Mark对象 没有 返回None
mo.group()
###调用Match对象的group方法

```

#### 2 findall() 返回所有的字符串列表或者元组列表

* 1. 没有分组的正则表达式返回字符串列表
*  2. 分组的正则表达式返回元组的列表

### 3 利用符号 匹配更多模式
#### 1 括号--分组

```python
phonenum_regex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo=phonenum_regex.search(message1)
print('\n'+mo.group(1))##参数为0或者空 返回整个文本
areacode,b=mo.groups()###groups  返回所有分组
print('\n' + 'areacode:'+areacode +'  b: ' +b)
```

#### 2 利用管道'|' 匹配多个分组

```python
message2='Batman and TomFord'
message3='TomFord and Batman'

hero_regex=re.compile(r'Batman|TomFord')
mo=hero_regex.search(message2)
print('\n'+ mo.group())

mo=hero_regex.search(message3)
print('\n'+ mo.group())
###多通道的时候 返回第一次出现的字符
```

#### 3 用问号实现可选分配 ;匹配 1次或者0次

```python
# 字符 ？表明它的前面的分组在这个模式中是可选的
bat_regex= re.compile(r'Bat(wo)?man')
mo=bat_regex.search('The Adventures of Batman')
if mo !=None:
    print('\n'+mo.group())

mo=bat_regex.search('The Adventures of Batmaen')
if mo !=None:   ###
    print('\n'+mo.group())
else:
    print('\nNone')
```

#### 4 利用*号匹配 零次或者多次 加号+匹配一次或者多次

```python
bat_regex= re.compile(r'Bat(wo)*man')
mo=bat_regex.search('The Adventures of Batman')
if mo !=None:
    print('\n'+mo.group())
mo=bat_regex.search('The Adventures of Batwowowoman')
if mo !=None:
    print('\n'+mo.group())
```

#### 5 花括号匹配特定次数{}

```python
(liu){3}匹配3次
(liu){3,5}匹配3-5次
(liu){3,}3到更多次
(liu){,5}0-5次
```

### 4 贪心与非贪心匹配
* 1 贪心:默认 在有很多匹配的时候 匹配最长的字符串
* 2 非贪心:在{}后面加上一个? 匹配最短的字符串

### 5 常用缩写字符分类
| 缩写字符    | 表示   |  
| ----- | -- | 
| \d     | 0-9任何数字 |   
| \d+     | 0-9任何数字(一个或者多个数字) |  
| \D     |   0-9外所有字符  |  
| \w        |    任何字母数字或者下划线字符|
| \W        |    除去字母数字或者下划线字符|
| \s    | 空格 制傅表 或者换行符|
| \S   | 除去空格 制傅表 或者换行符|

### 6 建立自己的字符分类 []定义

* 1. r'[aeiouAEIOU]' ：匹配所有的元音
* 2. r'[a-zA-Z0-9]':匹配所有的字母数字
* 3. 插入'^' 表示反义 (r'[^aeiouAEIOU]')

### 7 '$' and '^'

* 1. '^' 匹配最开始处
* 2. '$' 以该正则模式结束  ： r'\d$' -- 以0-9 数字结束
* 3. '^\d$'---从开头到结尾都是数字

### 8 通配字符
#### 1 '.'匹配 除了换行之外 所有的字符（值匹配 一个字符）

```python
at_regex=re.compile(r'.at')
```

#### 2 '.*'匹配 所有字符  默认贪心模式

```python
# * 表示前面字符出现零次或者多次
name_regex=re.compile(r'First Name: (.*) Last Name: (.*)')

#非贪心模式 尽可能短 加？
(.*?)
```

#### 3 传入 re.DOTALL 句点字符匹配换行

```python
new_regex=re.compile(r'.*',re.DOTALL)
```

### 9 大小写匹配  传入re.IGNORECASE or re.I  则 大小写皆可替换

```python
re.compile(r'LIuchuang',re.I)
```

### 10 替换字符串 sub()
* sub() 第一个参数为字符串用于取代发现的匹配，第二个为待修改的字符串。

```python
name_regex=re.compile(r'Agent \w+')
name_regex.sub('Liu','Agent LIuchuang Gave   kd  kk KK ')
```

### 11 复杂的正则表达式 传入 re.VERBOSE 进行分行

```python
phone_regex=compile(r'''(
            (\d{3})|\(d{3}\))? ##可选分组 区号121 或者（112）
            (\s|-|\.)?   ### 分隔符
            \d{3}      ###前三位
            (\s|-|\.)
            \d{4})###后四位
            ''',re.VERBOSE)
```
 
----------



# 5 字符串
### 1字符串类型
![](https://images2018.cnblogs.com/blog/884071/201711/884071-20171127154213565-171071034.png)
* 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

```python
'ABC'.encode('ascii')
'中文'.encode('utf-8')
```

* 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

```python
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')#忽略错误字节
```

* 要计算str包含多少个字符，可以用len()函数：
```python
len('ABC')
len("中国话")
```

### 2 字符串方法
> 这些方法没有改变字符串本身 ，而是返回一个新的字符串

* 1 upper(),lower()

```python
str=str.upper()
```

* 2 isupper(),islower()
```python
str.isupper() :所有字母都是大写  返回True
str.islower()

isalpha():只包含字母 并且非空 
isdecimal()：只包含数字 并且非空
isalnum():只包含字母数字并且非空 返回True
isspace(): 只包含 空格制表符和换行，并且非空
istitle():字符串 包含以大写字母开头 后面都是小写的单词
```

* 
```python
* str.isalnum() 所有字符都是数字或者字母 
* str.isalpha() 所有字符都是字母 
* str.isdigit() 所有字符都是数字 
* str.islower() 所有字符都是小写 
* str.isupper() 所有字符都是大写 
* str.istitle() 所有单词都是首字母大写，像标题 
* str.isspace() 所有字符都是空白字符、\t、\n、\

```
**循环输入直到有效输入**

* 3 startwith(),endwith()

```python 
#判断字符串开头结尾
'Hello World'.startwith('Hello')
```

* 4 join() 和 split()

```python
#join()在一个字符串上调用，参数为字符串列表，返回一个字符串
','.join(['hello','world'])

#split() 在一个字符串上调用 返回列表 
'hello world'.split()#，默认以空白字符串分割
`helloABCworldABCoh'.split('ABC')
''.split('\n')#以换行符 切割   多行字符串
```

* 5 rjust();ljust,center() 左右中心对齐

```python
'Hello'.rjust(20,'*')#总长度为20 第二个参数为填充字符
```

* 6 rtrip(),ltrip(),strip() ：删除 空白字符（空格制表符，换行符），返回新的字符串

```python
str=str.rtrip()

str.strip('abc')#删除两边的字符 顺序不重要 出现既可以删除
```


----------


# 6 print 格式化 代替

```python
print("%s : %d",%('L.C',23))

#%d整数

print('%2d-%03d' % (300, 1))#03 在1 前面补位 n-1个0 

#%f浮点数

print('%.2f' % 3.1415926)#保留两位小数

#%s字符串
#%z 十六进制整数
```
* [f-strings](https://docs.python.org/3/whatsnew/3.6.html#new-features)


## 4漂亮打印- 字典存在嵌套时
从程序中导入pprint模块 使用pprint()函数 使得键值排序 
```python
message="I love  you 'Zou Xiaowei'"
count={}

for character in message:
    count.setdefault(character,0)
    count[character]+=1
print(count)
pprint.pprint(count)

```
----------





# 7 函数

### 1 默认参数
> 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
* 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思  考一下为什么默认参数不能放在必选参数前面）；
*  二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

 **定义默认参数要牢记一点：默认参数必须指向不变对象！**

### 2函数的参数改为可变参数(参数前加一个* )任意数量的实参
* 1.

```python
def calc(*numbers): # 创建一个空元祖
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
>>> calc(1, 2)
5
>>> calc()
0
```

* 2.任意数量关键字实参：
> 函数 接受任意数量的 K-V值
```python
def fun(first,last,**user_info):
```
> *args and **kwargs
*args： 把所有的参数按出现顺序打包成一个 list
**kwargs：把所有 key-value 形式的参数打包成一个 dict

### 3 函数 传递列表
#### 1 传递 输入
```python
def greet_users(names)
    for name in names:
        print(name)
user_names=[]
greet_users(user_names)
```

#### 2 禁止函数修改 列表
> 将列表的副本传递给函数
```
 function_name(list_name[:])
```
 
### 4 高级函数
#### 1 map
* map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
```python
def f(x):
    return x*x
r=list(
map(f,[1,2,3,4,5,6,7]))
print(r)
```

#### 2 reduce
* reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：o
```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

### 5 filter 函数 筛选 过滤
#### 1 列表项
* filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
```python
def is_odd(s):
    return s%2==1

A=list(filter(is_odd,[1,2,3,4,5,6,7,8,9,89,99]))
print(A)
```

#### 2 应用 
**求素数**

### 6 匿名函数
```python
def f(x):
    return x*x

lambda x:x*x
f=lambda x: x*x

```


----------
# 8 模块
### 1 导入模块
* 1 导入整个模块
> 在相同目录创建文件，
* pizza.py 包含（make_pizza 函数）and make_pizzas.py
```python 
import pizza
pizza.make_pizza(16)
```

* 2 导入特定函数

```python
from pizza import function_0,function_1,function_2
function_0()
```
* 3 as 给函数指定别名

```python
from pizza import make_pizza as mp
mp()
```

* 4 as 给模块命名

```python
import pizza as p##功能描述性名称
p.make_pizza()
```

* 5 导入模块所有函数
```python
from pizza import * ##复制所有的函数
make_pizza()## 不需要前缀
```

**大型模块不宜使用**


----------
# 9 类  面向对象编程
### 1 编码风格
>  定义的一大类对象  有通用行为，基于类 创建对象时 每个对象自动拥有这些行为，根据需要赋予特性
> 首字母 大写指的是类Dog（）
* 实例名称和模块名都是小写加下划线 ： my_dog
> 类 在定义后 应该包含一个文档字符串 描述功能
* 一个空行分隔 方法def  两个空行分隔 类
* 先导入标准库模块  空一行 导入自己编写的模块


```python
Class Dog():
__init__(self,name,age)##方法
##self:调用init时候，自动传入实参self，每个与类相关的方法调用###都自动传递实参self，指向实例的引用，让实例能访问类中的属性方##法。不需要提供数值
self.name=name# self###为前缀的变量可以供类中所有方法使用，类########的实例也可以访问 称为 属性、
```

### 2 调用
* 创造实例后 句点调用方法
```
my_dog=Dog('asd',13)
my_dog.sit()
```

### 3 添加属性默认值

```python
self.name=0
```

### 4修改属性的值
> 通过方法修改属性的值
```
def update(self,m):
    self.name=m
```
**通过判断 设定修改范围 或者禁止修改**

----------

# 10 list 

### 0 list切片
```python
list[:]##全部
list[-3:]##倒数三个
```

### 1 写列表生成式时，把要生成的元素x*x放到前面，后面跟for循环，就可以把list创建出来
```python
A=[x+x for x in range(1,20)]

B=[x+x for x in range(1,20) if x%2==0]
```

### 2 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
```python
E=[d for d in os.listdir('.')]

```

### 3 一个list中所有的字符串变成小写
```python
L = ['Hello', 'World', 'IBM', 'Apple']
F=[s.lower() for s in L]
M = ['Hello', 'World', 18, 'Apple', None]
G=[q.lower() for q in M if isinstance(q,str) ]#判断是否为字符串
```

### 4 tuple()不变    list[]可变
> 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

* [列表和元组相互转换]
(https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316724772904521142196b74a3f8abf93d8e97c6ee6000)

### 5 列表排序
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
```python
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]

list=[1,2,3,4,5,3,4,2]
list.sort(reserve=True) ##不能记录排序返回值
print(list)

list=['a','b','D','AA']
list.sort() #大写排在小写前A面
list.sort(key=str.lower)
```


----------
# 11  集合 set()

> 1.是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算. 
> 2.sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。

```python
    A=set([1,2,3,4])
    B=set([1,2,3])
    A|B #并集
    A&B #交集
    A-B #差集
    list(A) #转为列表
    [i for i in A] # 转为列表

```
```python
len(s)  #set 的长度  
x in s  #测试 x 是否是 s 的成员  
x not in s  #测试 x 是否不是 s 的成员  
s.issubset(t)  
s <= t  
#测试是否 s 中的每一个元素都在 t 中  

s.issuperset(t)  
s >= t  
#测试是否 t 中的每一个元素都在 s 中  

s.union(t)  
s | t  
#返回一个新的 set 包含 s 和 t 中的每一个元素  

s.intersection(t)  
s & t  
#返回一个新的 set 包含 s 和 t 中的公共元素  

s.difference(t)  
s - t  
#返回一个新的 set 包含 s 中有但是 t 中没有的元素  

s.symmetric_difference(t)  
s ^ t  
#返回一个新的 set 包含 s 和 t 中不重复的元素  

s.copy()  ##返回 set “s”的一个浅复制  
```


------

# 12 tuple 元组
### 1 赋值顺序
```python
a = 3
a, b = 1, a
print('a=',a,'\n''b=',b)

输出：a= 1
      b= 3
```

> 如果按正常思维肯定是先将1赋值给a，然后再将a值赋给b，实际上也确实是这样的，但是前面提到这样赋值其实右边相当于一个元组tuple，而tuple中的元素是不变的，所以后面的b=a中的a相当于t(1)是不变的,是前面a=3就已经确定好的，就是说a, b = 1, a这条语句是先执行右边即先创建一个元组，然后再是分为两条语句执行的先将1赋值给a，然后将元组中的a赋值给b

```python
max, min = min, max
#同时执行 不等价 分别min=max，max=min
print(max(1, 2, 3, 4, 5))
```
### 2元组（）
* 1.元组内数据不能赋值
* 2 但是可给储存元组的变量赋值

### 3 应用 
1 禁止修改图片尺寸
2 自助菜单点菜 两份菜单


----------



# 13 迭代器 和装饰器
### 1 迭代器判断
* 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。可以使用isinstance()判断一个对象是否是Iterator对象：

```python
>>> from collections import Iterator
isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)
```

### 2 转换成迭代器
* 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
```python
isinstance(iter([]), Iterator)
```
### 3 装饰器
> def:在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

* [1装饰器原理](https://www.zhihu.com/question/26930016/answer/99243411 )
* [2装饰器使用](https://blog.csdn.net/MDL13412/article/details/22608283)
```python
import time
def func():
    print("hello")
    time.sleep(1)
    print("world")

#原始侵入，篡改原函数
def func1():
    startTime=time.time()
    print("hello")
    time.sleep(3)
    print("world")
    endTime=time.time()
    mes=(endTime - startTime)*100
    print('time is %d ms'%mes)
   
func1()
#装饰器就像一个注入符号：有了它，拓展了原来函数的功能既不需要侵入函数内更改代码，#
#也不需要重复执行原函数。 
def deco(func2):
    def wrapp():
        startTime=time.time()
        func2()
        endTime=time.time()
        mes=(endTime - startTime)*100
        print('time is %d ms'%mes)
    return wrapp

@deco
def func2():
    print('hello')
    time.sleep(4)
    print('world')
  
func2()

##带有参数的装饰器
def deco1(func3):
    def wrapp1(a,b):
        startTime=time.time()
        func3(a,b)
        endTime=time.time()
        mes=(endTime - startTime)*100
        print('TIME is %d ms'%mes)
    return  wrapp1

@deco1
def func3(a,b):
    print('hello')
    time.sleep(0.3)
    print('sb')
    print('a+b =%d'%(a+b))
func3(5,6)    

##带有不定参数的装饰器
def deco2(func4):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func4(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper

@deco2
def func4(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco2
def func5(a,b,c):
    print("hello，here is a func  :")
    time.sleep(0.4)
    print("result is %d" %(a+b+c))


if __name__ == '__main__':
    f = func4
    func5(3,4,5)
    f(3,4)
    #func()

def deco01(func):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        print("deco01 end here")
    return wrapper

def deco02(func):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        func(*args, **kwargs)

        print("deco02 end here")
    return wrapper

@deco01
@deco02
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f = func
    f(3,4)
    #func()
```



# 14 随机数
* [在线字符串生成随机数生成](http://tools.jb51.net/aideddesign/suijishu)
* [高密度字符串密码](http://tools.jb51.net/password/CreateStrongPassword)

```python
print(random.uniform(10, 20))
print(random.uniform(20, 10)) 

用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，Python生成随机数

print(random.randint(12, 20)) #生成的随机数n: 12 <= n <= 20 
print(random.randint(20, 20)) #结果永远是20 
print(random.randint(20, 10)) #该语句是错误的,下限必须小于上限。
random.randrange
```

* 随机整数
```python
：
>>> import random
>>> random.randint(0,99)
21
```

* 随机选取0到100间的偶数：
```python
>>> import random
>>> random.randrange(0, 101, 2)
42
```
* 随机浮点数：

```python
>>> import random
>>> random.random() 
0.85415370477785668
>>> random.uniform(1, 10)
5.4221167969800881
```

* 随机字符
```python
>>> import random
>>> random.choice('abcdefg&#%^*f')
'd'
```

* 多个字符中选取特定数量的字符
```python
>>> import random
random.sample('abcdefghij',3) 
['a', 'd', 'b']
```

* 多个字符中选取特定数量的字符组成新字符串
```python
>>> import random
>>> import string
>>> string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).r
eplace(" ","")
'fih'
```

* 随机选取字符串：
```python
>>> import random
>>> random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )
'lemon'
```
* 洗
```python
>>> import random
>>> items = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(items)
>>> items
[3, 2, 5, 6, 4, 1]
```
--------



# 15  字典
![](https://raw.githubusercontent.com/LiuChuang0059/gitpic/master/dict_time.png)
### 1 添加 修改 删除键值对
```python
alien_0={}
alien_0['color']='green'
alien_0['point']=5
del alien_0['point'] #k-v del the same time

```
### 2 setfault（）确保一个键值的存在
```python
###setdefault()第一个参数检查是否存在该键值
###第二个参数  ，如果键值存在，返回键值，不存在  设置添加键值
dict1={'a':1,'b':2}
print(dict1.setdefault('c',3))
print(dict1)

##查找各个字符出现的次数
message="I love  you 'Zou Xiaowei'"
count={}
for character in message:
    count.setdefault(character,0)##确保字典里面有该键值
    count[character]+=1
print(count)
```
### 3 get获取键值：如果不存在，返回备用值
```
dict1={'a':1,'b':2}
a=dict1.get('a','None')
c=dict1.get('c','None')
print(a,c)
```
### 4 遍历字典
```
for k,v in alien_0.items():#遍历所有 key value

for k in alien_0.keys():# 只遍历 key
for k in alien_0  #等价上语句
```
### 5 .keys()返回一个列表
> 通过sorted（） 对 字典进行排序
```
for k in sorted(alien_0.keys()):
```

### 6 字典重复项 set（） 去除
```
for value in set(alien_0.values()):
```

### 7  迭代 value
* 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
* 如果要同时迭代key和value，可以用for k, v in d.items()。


### 6嵌套
#### 1 包含字典的列表
```python
#产生不同的外星人
alien_0={'color':'green','point':5}
alien_1={'color':'red','point':10}
alien_2={'color':'yellow','point':15}
aliens=[alien_0,alien_1,alien_2]
for i in aliens:
    print(i)
```

```python
#批量外星人
alien={'color':'green','point':5}
aliens=[]
for i in range(1,10):
    aliens.append(alien)
for i in aliens[-3:-1]:
    print(i)
print(len(aliens))
```
```python
#？？？？？？？？
aliens=[]
for i in range(1,10):
    alien1={'color':'green','point':5}###不能放在for外面？？？
    aliens.append(alien1)

#批量修改外星人
for alien in aliens[:1]:
    if alien['color']== 'green':
        alien['color']='blue'
        alien['point']= 2
    elif alien['color']=='red':
        alien['color']='xxx'
        alien['point']= 21
for alien in aliens[0:6]:
    print(alien)
```

#### 2 包含list 的dict（一个key 关联很多信息）
```python
information={
        'Name':'Liu Chuang',
        'Age':20,
        'School':['Haiwan','37th','Wuhan University'],
        'ideal':['Zhejiang','Peking'],
        }
print('Name: '+ information['Name']+ '\n')
print('Age:  '+ str(information['Age'])+ '\n')
print('\nSchool:')
for school in information['School']:
    print(school)
print('\nIdeal:')
for ideal in information['ideal']:
    print(ideal)
```
#### 3 字典嵌套字典
> * 登记学生信息 有很多学生  每个学生有几个信息

```python
cities={
        'Dalian':{
                'Location':'A+',
                'Environment':'A+',
                'consume':'B+'
                },
        'Hangzhou':{
                'Location':'A',
                'Environment':'A+',
                'consume':'A+'
                },
        'Shenzhen':{
                'Location':'A',
                'Environment':'A',
                'consume':'A+'
                },
        }

cities['Dalian']['Location']='A-' ## 修改字典中的Value
cities['DaLian']=cities.pop('Dalian')##修改字典的Key
for city,infor in cities.items():
    print('\n'+city +'  :')
    ##另一个字典
    for facter,rank in infor.items():
        print('\t'+facter +':  '+ rank)

```

-------

# 16 While 循环
### 1 单个事件控制循环退出
```python
while message!= 'quit'
```
### 2 多个事件导致停止  引入“标志”
```python
act=True
while act :
    message=input(prompt)
    if message == 'quit':
        act=False
    elif message == 'QUIT':
        act=False
    else:
        print(message)
```
### 3 break vs  continue
* break  跳出循环
* continue  忽略后面代码 从while 执行

-----------

# 17 异常
### try--except--else 模块
* 将可能引发异常的代码放入try语句  
* 在try成功执行的代码放入else 
* except 代码 对应错误类型 以及 引发错误该怎么办

--------

# 18  代码测试 unittest
> 运行测试实例时，完成一个测试单元，python打印一个字符：
* 通过一个测试，打印一个句点；
* 测试引发错误时，打印一个E，
* 测试导致断言失败时候 打印一个F。

### 1  测试函数

### 2 测试类
* 断言方法


| 方法      | 用途 |  
| --------   | -----:  | 
| assertEqual(a,b)   | a==b |  
| assertTrue(x)        |   x为True   |  
| assertIn(item,list)       |    核实item在list中    | 
| assertNotEqual(a,b)   | a!=b |  
| assertFalse(x)        |   x为False   |  
| assertNotIn(item,list)       |    核实item不在list中    | 

----------


