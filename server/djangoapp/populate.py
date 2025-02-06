from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN",
         "description": "Great cars. Japanese technology",
         "country": "Japan",
         "founded_year": 1933,
         "website": "https://www.nissan-global.com"},
        {"name": "Mercedes",
         "description": "Great cars. German technology",
         "country": "Germany",
         "founded_year": 1926,
         "website": "https://www.mercedes-benz.com"},
        {"name": "Audi",
         "description": "Great cars. German technology",
         "country": "Germany",
         "founded_year": 1909,
         "website": "https://www.audi.com"},
        {"name": "Kia",
         "description": "Great cars. Korean technology",
         "country": "South Korea",
         "founded_year": 1944,
         "website": "https://www.kia.com"},
        {"name": "Toyota",
         "description": "Great cars. Japanese technology",
         "country": "Japan",
         "founded_year": 1937,
         "website": "https://www.toyota-global.com"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'],
            description=data['description'],
            country=data['country'],
            founded_year=data['founded_year'],
            website=data['website']
        ))

    car_model_data = [
        {"name": "Pathfinder",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[0],
         "horsepower": 284,
         "color": "Red",
         "price": 32000.00,
         "transmission": "Automatic"},
        {"name": "Qashqai",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[0],
         "horsepower": 187,
         "color": "Blue",
         "price": 25000.00,
         "transmission": "Automatic"},
        {"name": "XTRAIL",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[0],
         "horsepower": 169,
         "color": "Green",
         "price": 27000.00,
         "transmission": "Manual"},
        {"name": "A-Class",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[1],
         "horsepower": 188,
         "color": "White",
         "price": 35000.00,
         "transmission": "Automatic"},
        {"name": "C-Class",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[1],
         "horsepower": 255,
         "color": "Black",
         "price": 40000.00,
         "transmission": "Manual"},
        {"name": "E-Class",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[1],
         "horsepower": 362,
         "color": "Silver",
         "price": 45000.00,
         "transmission": "Automatic"},
        {"name": "A4",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[2],
         "horsepower": 201,
         "color": "Red",
         "price": 30000.00,
         "transmission": "Manual"},
        {"name": "A5",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[2],
         "horsepower": 261,
         "color": "Blue",
         "price": 32000.00,
         "transmission": "Automatic"},
        {"name": "A6",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[2],
         "horsepower": 335,
         "color": "Green",
         "price": 38000.00,
         "transmission": "Automatic"},
        {"name": "Sorrento",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[3],
         "horsepower": 191,
         "color": "White",
         "price": 28000.00,
         "transmission": "Manual"},
        {"name": "Carnival",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[3],
         "horsepower": 290,
         "color": "Black",
         "price": 35000.00,
         "transmission": "Automatic"},
        {"name": "Cerato",
         "type": "Sedan",
         "year": 2023,
         "car_make": car_make_instances[3],
         "horsepower": 147,
         "color": "Silver",
         "price": 22000.00, "transmission": "Manual"},
        {"name": "Corolla",
         "type": "Sedan",
         "year": 2023,
         "car_make": car_make_instances[4],
         "horsepower": 139,
         "color": "Red",
         "price": 24000.00,
         "transmission": "Automatic"},
        {"name": "Camry",
         "type": "Sedan",
         "year": 2023,
         "car_make": car_make_instances[4],
         "horsepower": 203,
         "color": "Blue",
         "price": 27000.00,
         "transmission": "Manual"},
        {"name": "Kluger",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[4],
         "horsepower": 295,
         "color": "Green",
         "price": 33000.00,
         "transmission": "Automatic"},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            horsepower=data['horsepower'],
            color=data['color'],
            price=data['price'],
            transmission=data['transmission']
        )
