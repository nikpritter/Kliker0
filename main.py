import pygame # Импорт необходимой билиотеки pygame
import sys # Импорт необходимой билиотеки
#import functions # Импорт файла с функциями(на будущее)


pygame.init() #Запуск библиотеки pygame


font = pygame.font.SysFont("Arial", 20) # Создание шрифта


width = 800 # Ширина окна
height = 600 # Высота окна

white = (255,255,255) # Белый цвет
red = (255,0,0) # Красный цвет

score = 0 # Счёт игровой валюты


def main(): # Создание основной функции

    global score # Объявление глобальной переменной

    screen = pygame.display.set_mode((width, height)) #Запуск экрана через библиотеку pygame
    pygame.display.set_caption("Kliker0") #Присвоение окну названия "Kliker0"
    screen.fill(white) # Покраска в белый
    text_surface = font.render(str(score), True, red)  # Рендер значения счёта в картинку
    screen.blit(text_surface, (20, 10))  # Вывод картинки со счётом на экран
    pygame.display.flip() # Обновление окна

    while True:  # Цикл-затычка чтобы не сворачивалось окно
        for event in pygame.event.get(): # Запись каждого нажатия в переменную event
            if event.type == pygame.MOUSEBUTTONDOWN: # Проверка на нажатие кнопки мыши
                if event.button == 1: # Проверка на нажатие левой кнопки мыши
                    score += 1 # Начисление валюты за клик
                    screen.fill(white)  # Покраска в белый
                    text_surface = font.render(str(score), True, red) # Рендер значения счёта в картинку
                    screen.blit(text_surface, (20, 10)) # Вывод картинки со счётом на экран
                    pygame.display.flip() # Обновление окна



            if event.type == pygame.QUIT: # Проверка кнопки
                screen.fill(red) # Покраска в красный
                pygame.display.flip()  # Обновление окна
                pygame.time.delay(100) # Задержка на 0,1 секунды
                print(score) # Вывод итогового результата
                sys.exit() # Выход из окна


main() # Запуск основной функции