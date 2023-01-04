---
marp: true
theme: gaia
---
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

![W12](https://media.discordapp.net/attachments/868759966431973416/1060031986472845352/2023-01-04_11.08.30.png?width=1681&height=937)