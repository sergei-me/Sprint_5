# QA Sprint_5 Project

Автоматизация тестирования веб-приложения [QA Desk](https://qa-desk.stand.praktikum-services.ru/) с использованием **Selenium**, **Python** и **pytest**.

---

## 🔹 Функционал

- Авторизация и регистрация пользователей
- Создание и удаление объявлений
- Проверка корректности работы форм
- Работа с локаторами элементов страницы

---

## 🔹 Структура проекта

```
├── tests/ # Тесты
│ ├── test_create_ad.py
│ ├── test_login.py
│ ├── test_logout.py
│ └── test_registration.py
├── locators/ # Локаторы элементов
│ ├── ad_locators.py
│ ├── base_locators.py
│ ├── login_locators.py
│ ├── logout_locators.py
│ └── registration_locators.py
├── config.py # переменные URL
├── conftest.py # Фикстуры
├── requirements.txt # Зависимости проекта
├── .gitignore
└── README.md # Документация
```

---

## 🔹 Ветки

- **main** – только README.md и стабильные релизы
- **develop** – вся остальная разработка и тесты


Автор: Сергей Межов

Email: mezhov@mail.ru