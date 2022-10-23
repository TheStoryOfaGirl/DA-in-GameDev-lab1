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
- Объекту «сфера» добавила компоненты Decision Requester, Behavior Parameters, Rigidbody и произвела их настройку.

![5](https://user-images.githubusercontent.com/106344305/197363242-ef8f7069-0a49-4379-b9be-19961d4f6b6e.PNG)

- В корень проекта добавила файл конфигурации нейронной сети: 
```yaml
behaviors:
  RollerBall:
    trainer_type: ppo
    hyperparameters:
      batch_size: 10
      buffer_size: 100
      learning_rate: 3.0e-4
      beta: 5.0e-4
      epsilon: 0.2
      lambd: 0.99
      num_epoch: 3
      learning_rate_schedule: linear
    network_settings:
      normalize: false
      hidden_units: 128
      num_layers: 2
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 1.0
    max_steps: 500000
    time_horizon: 64
    summary_freq: 10000
```
- Запустила работу ml-агента:

![7](https://user-images.githubusercontent.com/106344305/197363365-b7e68d76-91be-4d2a-af80-bc0e6b10375b.PNG)
![8](https://user-images.githubusercontent.com/106344305/197363367-1e57d5c4-2790-43c9-bf3a-804a8ee406a0.PNG)

- Сделала 3, 9, 27 копий модели «Плоскость-Сфера-Куб», запустила симуляцию сцены и проследила за результатом обучения модели:

![9](https://user-images.githubusercontent.com/106344305/197363416-4c87a6f9-8f32-4b06-9b1d-7e5a0688fa19.PNG)
![10](https://user-images.githubusercontent.com/106344305/197363417-427a0c35-beaf-4be6-9dde-08cc22c501db.PNG)
![11](https://user-images.githubusercontent.com/106344305/197363420-a5ca17b8-483a-4f9d-b0c3-ae9a0be8576c.PNG)

- После завершения обучения проверила работу модели:

![12](https://user-images.githubusercontent.com/106344305/197363489-ef25b798-18ff-425e-ad6f-f79bab3b75b7.PNG)

- Выводы: В результате обучения полученная модель шара катилась за кубом более плавно и быстрее находила куб, чем в процессе обучения. Также в начале обучения шар мог укатиться за пределы пола, чего не наблюдалось после обучения.

## Задание 2
### Подробно опишите каждую строку файла конфигурации нейронной сети, доступного в папке с файлами проекта по ссылке. Самостоятельно найдите информацию о компонентах Decision Requester, Behavior Parameters, добавленных сфере.
- Конфигурация нейронной сети. Задается поведение шара.
```
behaviors:
  RollerBall:
  ...
```
Задаем тип используемого тренажера по умолчанию.
```
trainer_type: ppo
```
Задаем гиперпараметры.
```
 hyperparameters:
```
Задаем количество опытов (10) на каждой итерации градиентного спуска.
```
batch_size: 10
```
Задаем количество опытов, которые необходимо собрать перед обновлением модели политики. Соответствует тому, сколько опытов должно быть собрано, прежде чем мы начнем какое-либо изучение или обновление модели.
```
buffer_size: 100
```
Задаем начальную скорость обучения для градиентного спуска. Соответствует силе каждого шага обновления градиентного спуска. 
```
learning_rate: 3.0e-4
```
Задаем силу регуляризации энтропии, которая делает политику "более случайной". Это гарантирует, что агенты должным образом исследуют пространство действий во время обучения. 
```
beta: 5.0e-4
```
Параметр влияет на то, насколько быстро политика может развиваться во время обучения. Соответствует допустимому порогу расхождения между старой и новой политиками при обновлении градиентного спуска. 
```
epsilon: 0.2
```
Задаем параметр регуляризации, используемый при вычислении обобщенной оценки преимуществ (GAE). Это можно рассматривать как то, насколько агент полагается на свою текущую оценку стоимости при вычислении обновленной оценки стоимости.
```
lambd: 0.99
```
Задаем количество проходов через буфер опыта при выполнении оптимизации градиентного спуска.
```
num_epoch: 3
```
Определяет, как скорость обучения изменяется с течением времени.
```
learning_rate_schedule: linear
```
Задаем сетевые настройки.
```
network_settings:
```
Параметр определяет, применяется ли нормализация к входным данным векторного наблюдения. В данном случае нет.
```
normalize: false
```
Задаем количество единиц в скрытых слоях нейронной сети. Соответствуют количеству единиц в каждом полностью подключенном слое нейронной сети.
```
hidden_units: 128
```
Задаем количество скрытых слоев в нейронной сети. Соответствует тому, сколько скрытых слоев присутствует после ввода наблюдения или после кодирования CNN визуального наблюдения. 
```
num_layers: 2
```
Задаем сигналы о вознаграждениии.
```
reward_signals:
```
Задаем внешние награды.
```
extrinsic:
```
Задаем коэффициент скидки для будущих вознаграждений, поступающих из среды. Это можно рассматривать как то, насколько далеко в будущем агент должен заботиться о возможных вознаграждениях.
```
gamma: 0.99
```
Задаем коэффициент, на который умножается вознаграждение, предоставляемое средой.
```
strength: 1.0
```
Задаем общее количество шагов (т.е. собранных наблюдений и предпринятых действий), которые должны быть выполнены в среде до завершения процесса обучения.
```
max_steps: 500000
```
Задаем параметр, определяющий, сколько шагов опыта нужно собрать для каждого агента, прежде чем добавлять его в буфер опыта. Когда этот предел достигается по окончании эпизода, оценка стоимости используется для прогнозирования общего ожидаемого вознаграждения от текущего состояния агента.
```
time_horizon: 64
```
Задаем количество опытов, которое необходимо собрать перед созданием и отображением статистики обучения. 
```
summary_freq: 10000
```

## Задание 3
### Доработайте сцену и обучите ML-Agent таким образом, чтобы шар перемещался между двумя кубами разного цвета. Кубы должны, как и впервом задании, случайно изменять кооринаты на плоскости. 



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
