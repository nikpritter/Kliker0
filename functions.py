# Все функции проекта

# Импорт необходимых билиотек
import variables
import pygame
import sys

pygame.init()

def main(): # Создание основной функции

    screen = pygame.display.set_mode((variables.width, variables.height)) #Запуск экрана через библиотеку pygame
    pygame.display.set_caption("Kliker0") #Присвоение окну названия "Kliker0"
    screen.fill(variables.white) # Покраска в белый
    text_surface = variables.font.render(str(variables.score), True, variables.red)  # Рендер значения счёта в картинку
    screen.blit(text_surface, (20, 10))  # Вывод картинки со счётом на экран
    pygame.draw.rect(screen, variables.white, variables.button_klik)
    pygame.draw.rect(screen, variables.red, variables.button_klik, 2)
    screen.blit(variables.button_text, (variables.button_klik.x + 40, variables.button_klik.y + 14))
    pygame.display.flip() # Обновление окна

    while True:  # Цикл-затычка чтобы не сворачивалось окно
        for event in pygame.event.get(): # Запись каждого нажатия в переменную event
            if event.type == pygame.MOUSEBUTTONDOWN: # Проверка на нажатие кнопки мыши
                if event.button == 1:  # Проверка на нажатие левой кнопки мыши
                    if variables.button_klik.collidepoint(event.pos):  # Проверяем, попал ли клик в область кнопки
                        variables.score += 5
                    screen.fill(variables.white)  # Покраска в белый
                    text_surface = variables.font.render(str(variables.score), True, variables.red)  # Рендер значения счёта в картинку
                    screen.blit(text_surface, (20, 10))  # Вывод картинки со счётом на экран
                    pygame.draw.rect(screen, variables.white, variables.button_klik)
                    pygame.draw.rect(screen, variables.red, variables.button_klik, 2)
                    screen.blit(variables.button_text, (variables.button_klik.x + 40, variables.button_klik.y + 14))
                    pygame.display.flip()  # Обновление окна



            if event.type == pygame.QUIT: # Проверка кнопки
                screen.fill(variables.red) # Покраска в красный
                pygame.display.flip()  # Обновление окна
                pygame.time.delay(100) # Задержка на 0,1 секунды
                print(variables.score) # Вывод итогового результата
                sys.exit() # Выход из окна



