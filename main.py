import pygame #Импорт необходимой билиотеки pygame
pygame.init() #Запуск библиотеки pygame

stop = False
screen = pygame.display.set_mode((1000, 500)) #Запуск экрана через библиотеку pygame
pygame.display.set_caption("Kliker0") #Присвоение окну названия "Kliker0"

while stop != True: #Цикл-затычка чтобы не сворачивалось окно
    a = 1
