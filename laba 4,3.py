#Требуется написать программу, которая вычисляет общую площадь стены
#комнаты, которую необходимо оклеить обоями. При этом окна, двери, пол и
#потолок оклеивать не нужно.

class Room:
    def __init__(self, wall_width, wall_height, wall_length, ceiling_height,s_window, s_doors, windows_height):
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.wall_length = wall_length
        self.ceiling_height = ceiling_height
        self.s_window = s_window
        self.s_doors = s_doors
        self.windows_height = windows_height

    def calculate_wallpaper_area(self):
        # Вычисление площади стен для покрытия обоями
        s_walls = (self.wall_width + self.wall_length) * 2 * self.wall_height - self.s_window - self.s_doors * self.windows_height
        return s_walls

# Заданные размеры и параметры
wall_width = 5
wall_height = 2.5
wall_length = 7
ceiling_height = 3
s_window = 6
s_doors = 2
windows_height = 1

# Создание обьекта комнаты
room = Room(wall_width, wall_height,wall_length, ceiling_height, s_window,s_doors,windows_height)

# Вычисление общей площади
wallpaper_area = room.calculate_wallpaper_area()

print("Общая площадь стен для оклейки обоями: ", wallpaper_area , "квадратных метров")