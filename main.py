import pygame #Импорт необходимой билиотеки pygame
import sys #Импорт необходимой билиотеки


pygame.init() #Запуск библиотеки pygame


stop = False # Переменная для цикла-затычки
width = 800 # Ширина окна
height = 600 # Высота окна
color = (255,255,255) # Цвет

def Main():
    screen = pygame.display.set_mode((width, height)) #Запуск экрана через библиотеку pygame
    pygame.display.set_caption("Kliker0") #Присвоение окну названия "Kliker0"
    screen.fill(color) # Заливка цвета
    pygame.display.flip() # Обновление окна

    while stop != True: #Цикл-затычка чтобы не сворачивалось окно
        for event in pygame.event.get(): # Запись каждого нажатия в переменную event
            if event.type == pygame.QUIT: # Проверка кнопки
                sys.exit() # Выход из окна







Main()