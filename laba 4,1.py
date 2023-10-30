#Создать класс List (список), в котором реализовать методы для работы со списком (не менее 5).

class CustomList:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(str(item)+ " Не обнаружено в списке.")

    def find_item(self,item):
        if item in self.items:
            return str(item)+ " обнаружен в списке."
        else:
            return str(item)+ " не найдено в списке."

    def get_length(self):
        return len(self.items)

    def display_list(self):
        print(self.items)


my_list = CustomList()
my_list.add_item(1)
my_list.add_item(2)
my_list.add_item(3)
my_list.add_item(4)
my_list.add_item(5)

my_list.display_list()

print("Длина списка: ", my_list.get_length())

my_list.remove_item(3)
my_list.display_list()

print(my_list.find_item(3))