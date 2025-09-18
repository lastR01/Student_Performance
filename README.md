# Анализ успеваемости студентов
Скрипт для генерации отчета по успеваемости студентов из CSV-файлов.  

## Описание
- Чтение одного или нескольких CSV-файлов с данными о студентах, предметах и оценках.
- Вычисление среднего балла для каждого студента.
- Сортировка студентов по убыванию среднего балла.
- Вывод отчёта в виде таблицы.

## Установка
1. Клонируйте репозиторий:
    ```
    git clone https://github.com/lastR01/Student_Performance.git
    ```

2. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
    Или
    ```
    pip install tabulate
    ```

## Запуск скрипта через командную строку:
Пример запуска с файлами в репозитории:
```
python main.py --files students1.csv students2.csv --report students-report
```
Пример запуска с вашими файлами:
```
python main.py --files <csv1> <csv2> ... --report students-report
```

## Запуск тестов
```
python -m unittest test_main.py
```

## Формат CSV файла:
```
student_name,subject,teacher_name,date,grade
Иванов Иван,Математика,Сидоров,2023-10-10,5
```