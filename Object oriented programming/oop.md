<!--
 * @Author: error: git config user.name && git config user.email & please set dead value or install git
 * @Date: 2022-10-31 18:02:29
 * @LastEditors: error: git config user.name && git config user.email & please set dead value or install git
 * @LastEditTime: 2022-10-31 20:58:49
 * @FilePath: \筆記本\Object oriented programming\oop.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 物件導向課程筆記

[![python](https://img.shields.io/badge/Python--3776ab?style=plastic&logo=python)](https://www.python.org/)
[![numpy](https://img.shields.io/badge/Numpy--013243?style=plastic&logo=numpy)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/Pandas--150458?style=plastic&logo=pandas)](https://pandas.pydata.org/)
[![openCV](https://img.shields.io/badge/OpenCV--5c3ee8?style=plastic&logo=opencv)](https://opencv.org/)
[![tensorflow](https://img.shields.io/badge/Tensorflow--ff6f00?style=plastic&logo=tensorflow)](https://www.tensorflow.org/)
[![jupyter](https://img.shields.io/badge/Jupyter--f37626?style=plastic&logo=jupyter)](https://jupyter.org/)
[![vscode](https://img.shields.io/badge/VScode--007acc?style=plastic&logo=visual-studio-code)](https://code.visualstudio.com/)
[![markdown](https://img.shields.io/badge/Markdown--000000?style=plastic&logo=markdown)](https://www.markdownguide.org/)
[![GitHub](https://img.shields.io/badge/GitHub--181717?style=plastic&logo=github)](https://github.com/hibana2077/Notebook/blob/main/Object%20oriented%20programming/oop.md)

## Python運算

### 1. 數字運算

```python
# 數字運算
a = 10 + 3 # 加法 + (13)
b = 10 - 3 # 減法 - (7)
c = 10 * 3 # 乘法 * (30)
d = 10 / 3 # 除法 / (3.3333333333333335)
e = 10 // 3 # 整數除法 // (3)
f = 10 % 3 # 取餘數 % (1)
g = 10 ** 3 # 次方 ** (1000) 也可以用 pow(10, 3)
```

### 2. 字串運算

```python
# 字串運算
a = "Hello" + "World" # 字串相加 (HelloWorld)
b = "Hello" * 3 # 字串重複 (HelloHelloHello)
c = "Hello" * 3 + "World" # 字串重複 + 字串相加 (HelloHelloHelloWorld)
d = "Hello" * (3 + 3) # 字串重複 + 數字相加 (HelloHelloHelloHelloHelloHello)
```

### 3. 比較運算

```python
# 比較運算
a = 3 > 2 # 大於 (True)
b = 3 < 2 # 小於 (False)
c = 3 >= 2 # 大於等於 (True)
d = 3 <= 2 # 小於等於 (False)
e = 3 == 2 # 等於 (False)
f = 3 != 2 # 不等於 (True)
```

### 4. 邏輯運算

```python
# 邏輯運算
a = True and True # 且 (True)
b = True and False # 且 (False)
c = True or True # 或 (True)
d = True or False # 或 (True)
e = not True # 非 (False)
f = not False # 非 (True)
```

### 5. 位元運算

```python
# 位元運算
a = 0b0011 # 3
b = 0b0101 # 5
c = a & b # 位元且 (1) and
d = a | b # 位元或 (7) or
e = a ^ b # 位元互斥或 (6) xor
f = ~a # 位元非 (-4) not
g = a << 2 # 位元左移 (12) 左邊補0
h = a >> 2 # 位元右移 (0) 右邊補0
```

### 6. 身分運算

```python
# 身分運算
a = 1
b = 1.0
c = a is b # 身分運算 (False)
d = a is not b # 身分運算 (True)
```

### 7. 成員運算

```python
# 成員運算
a = [1, 2, 3, 4, 5]
b = 1 in a # 成員運算 (True)
c = 6 in a # 成員運算 (False)
d = 1 not in a # 成員運算 (False)
e = 6 not in a # 成員運算 (True)
```

## python串列讀取資料及性質

Python 串列是一種有序的資料結構，可以用來儲存多筆資料，並且可以透過索引值來存取資料，並且可以透過索引值來存取資料，索引值從 0 開始，也可以使用負數來存取資料，負數索引值從 -1 開始，-1 代表最後一筆資料，-2 代表倒數第二筆資料，以此類推。

### 1. 建立串列

```python
# 建立串列
a = [1, 2, 3, 4, 5]
b = ["Hello", "World"]
c = [1, "Hello", True] # 串列中可以放不同型態的資料
d = list() # 建立空串列
e = list("Hello") # 將字串轉換成串列 => ['H', 'e', 'l', 'l', 'o']
```

### 2. 串列的索引值

```python
# 串列的索引值
a = [1, 2, 3, 4, 5]
b = a[0] # 1
c = a[1] # 2
d = a[-1] # 5
e = a[-2] # 4
index_1 = a.index(1) # 0 取得值為 1 的索引值
index_2 = a.index(5) # 4 取得值為 5 的索引值
```

### 3. 串列的切片

>> 串列的切片可以用來取得串列中的部分資料，切片的語法為：串列名稱[起始索引值:結束索引值:間隔值]

```python
# 串列的切片
a = [1, 2, 3, 4, 5]
b = a[0:3] # [1, 2, 3] 取得索引值 0 到 3 的資料
c = a[1:4] # [2, 3, 4] 取得索引值 1 到 4 的資料
d = a[0:5:2] # [1, 3, 5] 取得索引值 0 到 5 的資料，間隔為 2
e = a[::2] # [1, 3, 5] 取得索引值 0 到 5 的資料，間隔為 2
f = a[::-1] # [5, 4, 3, 2, 1] 取得索引值 0 到 5 的資料，間隔為 -1
```

### 4. 串列的長度

```python
# 串列的長度
a = [1, 2, 3, 4, 5]
b = len(a) # 5 取得串列的長度
```

### 5. 串列的相加

```python
# 串列的相加
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = a + b # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 串列的相加
# 串列的相加可以用來將兩個串列合併成一個串列
```

### 6. 串列的相乘

```python
# 串列的相乘
a = [1, 2, 3, 4, 5]
b = a * 2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] 串列的相乘
# 串列的相乘可以用來將串列重複多次
```

### 7. 串列的修改

```python
# 串列的修改
a = [1, 2, 3, 4, 5]
a[0] = 10 # [10, 2, 3, 4, 5] 修改串列中的資料
a[1:3] = [20, 30] # [10, 20, 30, 4, 5] 修改串列中的資料
```

### 8. 串列的刪除

```python
# 串列的刪除
a = [1, 2, 3, 4, 5]
del a[0] # [2, 3, 4, 5] 刪除串列中的資料
del a[1:3] # [2, 5] 刪除串列中的資料
```

### 9. 串列的方法

```python
# 串列的方法
a = [1, 2, 3, 4, 5]
a.append(6) # [1, 2, 3, 4, 5, 6] 在串列的最後面新增資料
a.insert(0, 0) # [0, 1, 2, 3, 4, 5, 6] 在串列的指定位置新增資料
a.remove(0) # [1, 2, 3, 4, 5, 6] 刪除串列中的資料
a.pop() # [1, 2, 3, 4, 5] 刪除串列中的最後一筆資料
a.pop(0) # [2, 3, 4, 5] 刪除串列中的指定位置的資料
a.clear() # [] 清空串列中的資料
a = [1, 2, 3, 4, 5]
a.reverse() # [5, 4, 3, 2, 1] 將串列中的資料反轉
a = [1, 2, 3, 4, 5]
a.sort() # [1, 2, 3, 4, 5] 將串列中的資料由小到大排序
a.sort(reverse=True) # [5, 4, 3, 2, 1] 將串列中的資料由大到小排序
```

### 10. 串列的迭代

#### 10.1 for 迴圈

```python
# 串列的迭代
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
# 1
# 2
# 3
# 4
# 5
#或是使用
for i in range(len(a)):
    print(a[i])
```

#### 10.2 while 迴圈

```python
# 串列的迭代
a = [1, 2, 3, 4, 5]
i = 0
while i < len(a):
    print(a[i])
    i += 1
```

### 11. 串列的搜尋

```python
# 串列的搜尋
a = [1, 2, 3, 4, 5]
print(1 in a) # True 判斷串列中是否有指定的資料
print(6 in a) # False 判斷串列中是否有指定的資料
print(1 not in a) # False 判斷串列中是否沒有指定的資料
print(6 not in a) # True 判斷串列中是否沒有指定的資料
```

### 12. 串列的比較

```python
# 串列的比較
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = [1, 2, 3, 4, 6]
print(a == b) # True 比較兩個串列是否相等
print(a == c) # False 比較兩個串列是否相等
print(a != b) # False 比較兩個串列是否不相等
print(a != c) # True 比較兩個串列是否不相等
```

### 13. 其他

```python
# 其他
a = [i for i in range(20)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a = [i for i in range(20) if i % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
a = [[i * j for i in range(1, 10)] for j in range(1, 10)]
#產生九九乘法表的串列
```

## 字串

### 1. 字串的宣告

```python
# 字串的宣告
a = 'Hello World'
b = "Hello World"
c = '''Hello World'''
d = """Hello World"""
number = 123
number2Str = str(number)
```

### 2. 字串的運算

> 這一段的內容請參考[數值運算](#2-字串運算)

```python
# 字串的運算
a = 'Hello'
b = 'World'
print(a + b) # HelloWorld 字串的連接
print(a * 3) # HelloHelloHello 字串的重複
print(a[0]) # H 取得字串中的字元
print(a[0:3]) # Hel 取得字串中的字元
print(a[0:5:2]) # Hlo 取得字串中的字元
print(a[-1]) # o 取得字串中的字元
print(a[-5:-1]) # Hell 取得字串中的字元
```

### 3. 字串的方法

```python
# 字串的方法
a = 'Hello World'
print(a.upper()) # HELLO WORLD 將字串中的字母轉成大寫
print(a.lower()) # hello world 將字串中的字母轉成小寫
print(a.title()) # Hello World 將字串中的每個單字的第一個字母轉成大寫
print(a.capitalize()) # Hello world 將字串中的第一個字母轉成大寫
print(a.swapcase()) # hELLO wORLD 將字串中的大寫轉成小寫，小寫轉成大寫
print(a.count('l')) # 3 計算字串中指定字元出現的次數
print(a.find('l')) # 2 計算字串中指定字元出現的位置
print(a.find('l', 3)) # 3 計算字串中指定字元出現的位置，並指定從哪個位置開始計算
print(a.replace('l', 'L')) # HeLLo WorLd 將字串中指定的字元替換成另一個字元
```

### 4. 字串的格式化

```python
# 字串的格式化
a = 'Hello'
b = 'World'
name = 'John'
age = 20
print('%s %s %s %d' % (a, b, name, age)) # Hello World John 20
print('{} {} {} {}'.format(a, b, name, age)) # Hello World John 20
print('{0} {1} {2} {3}'.format(a, b, name, age)) # Hello World John 20
print('{3} {2} {1} {0}'.format(a, b, name, age)) # 20 John World Hello
print('{a} {b} {name} {age}'.format(a=a, b=b, name=name, age=age)) # Hello World John 20
print(f'{a} {b} {name} {age}') # Hello World John 20
```

### 5. 字串的比較

```python
# 字串的比較
a = 'Hello'
b = 'Hello'
c = 'hello'
print(a == b) # True 比較兩個字串是否相等
print(a == c) # False 比較兩個字串是否相等
print(a != b) # False 比較兩個字串是否不相等
print(a != c) # True 比較兩個字串是否不相等
```

### 6. 其他

```python
# 其他
a = 'Hello World'
print(a.split()) # ['Hello', 'World'] 將字串以空白分割成串列
print(a.split('o')) # ['Hell', ' W', 'rld'] 將字串以指定字元分割成串列
print(a.split('o', 1)) # ['Hell', ' World'] 將字串以指定字元分割成串列，並指定分割的次數
print(a.join('123')) # 1Hello World2Hello World3 將字串中的字元插入到指定字串中
print(a.join(['1', '2', '3'])) # 1Hello World2Hello World3 將字串中的字元插入到指定串列中
print(a.startswith('H')) # True 判斷字串是否以指定字元開頭
print(a.startswith('h')) # False 判斷字串是否以指定字元開頭
print(a.endswith('d')) # True 判斷字串是否以指定字元結尾
print(a.endswith('D')) # False 判斷字串是否以指定字元結尾
```

## Numpy 套件

### 1. 簡介

- numerical python
- 主要處理多維陣列的運算
- 應用於科學計算、機器學習、深度學習等領域
- 許多套件都是以 Numpy 為基礎 ( matplotlib, pandas, opencv-python, ...)

### 2. 安裝

```bash
#windows
pip install numpy
#mac and linux
pip3 install numpy
```

檢查是否安裝成功

```python
import numpy as np
print(np.__version__)
```

或是開啟 python shell

```bash
$python
>>> import numpy as np
>>> print(np.__version__)
```

### 3. 基本操作

```python
import numpy as np
# 建立一維陣列
a = np.array([1, 2, 3])
print(a) # [1 2 3]

# 建立二維陣列
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b) # [[1 2 3] [4 5 6]]

# shape 屬性 => 陣列的維度
print(a.shape) # (3,) 一維陣列
print(b.shape) # (2, 3) 二維陣列

# ndim 屬性 => 維度
print(a.ndim) # 1
print(b.ndim) # 2

# size 屬性 => 陣列中元素的個數
print(a.size) # 3
print(b.size) # 6

# dtype 屬性 => 陣列中元素的資料型態
print(a.dtype) # int32
print(b.dtype) # int32

# astype() 方法 => 轉換陣列中元素的資料型態
print(a.astype(np.float32)) # [1. 2. 3.]
print(b.astype(np.float32)) # [[1. 2. 3.] [4. 5. 6.]]
print(a.astype(np.float32).dtype) # float32
print(b.astype(np.float32).dtype) # float32

# reshape() 方法 => 改變陣列的維度
arr1 = np.arange(1,13)
print(arr1) # [ 1  2  3  4  5  6  7  8  9 10 11 12] => Vector
print(arr1.shape) # (11,)
print(arr1.reshape(3,4)) # [[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11]] => Matrix
print(arr1.reshape(3,4).shape) # (3, 4)
print(arr1.reshape(3,4).ndim) # 2
print(arr1.reshape(3,4).size) # 12
arr2 = np.arange(1,17)
print(arr2) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]
print(arr2.reshape(2,2,4)) # [[[ 1  2  3  4] [ 5  6  7  8]] [[ 9 10 11 12] [13 14 15 16]]] =>Tensor
#reshape(a:array_like , newshape:int或tuple的整数 , order = 'C'(C-style)或'F'(Fortran-style) )
#a:要重新形成的陣列
#newshape:新的形状应该与原始形状兼容。如果是整数，则结果将是该长度的1-D陣列。一个形状维度可以是-1。在这种情况下，从陣列的长度和其余维度推断该值。
#order = 'C' 案照C的方式读取陣列元素，'F' 按照Fortran的方式读取陣列元素。(其實還有'A'，但是不常用)
#這個方法不會改變原陣列的維度，只會回傳一個新的陣列，並且是產生的新陣列會與原陣列共用同一塊記憶體空間
#如果更改新陣列的元素，原陣列的元素也會跟著改變。

#sum() 方法 => 計算陣列中元素的總和
print(arr1.sum()) # 66

#mean() 方法 => 計算陣列中元素的平均值
print(arr1.mean()) # 6.0

#transpose() 方法 => 轉置矩陣
print(arr1.reshape(3,4)) # [[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11]]
print(arr1.reshape(3,4).transpose()) # [[ 1  5  9] [ 2  6 10] [ 3  7 11] [ 4  8 12]]
```

![img](https://media.discordapp.net/attachments/868759966431973416/1036597819554934844/unknown.png)

```python
# trace() 方法 => 計算矩陣的積
arr1 = np.arange(1,10).reshape(3,3)
print(arr1.trace()) # 15

# diag() 方法 => 計算矩陣的對角線元素
arr1 = np.arange(1,10).reshape(3,3)
print(np.diag(arr1)) # [1 5 9]

# flatten() 方法 => 將多維陣列轉換為一維陣列
arr1 = np.arange(1,10).reshape(3,3)
print(arr1.flatten()) # [1 2 3 4 5 6 7 8 9]

# linspace() 方法 => 建立等差陣列
arr1 = np.linspace(0,1,5)
print(arr1) # [0.   0.25 0.5  0.75 1.  ] => [起始值,結束值,元素個數] endpoints 是否包含結束值
#等差陣列的元素間距為 (結束值-起始值)/(元素個數-1)

# zeros() 方法 => 建立全為0的陣列
arr1 = np.zeros(5)
print(arr1) # [0. 0. 0. 0. 0.]

# ones() 方法 => 建立全為1的陣列
arr1 = np.ones(5)
print(arr1) # [1. 1. 1. 1. 1.]

# eye() 方法 => 建立單位矩陣
arr1 = np.eye(5)
print(arr1) 
# [
# [1. 0. 0. 0. 0.]
# [0. 1. 0. 0. 0.]
# [0. 0. 1. 0. 0.]
# [0. 0. 0. 1. 0.]
# [0. 0. 0. 0. 1.]
# ]

# vsplit() 方法 => 將陣列垂直分割
# hsplit() 方法 => 將陣列水平分割
# vstack() 方法 => 將陣列垂直堆疊
# hstack() 方法 => 將陣列水平堆疊
# copy() 方法 => 複製陣列
# sort() 方法 => 將陣列排序 (預設為升冪)
```

### 4. Slicing

```python
# 陣列切片
# 陣列切片的語法為 [起始索引:結束索引:步長]
# 起始索引與結束索引都是可選的，如果沒有指定，則預設為陣列的第一個元素與最後一個元素
# 步長也是可選的，如果沒有指定，則預設為1
# 步長可以是負數，這樣就可以從陣列的最後一個元素開始切片
a = np.arange(1,17).reshape(4,4)
print(a.shape) # (4, 4)
print(a[1:3,1:3]) # [[ 6  7] [10 11]]
print(a[1:3,1:3].shape) # (2, 2)
```

### 5. Broadcasting

```python
# 广播
# 广播是指当两个数组的维度不同时，NumPy会自动触发广播机制，使得两个数组的维度相同后再进行运算
# 广播机制只有在两个数组的最后一个维度的轴长度相符或其中一个为1时才会触发
# 广播机制的运算速度比循环运算要快得多
a = np.arange(1,17).reshape(4,4)
b = np.arange(1,5).reshape(4,1)
print(a+b)
# =a=
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]
# =b=
# [[1]
#  [2]
#  [3]
#  [4]]
# =a+b=
# [[ 2  3  4  5]
#  [ 7  8  9 10]
#  [12 13 14 15]
#  [17 18 19 20]]
```

### 6. Array Operations

```python
# 陣列運算
# 陣列運算的語法為 [運算子] [陣列1] [運算子] [陣列2]
# 陣列運算的運算子有 + - * / // % **
# 陣列運算的運算子也可以是 += -= *= /= //= %= **=
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
print(x+y) # [ 6  8 10 12]
print(x-y) # [-4 -4 -4 -4]
print(x*y) # [ 5 12 21 32]
print(x/y) # [0.2        0.33333333 0.42857143 0.5       ]
print(x//y) # [0 0 0 0]
print(x%y) # [1 2 3 4]
print(x**y) # [    1    64  2187 65536]
dot = np.dot(x,y) # 內積
print(dot) # 70
```

### 7. 檔案存取 (np.savetxt() & np.loadtxt())

```python
# 檔案存取
# np.savetxt() 方法 => 將陣列存成檔案
# np.savetxt() 方法的語法為 np.savetxt(檔案名稱, 陣列, 分隔符號, fmt)
# np.loadtxt() 方法 => 將檔案讀取成陣列
# np.loadtxt() 方法的語法為 np.loadtxt(檔案名稱, 分隔符號)
a = np.arange(1,17).reshape(4,4)
np.savetxt('a.csv', a, delimiter=',', fmt='%d') 
#會產生一個 a.csv 檔案 ， 並且用 , 分隔
b = np.loadtxt('a.csv', delimiter=',')
print(b)
# =a.csv=
# [[ 1.  2.  3.  4.]
#  [ 5.  6.  7.  8.]
#  [ 9. 10. 11. 12.]
#  [13. 14. 15. 16.]]
```

## 物件

在學習程式語言時，或多或少都有聽過物件導向程式設計(Object-oriented programming，簡稱OOP)，它是一個具有物件(Object)概念的開發方式，能夠提高軟體的重用性、擴充性及維護性，在開發大型的應用程式時更是被廣為使用，所以在現今多數的程式語言都有此種開發方式，Python當然也不例外。而要使用物件導向程式設計就必須對類別(Class)及物件(Object)等有一些基本的了解，包含了：

- 類別(Class)
- 物件(Object)
- 屬性(Attribute)
- 建構式(Constructor)
- 方法(Method)

### 1. 類別(Class)

```python
# 類別
class car:#car 是類別名稱
    def __init__(self, brand, color): #建構式 => __init__(self, 參數1, 參數2, ...)
        self.brand = brand
        self.color = color
    def drive(self): #方法 
        print('開車中')
    def stop(self): #方法
        print('停車中')
    def __str__(self): #方法 (超載) => print(物件) 時會執行此方法
        return '這是一輛' + self.color + '的' + self.brand + '車'
    def __del__(self): #方法 (超載) => del 物件 時會執行此方法
        print('物件已刪除')
        self.brand = None
        self.color = None
```

### 2. 物件(Object)

```python
# 物件
# 類別的實例化 => 類別名稱(參數1, 參數2, ...)
# 類別的實例化後會產生一個物件
# 類別的實例化後會執行建構式
# 類別的實例化後會執行 __init__(self, 參數1, 參數2, ...) 方法
toyota = car('toyota', 'red')#toyota 是物件名稱
honda = car('honda', 'blue')#honda 是物件名稱
McLaren = car('McLaren', 'black')#McLaren 是物件名稱
print(toyota) # 這是一輛red的toyota車
print(honda) # 這是一輛blue的honda車
toyota.drive() # 開車中
honda.stop() # 停車中
del toyota # 物件已刪除
del honda # 物件已刪除
```

### 3. 超載

```python
# 超載
# __str__(self) 方法 => print(物件) 時會執行此方法
# __del__(self) 方法 => del 物件 時會執行此方法
# __add__(self, other) 方法 => 物件 + 物件 時會執行此方法
# __sub__(self, other) 方法 => 物件 - 物件 時會執行此方法
# __mul__(self, other) 方法 => 物件 * 物件 時會執行此方法
# __truediv__(self, other) 方法 => 物件 / 物件 時會執行此方法
# __floordiv__(self, other) 方法 => 物件 // 物件 時會執行此方法
# __mod__(self, other) 方法 => 物件 % 物件 時會執行此方法
# __pow__(self, other) 方法 => 物件 ** 物件 時會執行此方法
# __and__(self, other) 方法 => 物件 & 物件 時會執行此方法
# __or__(self, other) 方法 => 物件 | 物件 時會執行此方法
# __xor__(self, other) 方法 => 物件 ^ 物件 時會執行此方法
# __lshift__(self, other) 方法 => 物件 << 物件 時會執行此方法
# __rshift__(self, other) 方法 => 物件 >> 物件 時會執行此方法
# __eq__(self, other) 方法 => 物件 == 物件 時會執行此方法
# __ne__(self, other) 方法 => 物件 != 物件 時會執行此方法
# __lt__(self, other) 方法 => 物件 < 物件 時會執行此方法
# __le__(self, other) 方法 => 物件 <= 物件 時會執行此方法
# __gt__(self, other) 方法 => 物件 > 物件 時會執行此方法
# __ge__(self, other) 方法 => 物件 >= 物件 時會執行此方法
# __getitem__(self, key) 方法 => 物件[key] 時會執行此方法
# __setitem__(self, key, value) 方法 => 物件[key] = value 時會執行此方法
# __delitem__(self, key) 方法 => del 物件[key] 時會執行此方法
# __len__(self) 方法 => len(物件) 時會執行此方法
# __contains__(self, item) 方法 => item in 物件 時會執行此方法
# __call__(self, *args, **kwargs) 方法 => 物件() 時會執行此方法
```

### 4. 物件特性 - 繼承 (inheritance)

![img](https://miro.medium.com/max/1400/1*HOqX57WiUVrlfrXYZT5yMA.png)

>簡單來說：繼承就像是生活中，子女繼承父母的財產一樣。

- 繼承的語法
    
    - class 子類別名稱(父類別名稱):

```python
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

class Son(Father):
    pass

class Daughter(Father):
    pass

# 建立物件
son = Son('小明', 20)
daughter = Daughter('小華', 18)
Son.show(son)
Daughter.show(daughter)
```

可以看到，子類沒有訂議 `__init__` 與 `show` 方法，但是可以直接使用父類的方法。

### 5. 物件特性 - 封裝 (encapsulation)

>簡單來說：隱藏程式實現細節只保留下接口，使程式容易模組化。

- 封裝的語法

```python
class class_name:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def public_method(self):
        print('public_method')
    def __private_method(self):
        print('private_method')
```
- 實作

```python
class Father:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age, self.money)
    def __private_method(self):
        print(f'爸爸的私房錢 {1200000} 元')

class Son(Father):
    def __init__(self, name, age, money):
        super().__init__(name, age, money)
    def show(self):
        print(self.name, self.age, self.money)
    def __private_method(self):
        print(f'儲蓄 {self.money} 元')

if __name__ == '__main__':
    son = Son('小明', 20, 100000)
    son.show()
    son.__private_method()# 會出現錯誤
    son._Son__private_method()# 這樣才能呼叫
```

### 6. 物件特性 - 多型 (polymorphism)

>簡單來說：多型就是同一個方法，不同的物件會有不同的實現。

- 多型的語法

```python
class classname01:
    def method(self):
        print('classname01')

class classname02:
    def method(self):
        print('classname02')

class classname03:
    def method(self):
        print('classname03')

```

- 實作

```python
class worker:
    def work(self):
        print('工作')

class andy(worker):
    def work(self):
        print('andy 工作')

class bob(worker):
    def work(self):
        print('bob 工作')

worker = worker()
andy = andy()
bob = bob()

worker.work()
andy.work()
bob.work()
```

其中考範圍到這裡，下面的範圍應該是期末考範圍。

***

### 7. 物件方法 - 抽象方法 (abstract)

>概念：抽象類別是一種特殊的類別，它不能被實例化，只能被繼承。

- 抽象的語法

```python
from abc import ABCMeta, abstractmethod

class classname(metaclass=ABCMeta):
    @abstractmethod
    def method(self): # 抽象方法
        pass
```

- 實作

```python
from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: " + self.title + "\nAuthor: " + self.author + "\nPrice: " + str(self.price))


title = 'Im Westen nichts Neues'
author = 'Ernst Jünger'
price = 29
new_novel = MyBook(title, author, price)
new_novel.display()
title = 'The Catcher in the Rye'
author = 'J. D. Salinger'
price = 21
new_novel = MyBook(title, author, price)
new_novel.display()
```

- 實際上就是把 `display` 方法設定為抽象方法，這樣就不能實例化 `Book` 類別，但是可以建立子類別去繼承 `Book` 抽象方法。

### 8. 物件方法 - 靜態方法 (static)

>概念：靜態方法不需要實例化，可以直接使用類別名稱呼叫。

- 靜態方法的語法

```python
class classname:
    @staticmethod
    def method():
        pass
```

- 實作

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def welcome():
        print('歡迎來到書店')
    
    def display(self):
        print("Title: " + self.title + "\nAuthor: " + self.author)

Book.welcome() # 這樣就可以直接呼叫

title = 'The Alchemist'
author = 'Paulo Coelho'
new_novel = Book(title, author)
new_novel.display() # 這樣也可以呼叫，但是必須要實例化
```

### 9. 物件方法 - 類別方法 (class)

>概念：類別方法不需要實例化，可以直接使用類別名稱呼叫。
>不過類別方法必須要有參數 `cls`，並且要在方法裡面使用 `cls`。

- 類別方法的語法

```python
class classname:
    @classmethod
    def method(cls):
        pass
```

- 實作

```python
class Book:
    def __init__(self):
        pass

    @classmethod
    def empty_book(cls):
        print('這是一本空書')
        cls().display('空書', '空書')

    def display(self, title, author):
        print(f'書名：{title}，作者：{author}')

if __name__ == '__main__':
    Book.empty_book()
    book1 = Book()
    book1.display('Thinking, Fast and Slow', 'Daniel Kahneman')
```

</br>

***
到這裡就把物件導向的基礎語法介紹完畢，接下來是教 Tensorflow 的使用，跟實作一些簡單的 classifier 。
***
