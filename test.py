with open("winequality-white.csv", "r") as f:
    data = f.read().splitlines()

data = list(map(lambda x: x.split(";"), data))
X = list(map(lambda x: x[:-1], data))
y = list(map(lambda x: x[-1], data))
print(X)
print(y)