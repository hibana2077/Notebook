---
marp: true
theme: gaia
---
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg')-->
<!-- _class: lead -->

# OOP 期末考筆記


---

# Week 9

![W9](https://media.discordapp.net/attachments/868759966431973416/1060030421133439099/2023-01-04_11.02.12.png?width=850&height=500)

---

## 1. 概念

就只是實作一個方法，用來做矩陣轉置

## 2. 程式

基礎寫法：

```python
def T(self):
    new_matrix = []
    for i in range(len(self.matrix[0])):
        new_matrix.append([])
        for j in range(len(self.matrix)):
            new_matrix[i].append(self.matrix[j][i])
    return new_matrix
```

---

進階寫法：

```python
def T(self):
    return list(map(list, zip(*self.matrix)))
```

---

## 3. 說明

基礎寫法：

1. 先建立一個空的矩陣
2. 用兩個 for 迴圈，把原本的矩陣的每一個元素，依序放到新的矩陣中
3. 回傳新的矩陣

進階寫法：

1. 用 `zip` 把原本的矩陣轉置
2. 用 `map` 把 `zip` 後的結果，轉成 list
3. 回傳新的矩陣

---

# Week 12

![W12](https://media.discordapp.net/attachments/868759966431973416/1060031986472845352/2023-01-04_11.08.30.png?width=850&height=450)

---

## 1. 概念

這題用到繼承的概念，利用已經有的 `Circle` 類別，來建立 `Ellipse` 類別，並且新增成員屬性 長軸 `major_axis` 和 短軸 `minor_axis`，然後更新 `area` 的計算方式。

## 2. 程式

```python
class Ellipse(Circle):
    def __init__(self, cx,cy, major_axis, minor_axis):
        super().__init__(cx, cy, major_axis)
        self.minor_axis = minor_axis

    def area(self):
        return self.r * self.minor_axis * 3
```

---

## 3. 說明

1. `Ellipse` 繼承 `Circle`，所以 `Ellipse` 會繼承 `Circle` 的所有成員，然後把 `major_axis` 傳給 `Circle` 的 `__init__`，這樣就可以把 `major_axis` 設定成 `Circle` 的 `r`， 所以後續要計算 `area` 的時候，就可以直接用 `self.r` 來取得長軸的長度。
2. `Ellipse` 的 `area` 要重新計算，所以要把 `area` 的方法重新寫一次，這樣就可以覆蓋掉 `Circle` 的 `area` 方法。

---

# Week 14

![W14](https://media.discordapp.net/attachments/868759966431973416/1060037520668246016/2023-01-04_11.30.29.png?width=850&height=450)

---

## 1. 概念

在建立類別時，將 list 作為父類別，並在 `__init__` 方法中將傳入的參數初始化為向量。

---

## 2. 程式

```python
class Vector(list):
    def __init__(self, *args):
        super().__init__(*args)

    def dot(self, other):

        # 如果兩個向量的長度不同，則返回 ValueError
        if len(self) != len(other):
            raise ValueError("both vectors must have the same length")

        # 計算內積
        result = sum([a * b for a, b in zip(self, other)])
        return result
```

---

## 3. 說明

1. `Vector` 繼承 `list`，所以 `Vector` 會繼承 `list` 的所有成員，然後把 `*args` 傳給 `list` 的 `__init__`，這樣就可以把 `*args` 設定成 `Vector` 的成員。
2. `Vector` 的 `dot` 方法，用來計算內積，首先檢查兩個向量的長度是否相同，如果不同，則返回 `ValueError`，如果相同，則用 `zip` 把兩個向量的元素一一對應，然後用 `sum` 把兩個向量的元素相乘，最後回傳結果。

---

# Week 15

![W15](https://media.discordapp.net/attachments/868759966431973416/1060043273462358097/2023-01-04_11.53.19.png?width=850&height=450)

---

## 1. 概念

就只是把資料讀進來，然後做資料分割，如果用 `pandas` 會快一點，不知道老師考試時會不會有限制。

---

## 2. 程式

不使用套件

```python
with open("winequality-white.csv", "r") as f:
    data = f.read().splitlines()

data = list(map(lambda x: x.split(";"), data))
X = list(map(lambda x: x[:-1], data))
y = list(map(lambda x: x[-1], data))
```

---

使用 `pandas`

```python
import pandas as pd

df = pd.read_csv("winequality-white.csv", sep=";")
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
```

---

## 3. 說明

1. 使用 `with` 來讀取檔案，然後用 `splitlines` 把每一行分割成一個 list，然後用 `map` 把每一行的資料分割成一個 list，最後用 `list` 把 `map` 轉成 list。

2. 使用 `pandas` 讀取檔案，然後用 `iloc` 把資料分割成 `X` 和 `y`。

---

<!-- _class: lead -->
# The End
powered by [Marp](https://marp.app/)