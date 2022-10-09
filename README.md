# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #2 выполнил(а):
- Хмелёва Виктория Сергеевна
- РИ210942
Отметка о выполнении заданий (заполняется студентом):

| Задание | Выполнение | Баллы |
| ------ | ------ | ------ |
| Задание 1 | * | 60 |
| Задание 2 | * | 20 |
| Задание 3 | * | 20 |

знак "*" - задание выполнено; знак "#" - задание не выполнено;

Работу проверили:
- к.т.н., доцент Денисов Д.В.
- к.э.н., доцент Панов М.А.
- ст. преп., Фадеев В.О.

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Структура отчета

- Данные о работе: название работы, фио, группа, выполненные задания.
- Цель работы.
- Задание 1.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Задание 2.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Задание 3.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Выводы.
- ✨Magic ✨

## Цель работы
Познакомиться с программными средствами для организции передачи данных между инструментами google, Python и Unity.

## Задание 1
### Реализовать совместную работу и передачу данных в связке Python - Google-Sheets – Unity
#### В облачном сервисе google console подключить API для работы с google sheets и google drive.
- В google console добавила Google Sheets API и Google Drive API:  

![1](https://user-images.githubusercontent.com/106344305/194774842-9c4f42cd-934f-4429-8391-e41f8a17bd9f.PNG)
![2](https://user-images.githubusercontent.com/106344305/194774845-b6d65730-7a29-424c-93f0-df030c987cb0.PNG)

- Далее создала Service account, в котором был добавлен private key формата JSON (впоследствии будет добавлен в скрипт на python):

![3](https://user-images.githubusercontent.com/106344305/194774847-d9122807-c7f4-482e-b889-b527e030196c.PNG)
![4](https://user-images.githubusercontent.com/106344305/194774849-966ade46-0162-4dbe-aaf8-61916204b43f.PNG)

- Затем была создана таблица UnitySheets:
 ![6](https://user-images.githubusercontent.com/106344305/194774852-642cfcb4-e8a3-400e-9b81-1e4b0e4ebe2f.PNG)

- В созданном аккаунте в google console появился email адрес, который необходимо записать в настройки доступа таблицы UnitySheets:

![5](https://user-images.githubusercontent.com/106344305/194774851-5d25b6c2-abcc-4b16-88e9-c6fd7cccc41e.PNG)
![7](https://user-images.githubusercontent.com/106344305/194774854-adc07c6d-1dac-4adf-9260-fa9f2c8bb7e3.PNG)

#### Реализовать запись данных из скрипта на python в google-таблицу. Данные описывают изменение темпа инфляции на протяжении 11 отсчётных периодов, с учётом стоимости игрового объекта в каждый период.
- В PyCharm был реализован скрипт по изменению темпа инфляции на протяжении 11 отсчётных периодов, с учётом стоимости игрового объекта в каждый период. Была добавлена привязка к таблице UnitySheets через JSON файл и название таблицы.

![8](https://user-images.githubusercontent.com/106344305/194775286-f8962949-a900-44cc-93c5-960811615743.PNG)

![9](https://user-images.githubusercontent.com/106344305/194775292-12322344-50f3-409a-b542-91f7fe4bb1a5.PNG)

#### Создать новый проект на Unity, который будет получать данные из google-таблицы, в которую были записаны данные в предыдущем пункте.
- В Unity был создан проект UnityDataScience, в который были импортированы два пакета - jsonPackage и soundPackage. Был добавлен GameObject, к которому необходимо было привязать компонент Audio Source. Затем для выгрузки данных из таблицы был написан скрипт.

![11](https://user-images.githubusercontent.com/106344305/194775638-81288a5b-f24b-4801-8e38-4057209e10c5.PNG)

#### Написать функционал на Unity, в котором будет воспризводиться аудио-файл в зависимости от значения данных из таблицы.
- В скрипте для выгрузки данных из таблицы UnitySheets был реализован код для воспризводения аудио-файла в зависимости от значения данных из таблицы. Затем скрипт был привязан к GameObject, в поля звуков записаны соответствующие звуки из папки Sound. В результате из скрипта на Python данные выгружались в таблицу UnitySheets, а в Unity данные брались из таблицы. Исходя из полученных данных в проекте в Unity воспроизводятся 11 звуков.

![10](https://user-images.githubusercontent.com/106344305/194776076-b1268329-f458-40ef-8f22-6e25e3df278f.PNG)

![2022-10-09 (23)](https://user-images.githubusercontent.com/106344305/194776103-eb8239df-8bc2-446d-b6e1-320ca7d89179.png)
![2022-10-09 (25)](https://user-images.githubusercontent.com/106344305/194776113-9dfe55ea-9db7-4150-abb4-ca084fd35074.png)

## Задание 2
### Пошагово выполнить каждый пункт раздела "ход работы" с описанием и примерами реализации задач
Ход работы:
- Произвести подготовку данных для работы с алгоритмом линейной регрессии. 10 видов данных были установлены случайным образом, и данные находились в линейной зависимости. Данные преобразуются в формат массива, чтобы их можно было вычислить напрямую при использовании умножения и сложения.

```py

#Import the required modules, numpy for calculation, and Matplotlib for drawing
import numpy as np
import matplotlib.pyplot as plt

# define data, and change list to array
x = [3,21,22,34,54,34,55,67,89,99]
x = np.array(x)
y = [2,22,24,65,79,82,55,130,150,199]
y = np.array(y)

#Show the effect of a scatter plot
plt.scatter(x,y)

```

![4](https://user-images.githubusercontent.com/106344305/192151632-22da9929-38a1-4095-8404-60666c9d2bdd.png)


- Определите связанные функции. Функция модели: определяет модель линейной регрессии wx+b. Функция потерь: функция потерь среднеквадратичной ошибки. Функция оптимизации: метод градиентного спуска для нахождения частных производных w и b.

Функция модели:
```py

def model(a, b, x):
    return a * x + b
    
```    

Функция потерь:
```py

def lossFunction(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    return (0.5 / num) * (np.square(prediction - y)).sum()

```
Функция оптимизации:
```py

def optimize(a, b, x, y, Lr):
    num = len(x)
    prediction = model(a, b, x)
    da = (1.0 / num) * ((prediction - y) * x).sum()
    db = (1.0 / num) * ((prediction - y).sum())
    a = a - Lr * da
    b = b - Lr * db
    return a, b
    
```

![5](https://user-images.githubusercontent.com/106344305/192151756-59aedcdd-f78c-4d5e-86e4-1fabc5e3711a.png)


Итерация:

![6](https://user-images.githubusercontent.com/106344305/192151773-1c6c649c-e916-45f5-9b32-fe9acaed6495.png)


## Задание 3
### Должна ли величина loss стремиться к нулю при изменении исходных данных? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ.

Величина loss будет стремиться к нулю при изменении исходных данных. К примеру, при увеличении количества итераций величина loss будет становиться меньше, т.е. стремиться к нулю.

При количестве итераций 10 величина loss равна примерно 1671:

![7](https://user-images.githubusercontent.com/106344305/192151812-ec54d542-1f06-424e-81f9-a1081dbb0961.png)

При количестве итераций 100 величина loss равна примерно 1295:

![8](https://user-images.githubusercontent.com/106344305/192151830-ae3c8d6a-db35-4736-926c-b472361fef55.png)

При количестве итераций 10000 величина loss равна примерно 191:

![9](https://user-images.githubusercontent.com/106344305/192151853-f05c9714-30ff-4784-ba4a-d666b36e076d.png)

### Какова роль параметра Lr? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ. В качестве эксперимента можете изменить значение параметра.

Параметр Lr влияет на угол наклона графика. Чем меньше параметр, тем наклон графика больше.

Значение параметра Lr равно 0.000001:

![10](https://user-images.githubusercontent.com/106344305/192151916-41175b47-c3f3-4231-bfb2-e46d05f39a1d.png)

Значение параметра Lr равно 0.00001:

![11](https://user-images.githubusercontent.com/106344305/192151952-3178f34e-b5a5-4bfc-8ad5-175ef1979098.png)

Значение параметра Lr равно 0.0001:

![12](https://user-images.githubusercontent.com/106344305/192151959-8a7d72bb-0cbe-4a2a-84db-4322206088be.png)

## Выводы

В ходе данной работы были написаны программы в среде Unity, a также PyCharm.
Я познакомилась с алгоритмом линейной регрессии, осуществила функции модели, потерь и оптимизации.  Также были проведены эксперименты с различными исходными данными и выявлены зависимости и закономерности.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Powered by

**BigDigital Team: Denisov | Fadeev | Panov**
