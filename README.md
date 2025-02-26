# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #4 выполнил(а):
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
Познакомиться с работой перцептрона.

## Задание 1
### В проекте Unity реализовать перцептрон, который умеет производить различные вычисления.
- В сцене был создан пустой объект и привязан к нему скрпит реализации перцептрона.
![2022-11-27](https://user-images.githubusercontent.com/106344305/204128271-e1f67e22-6e23-4435-bc6f-d2f4b0f85ddc.png)

- Ввела значения для реализации операции OR.
![2022-11-27 (1)](https://user-images.githubusercontent.com/106344305/204128657-6447f715-ea5f-4397-865b-9cbf81a8a448.png)
- Обучила перцептрон вычислять операцию OR. Для обучения хватило 3 эпох, чтобы при прохождении тестов были получены верные результаты вычислений. 
![image](https://user-images.githubusercontent.com/106344305/204129126-5440b601-eeeb-4e04-bb02-17cedbcf06d7.png)
- Ввела значения для реализации операции AND. Обучила перцептрон вычислять операцию AND. Для обучения хватило 4 эпохи, чтобы при прохождении тестов были получены верные результаты вычислений. 
![image](https://user-images.githubusercontent.com/106344305/204129247-74696c90-02f3-44eb-82fb-ef65a5ac4a7b.png)
- Ввела значения для реализации операции NAND. Обучила перцептрон вычислять операцию NAND. Для обучения хватило 6 эпох, чтобы при прохождении тестов были получены верные результаты вычислений. 
![image](https://user-images.githubusercontent.com/106344305/204129389-70fdf805-ed90-4f67-be6d-deb151b2f981.png)
- Ввела значения для реализации операции XOR. Попробовала обучить перцептрон вычислять операцию XOR, однако даже при большом количестве эпох (100) не удалось добиться верных результатов вычислений. Алгоритм работает некорректно.
![image](https://user-images.githubusercontent.com/106344305/204129652-aaef94e5-f4c5-4ea1-ac43-82c2dc197c40.png)



## Задание 2
### Построить графики зависимости количества эпох от ошибки обучения. Указать от чего зависит необходимое количество эпох обучения

![image](https://user-images.githubusercontent.com/106344305/204130493-bf86293c-0b98-48ab-88c2-559497d0d7c1.png)

- Количество эпох обучения зависит от смещения (bias) и веса (weight).

## Задание 3
### Построить визуальную модель работы перцептрона на сцене Unity.
- Построила визуальную модель работы перцептрона, реализовав функцию AND. В результате кубики меняют свой цвет в соответствии с выбранной операцией. Черные кубики отвечают за 1, белые - за 0.
![image](https://user-images.githubusercontent.com/106344305/204132291-dc61489d-45dd-4b62-a079-3056edd890e3.png)
- Для изменения цвета кубиков согласно операции AND был добавлен представленный ниже скрипт.
```cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeColor : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.GetComponent<Renderer>().material.color == Color.black && this.gameObject.GetComponent<Renderer>().material.color == Color.black)
        {
            other.gameObject.GetComponent<Renderer>().material.color = Color.black;
            this.gameObject.GetComponent<Renderer>().material.color = Color.black;
        }
        else
        {
            other.gameObject.GetComponent<Renderer>().material.color = Color.white;
            this.gameObject.GetComponent<Renderer>().material.color = Color.white;
        }
    }
}
```

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
