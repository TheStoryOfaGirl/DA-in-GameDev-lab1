# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #5 выполнил(а):
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
Осуществить интеграцию экономической системы в проект Unity и обучить ML-Agent.

## Задание 1
### Изменить параметры файла yaml-агента и определить какие параметры и как влияют на обучение модели.

- Открыла проект Unity, добавила в проект ml-agents-release_19. Запустила проект и ознакомилась с его работой.
![2022-11-30](https://user-images.githubusercontent.com/106344305/204775937-e355d2c8-4f01-4033-b1fa-ce9408654b8d.png)
- Запустила Anaconda Prompt. Создала и активировала виртуальное пространство. Запустила сцену в Unity и обучение ML-Агента.

![image](https://user-images.githubusercontent.com/106344305/204784917-95bb790a-3a03-417d-8916-86edfe810bf9.png)

- Осуществилось обучение модели.
![image](https://user-images.githubusercontent.com/106344305/204785845-656358bb-8178-44df-9b14-a09838596079.png)
![image](https://user-images.githubusercontent.com/106344305/204788606-3ffbd2d9-ccf8-4d73-bd55-b9f99f164833.png)
- Результаты обучения модели были успешно сохранены.
![image](https://user-images.githubusercontent.com/106344305/204788741-e630ffd7-8303-40d8-8693-abd4769c238e.png)
- Построила графики для оценки результатов обучения в TensorBoard.
![image](https://user-images.githubusercontent.com/106344305/204803703-d7b4bafb-45f5-4cfc-906d-bbec0d735750.png)
- Изменила параметр strength, задав ему значение 5 (было 1).

![image](https://user-images.githubusercontent.com/106344305/204804341-929d9fbf-e3bc-49e2-8272-4661726b4142.png)

- Изменила параметр gamma, задав ему значение 2 (было 0.99).

![image](https://user-images.githubusercontent.com/106344305/204809956-bee2ffea-99e6-4c63-9e16-5418c2db7445.png)

- Изменила параметр batch_size, задав ему значение 500 (было 1024).

![image](https://user-images.githubusercontent.com/106344305/204811911-a42f881b-83dc-4790-9e4d-54cb0aac006a.png)

- Изменила параметр learning_rate, задав ему значение 2.0e-4 (было 3.0e-4).

![image](https://user-images.githubusercontent.com/106344305/204814033-ec1538cf-1dc2-480f-9a0f-344d456e3217.png)




## Задание 2
### Описать результаты, выведенные в TensorBoard. 



## Выводы

- В ходе данной работы я научилась работать с перцептроном. Были реализованы логические операции (OR, AND, NAND, XOR). Все операции, кроме XOR отработали корректно, для их обучения потребовалось небольшое количество эпох. Операцию XOR не удалось реализовать. Были построены графики зависимости количества эпох от ошибки обучения. Можно заметить, что для операции NAND потребовалось больше эпох для обучения, чем OR и AND. Также была построена визуальная модель работы перцептрона на сцене Unity, где наглядно через изменение цвета кубиков была показана операция AND.


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
