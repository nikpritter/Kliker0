# Все функции проекта

# Импорт необходимых билиотек
import variables
import pygame
import sys

pygame.init() #Запуск библиотеки pygame

def button_rendering(screen, button_variable, button_variable_text, x_magnification, y_magnification): # Создание: (переменная экрана, переменная кнопки, переменная текста кнопки, значение сдвига по х, значение сдвига по у)
    pygame.draw.rect(screen, variables.white, button_variable)  # Заливка кнопки
    pygame.draw.rect(screen, variables.red, button_variable, 2)  # Отрисовка границы кнопки
    screen.blit(button_variable_text,(button_variable.x + x_magnification, button_variable.y + y_magnification))  # Добавление текста на кнопку

def frame_rendering(screen):
    screen.fill(variables.white)  # Покраска в белый
    text_surface = variables.font20.render(str(variables.score), True, variables.red)  # Рендер значения счёта в картинку
    screen.blit(text_surface, (20, 10))  # Вывод картинки со счётом на экран
    button_rendering(screen, variables.button_klik, variables.button_text, 40, 14)
    button_rendering(screen, variables.button_aktiv_in, variables.button_aktiv_in_text, 7, 15)
    pygame.display.flip()  # Обновление окна

def main(): # Создание основной функции

    screen = pygame.display.set_mode((variables.width, variables.height)) #Запуск экрана через библиотеку pygame
    pygame.display.set_caption("Kliker0") #Присвоение окну названия "Kliker0"

    frame_rendering(screen)

    while True:  # Рабочий цикл
        for event in pygame.event.get(): # Запись каждого нажатия в переменную event
            if event.type == pygame.MOUSEBUTTONDOWN: # Проверка на нажатие кнопки мыши
                if event.button == 1:  # Проверка на нажатие левой кнопки мыши
                    if variables.button_klik.collidepoint(event.pos):  # Проверяем, попал ли клик в область кнопки
                        variables.score += variables.score_aktiv_in # Начисление баллов за нажатие кнопки
                    if variables.button_aktiv_in.collidepoint(event.pos) and variables.score >= 5:  # Проверяем, попал ли клик в область кнопки
                        variables.score_aktiv_in += 1 # Увеличение количества баллов за нажатие кнопки
                        variables.score -= 5# Отнимаем цену улучшения



                    frame_rendering(screen)
            if event.type == pygame.QUIT: # Проверка кнопки
                screen.fill(variables.red) # Покраска в красный
                pygame.display.flip()  # Обновление окна
                pygame.time.delay(100) # Задержка на 0,1 секунды
                print(variables.score) # Вывод итогового результата
                sys.exit() # Выход из окна