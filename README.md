# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #3 выполнил(а):
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
Познакомиться с программными средствами для создания системы машинного обучения и ее интеграции в Unity.

## Задание 1
### Реализовать систему машинного обучения в связке Python - Google-Sheets – Unity. При выполнении задания можно использовать видео-материалы и исходные данные, предоставленные преподавателями курса.
- Создала новый пустой 3D проект на Unity.
- Скачала папку с ML агентом. В созданный проект добавила ML Agent, выбрав Window - Package Manager - Add Package from disk. Последовательно добавила .json – файлы:

![13](https://user-images.githubusercontent.com/106344305/197362879-68eb8e6f-8bc8-4413-8a02-6c6a52aea588.PNG)

- Во вкладке с компонентами (Components) внутри Unity появилась строка ML Agent.
- Далее запустила Anaconda Prompt для возможности запуска команд через консоль.
- Далее написала необходимые команды для создания и активации нового ML-агента, а также для скачивания необходимых библиотек:

![1](https://user-images.githubusercontent.com/106344305/197362937-aa50af1d-b768-4f85-8fd2-682e7dca308c.PNG)
![2](https://user-images.githubusercontent.com/106344305/197362938-141d3314-5fb5-4973-94cb-0e1abcf5b759.PNG)
![3](https://user-images.githubusercontent.com/106344305/197362941-51c2bf9c-f51d-4cbc-ba49-dfee529c4e13.PNG)

- Создала на сцене плоскость, куб и сферу. Создала C# скрипт-файл и подключила его к сфере:

![4](https://user-images.githubusercontent.com/106344305/197363035-81702a45-0bb4-47b0-82b5-0a6d109c470f.PNG)

Скрипт:

```C#

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;

public class RollerAgent : Agent
{
    Rigidbody rBody;
    // Start is called before the first frame update
    void Start()
    {
        rBody = GetComponent<Rigidbody>();
    }

    public Transform Target;
    public override void OnEpisodeBegin()
    {
        if (this.transform.localPosition.y < 0)
        {
            this.rBody.angularVelocity = Vector3.zero;
            this.rBody.velocity = Vector3.zero;
            this.transform.localPosition = new Vector3(0, 0.5f, 0);
        }

        Target.localPosition = new Vector3(Random.value * 8-4, 0.5f, Random.value * 8-4);
    }
    public override void CollectObservations(VectorSensor sensor)
    {
        sensor.AddObservation(Target.localPosition);
        sensor.AddObservation(this.transform.localPosition);
        sensor.AddObservation(rBody.velocity.x);
        sensor.AddObservation(rBody.velocity.z);
    }
    public float forceMultiplier = 10;
    public override void OnActionReceived(ActionBuffers actionBuffers)
    {
        Vector3 controlSignal = Vector3.zero;
        controlSignal.x = actionBuffers.ContinuousActions[0];
        controlSignal.z = actionBuffers.ContinuousActions[1];
        rBody.AddForce(controlSignal * forceMultiplier);

        float distanceToTarget = Vector3.Distance(this.transform.localPosition, Target.localPosition);

        if(distanceToTarget < 1.42f)
        {
            SetReward(1.0f);
            EndEpisode();
        }
        else if (this.transform.localPosition.y < 0)
        {
            EndEpisode();
        }
    }
}


```
- Объекту «сфера» добавила компоненты Decision Requester, Behavior Parameters, Rigidbody 

## Задание 2
### Пошагово выполнить каждый пункт раздела "ход работы" с описанием и примерами реализации задач
Ход работы:
- Произвести подготовку данных для работы с алгоритмом линейной регрессии. 10 видов данных были установлены случайным образом, и данные находились в линейной зависимости. Данные преобразуются в формат массива, чтобы их можно было вычислить напрямую при использовании умножения и сложения.



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
