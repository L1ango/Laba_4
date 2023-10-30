#Создать классы «Транспортное средство», «Самолет», «Поезд»,
#«Автомобиль». Определить время и стоимость перевозки для указанных
#городов и расстояний, в каждом классе реализовать переопределение метода
#«способ передвижения». Вывести данные о наиболее быстрой и экономичной
#поездке. Предусмотреть метод записи информации в файл.

class Transport:
    def __init__(self, speed, price):
        self.speed = speed
        self.price = price

    def TransportMethod(self):
        pass

class Airplane(Transport):
    def __init__(self):
        super().__init__(800,1000)

    def TransportMethod(self):
            return "Самолет"


class Train(Transport):
    def __init__(self):
        super().__init__(120, 300)

    def TransportMethod(self):
            return "Поезд"


class Car(Transport):
    def __init__(self):
        super().__init__(100, 500)

    def TransportMethod(self):
            return "Автомобиль"

City_A="Город А"
City_B="Город Б"
distance = 500

Transport_List = [Airplane(), Train(), Car()]

Fastest = ""
TimeFastest = float("inf")
Name_Economy = ""
Price_Economy = float("inf")

for Transport in Transport_List:
    time = distance / Transport.speed
    price = distance * Transport.price

    if time < TimeFastest:
        TimeFastest = time
        Fastest = Transport.TransportMethod()

    if price < Price_Economy:
        Price_Economy = price
        Name_Economy = Transport.TransportMethod()

print("Наиболее быстрая поездка: ", Fastest + ", Время: ", TimeFastest, " часов")
print("Наиболее экономичная поездка: ", Name_Economy + ", Стоимость: ", Price_Economy, " рублей")

with open("Поездки.txt", "w") as file:
    file.write("Наиболее быстрая поездка: " + Fastest + ", Время: " + str(TimeFastest) + " часов\n")
    file.write("Наиболее экономичная поездка: " + Name_Economy + ", Стоимость: " + str(Price_Economy) + " рублей\n")