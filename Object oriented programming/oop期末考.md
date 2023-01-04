# OOP 期末考筆記

# Week 9

![W9](https://media.discordapp.net/attachments/868759966431973416/1060030421133439099/2023-01-04_11.02.12.png?width=1679&height=937)

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

進階寫法：

```python
def T(self):
    return list(map(list, zip(*self.matrix)))
```