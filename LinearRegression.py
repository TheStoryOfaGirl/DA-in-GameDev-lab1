import numpy as np
import gspread
gc = gspread.service_account(filename='linearregression-365018-a1b5fc7c4914.json')
sh = gc.open("LinearRegressionUnity")

x = [3, 21, 22, 34, 54, 34, 55, 67, 89, 99]
x = np.array(x)
y = [2, 22, 24, 65, 79, 82, 55, 130, 150, 199]
y = np.array(y)


def model(a, b, x):
    return a * x + b


def lossFunction(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    return (0.5 / num) * (np.square(prediction - y)).sum()


def optimize(a, b, x, y, Lr):
    num = len(x)
    prediction = model(a, b, x)
    da = (1.0 / num) * ((prediction - y) * x).sum()
    db = (1.0 / num) * ((prediction - y).sum())
    a -= Lr * da
    b -= Lr * db
    return a, b


def iterate(a, b, x, y, times, Lr):
    for i in range(times):
        a, b = optimize(a, b, x, y, Lr)
    return a, b


a = np.random.rand(1)
b = np.random.rand(1)
Lr = 0.0001
a, b = iterate(a, b, x, y, 100, Lr)
prediction = model(a, b, x)
loss = lossFunction(a, b, x, y)
for i in range(len(x)):
    newY = float(model(a, b, x[i]))
    sh.sheet1.update(('A' + str(i + 1)), str(i + 1))
    sh.sheet1.update(('B' + str(i + 1)), str(x[i]).replace('.', ','))
    sh.sheet1.update(('C' + str(i + 1)), str(y[i]).replace('.', ','))
    sh.sheet1.update(('D' + str(i + 1)), str(newY).replace('.', ','))
    sh.sheet1.update(('E' + str(i + 1)), str(abs(y[i] - newY)).replace('.', ','))
    print(str(abs(y[i] - newY)).replace('.', ','))
