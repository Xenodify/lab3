class Car:
    def __init__(self):
        self.name = None
        self.color = None
        self.company = None
        self.status_door = None

# Какой-то новый коммент
def Car_create(Car):
    Car.company = input("Введите марку автомобиля: ")
    Car.name = input(f"Введите модель {Car.company}: ")
    Car.color = input(f"Введите цвет {Car.company} {Car.name}: ")
    Car.status_door = False

# Еще какой-то новый коммент
def Delete_car(autopark, car_select):
    print(f"Автомобиль {autopark[car_select].name} был удален")
    del autopark[car_select]
    if len(autopark) == 0:
        Car = Car()
        autopark = [Car]
    return autopark

def Append_car(autopark, car):
    Car_create(car)
    autopark.append(car)
    print(f"Автомобиль {car.name} был добавлен в автопарк")
    return autopark

def change_characteristics_car(Car):
    if Car.name is None:
        Car_create(Car)
        print(f"Марка автомобиля: {Car.company}")
        print(f"Модель {Car.company}: {Car.name}")
        print(f"Цвет автомобиля: {Car.color}")
        if not Car.status_door: print(f"Двери в автомобиле закрыты")
        else: print(f"Двери в автомобиле открыты")
    else:
        marker = 0
        while marker < 1 or marker > 5  :
            try:
                marker = int(input("Что вы хотите сделать?\n"
                                   "1: Посмотреть описание\n"
                                   "2: Изменить марку\n"
                                   "3: Изменить модель\n"
                                   "4: Изменить цвет\n"
                                   "5: Открыть/закрыть двери"))
            except: pass
        if marker == 1: print(f"Марка автомобиля: {Car.company}\n"
                              f"Название автомобиля: {Car.name}\n"
                              f"Цвет автомобиля: {Car.color}")
        if Car.status_door:
            Car.status_door = True
            print("Статус дверей: Открыты") #Говнокод. Поменяй 133-138
        else:
            print("Статус дверей: Закрыты")
        if marker == 2: Car.company = input("Введите новую марку автомобиля: ")
        if marker == 3: Car.name = input(f"Введите новое название модели {car.company}: ")
        if marker == 4: Car.color = input("Введите новый цвет автомобиля: ")
        if marker == 5 and not Car.status_door:
            Car.status_door = True
            print("Двери автомобиля теперь открыты")
        elif marker == 5 and Car.status_door:
            Car.status_door = False
            print("Двери автомобиля теперь закрыты")

autopark = []
while True:
    print(f"В вашем автопарке сейчас {len(autopark)} автомобилей:")
    for i in autopark: print(autopark.index(i), ":", i.name)
    car_select = -1
    n = 0
    while n < 1 or n > 3:
        try:
            n = int(input(f"Выберите, что вы хотите сделать:\n"
                          f"1: Изменить характеристики автомобиля,\n"
                          f"2: Добавить новый автомобиль,\n"
                          f"3: Удалить определенный автомобиль."))
        except: pass
    if n == 1: change_characteristics_car(autopark[int(input("Выберите ID автомобиля, с которым хотите "
                                                             "взаимодействовать: "))])
    elif n == 2:
        new_car = Car()
        autopark = Append_car(autopark, new_car)
    elif n == 3: autopark = Delete_car(autopark, int(input("Введите ID автомобиля, который хотите удалить: ")))