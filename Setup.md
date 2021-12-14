

## Інсталяція



В порожній папці виконайте команду:

`git clone https://github.com/oleksii-nevmerzhytskiy/Car-park-REST-API.git`

Перейдіть в папку проекту:

`cd Car-park-REST-API`


Створіть віртуальне середовище:

Linux:

`python3 -m venv venv`

`source venv/bin/activate`

Windows

`python3 -m venv venv`

`.\venv\Scripts\activate.bat`



Виконайте команду:

`pip install -r requirements.txt `


Створіть міграцію:

`python manage.py makemigrations <ім'я міграції>`

Після генерації міграції треба актуалізувати структуру БД

`python manage.py migrate`

Створіть адміністратора:

`python manage.py createsuperuser`
### Запуск проекту
Для запуску треба виконати у директорії з проектом наступну команду:


`python manage.py runserver 8000`



## Запити для перевірки:

1. Вивід списку водіїв:

    http://localhost:8000/drivers/driver/


2. Вивід списку водіїв, які створені після 10-11-2021

    http://localhost:8000/drivers/driver/?created_at__gte=10-11-2021


3. Вивід списку водіїв, котрі створені до 16-11-2021:

    http://localhost:8000/drivers/driver/?created_at__lte=16-11-2021


5. Отримання інформації по певному водію:

    http://localhost:8000/drivers/driver/1/


6. Створення нового водія:

    http://localhost:8000/drivers/driver/


    Методом POST передати дані у форматі json:

        {
        "driver": 
            {
                "first_name": "test name",
                "last_name": "test last name"
            }
        }

7. Редагування водія:

    http://localhost:8000/drivers/driver/1/

    Методом PUT передати дані у форматі json:

        {
        "driver": 
            {
                "first_name": "test name 1"
            }
        }
8. Видалення водія:

    Виконати метод DELETE

    http://localhost:8000/drivers/driver/1/


9. Вивід списку машин:

    http://localhost:8000/vehicles/vehicle/


10. Вивід списку машин з водіями:

      http://localhost:8000/vehicles/vehicle/?with_drivers=yes


11. Вивід списку машин без водіїв:

    http://localhost:8000/vehicles/vehicle/?with_drivers=no


12. Отримання інформації по певній машині:

    http://localhost:8000/vehicles/vehicle/1/


13. Створення нової машини:

    http://localhost:8000/vehicles/vehicle/

    Методом POST передати дані у форматі json:
    

        {
        "vehicle": 
            {
                "driver_id": null,
                "make": "test make",
                "model": "test model",
                "plate_number": "XX 1111 XX"
            }
        }
14. Редагування машини:

    http://localhost:8000/vehicles/vehicle/1/

    Методом PUT передати дані у форматі json:


        {
        "vehicle": 
            {
                "plate_number": "XX 9999 XX"
            }
        }

15. Садимо водія в машину / висаджуємо водія з машини

    http://localhost:8000/vehicles/set_driver/1/

    Методом POST передати дані у форматі json:


        {
        "vehicle": 
            {
                "driver_id": 1
            }
        }
    або

        {
        "vehicle": 
            {
                "driver_id": null
            }
        }
16. Видалення машини:

    Виконати метод DELETE

    http://localhost:8000/vehicles/vehicle/1/


