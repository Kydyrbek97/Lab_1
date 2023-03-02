## Старт

#### 1) Склонить проект
    Команда: git clone https://github.com/Kydyrbek97/Lab_1.git

#### 2) Cоздать виртуальную окружение
    Команда: python3 -m venv venv

#### 3) Активировать виртуальную окружению

    Команда: source venv/bin/activate

#### 4) Скачать библиотеки
    Команда: pip install -r requirements.txt

#### 5) Создать базу данных 
    Команда: CREATE DATABASE lab; 

#### 6) Запустить parsing.py
    Команда: python3 parsing.py

#### 7) Запустить main.py 
    Команда: python3 main.py

#### 8) Команда для экспорта в SQL
    Команда: pg_dump -U postgres -h localhost lab > homes.sql
