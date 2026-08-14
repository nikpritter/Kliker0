import pygame #Импорт необходимой билиотеки pygame


pygame.init() #Запуск библиотеки pygame


stop = False # Переменная для цикла-затычки
width = 0 # Ширина окна
height = 0 # Высота окна

def main():
    screen = pygame.display.set_mode((width, height)) #Запуск экрана через библиотеку pygame
    pygame.display.set_caption("Kliker0") #Присвоение окну названия "Kliker0"

    while stop != True: #Цикл-затычка чтобы не сворачивалось окно
        a = 1


main()