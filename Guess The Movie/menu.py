# SEM1 2021/2022
# CSCI 2304 SECTION 2 INTELLIGENT SYSTEMS
# ASSIGNMENT 1
# TITLE: GUESS THE MOVIE
# INSTRUCTOR: ASSOC. PROF. TS. DR. AMELIA RITAHANI BINTI ISMAIL
# DONE BY: AHMED FAISAL 1921967 & MUHAMMAD ISMAIL 1922235
import sys
import pygame


class Menu:
    def __init__(self, menu):  # Initialization.
        self.menu = menu
        self.mid_w, self.mid_h = self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 0, 0)
        self.offset_1 = - 75
        self.offset_2 = + 25

    def print_cursor_1(self):  # Displays '>' & '<' cursors.
        self.menu.print_text('>', 15, self.cursor_rect.x, self.cursor_rect.y, self.menu.WHITE)
        self.menu.print_text('<', 15, self.cursor_rect.x + 150, self.cursor_rect.y, self.menu.WHITE)

    def print_cursor_2(self):  # Displays '^' cursors.
        self.menu.print_text('^', 15, self.cursor_rect.x, self.cursor_rect.y, self.menu.WHITE)

    def blit_screen(self):  # Updates the screen display.
        self.menu.window.blit(self.menu.display, (0, 0))
        pygame.display.update()
        self.menu.reset_keys()


class MainMenu(Menu):
    def __init__(self, menu):  # Initializes the Main Menu.
        Menu.__init__(self, menu)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 50
        self.exitx, self.exity = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset_1, self.starty)

    def display(self):  # Main Menu loop.
        self.run_display = True
        while self.run_display:
            self.menu.check_events()
            self.check_input()
            self.menu.display.fill(self.menu.BLACK)
            self.menu.print_text('Guess The Movie', 60, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 - 80,
                                 self.menu.WHITE)
            self.menu.print_text('Main Menu', 40, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 - 20,
                                 self.menu.WHITE)
            self.menu.print_text("Start game", 20, self.startx, self.starty, self.menu.WHITE)
            self.menu.print_text("Credits", 20, self.creditsx, self.creditsy, self.menu.WHITE)
            self.menu.print_text("Exit", 20, self.exitx, self.exity, self.menu.WHITE)
            self.menu.print_text("Press up and down keys to navigate.", 15,
                                 self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 + 150, self.menu.WHITE)
            self.menu.print_text("Press enter to select.", 15,
                                 self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 + 165, self.menu.WHITE)
            self.print_cursor_1()
            self.blit_screen()

    def move_cursor(self):  # Move cursors based on the users input.
        if self.menu.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset_1, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + self.offset_1, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset_1, self.starty)
                self.state = 'Start'
        elif self.menu.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset_1, self.exity)
                self.state = 'Exit'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset_1, self.starty)
                self.state = 'Start'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + self.offset_1, self.creditsy)
                self.state = 'Credits'

    def check_input(self):  # Changes menu according to the users input.
        self.move_cursor()
        if self.menu.ENTER_KEY:
            if self.state == 'Start':
                self.menu.curr_display = self.menu.levels_menu
            elif self.state == 'Credits':
                self.menu.curr_display = self.menu.credits
            elif self.state == 'Exit':
                sys.exit()
            self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, menu):  # Initializes the Credits Menu.
        Menu.__init__(self, menu)

    def display(self):  # Credits Menu loop.
        self.run_display = True
        while self.run_display:
            self.menu.check_events()
            if self.menu.ENTER_KEY:
                self.menu.curr_display = self.menu.main_menu
                self.run_display = False
            self.menu.display.fill(self.menu.BLACK)
            self.menu.print_text("Thank you for playing!", 60, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 - 80,
                                 self.menu.WHITE)
            self.menu.print_text("Made by", 40, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 - 20,
                                 self.menu.WHITE)
            self.menu.print_text("Ahmed Faisal 1921967", 20, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 + 30,
                                 self.menu.WHITE)
            self.menu.print_text("Muhammad Ismail 1922235", 20, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 + 50,
                                 self.menu.WHITE)
            self.menu.print_text("Press enter to return to the main menu.", 15,
                                 self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 + 165, self.menu.WHITE)
            self.blit_screen()


class LevelsMenu(Menu):
    def __init__(self, menu):  # Initializes the Levels Menu.
        Menu.__init__(self, menu)
        self.state = 'Lvl1'
        self.lvl1x, self.lvl1y = self.mid_w - 50, self.mid_h + 20
        self.lvl2x, self.lvl2y = self.mid_w - 25, self.mid_h + 20
        self.lvl3x, self.lvl3y = self.mid_w, self.mid_h + 20
        self.lvl4x, self.lvl4y = self.mid_w + 25, self.mid_h + 20
        self.lvl5x, self.lvl5y = self.mid_w + 50, self.mid_h + 20
        self.cursor_rect.midtop = (self.lvl1x, self.lvl1y + self.offset_2)

    def display(self):  # Levels Menu loop.
        self.run_display = True
        while self.run_display:
            self.menu.check_events()
            self.check_input()
            self.menu.display.fill((0, 0, 0))
            self.menu.print_text('Guess The Movie', 60, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 - 80,
                                 self.menu.WHITE)
            self.menu.print_text('Levels', 40, self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 - 20, self.menu.WHITE)
            self.menu.print_text("1", 15, self.lvl1x, self.lvl1y, self.menu.WHITE)
            self.menu.print_text("2", 15, self.lvl2x, self.lvl2y, self.menu.WHITE)
            self.menu.print_text("3", 15, self.lvl3x, self.lvl3y, self.menu.WHITE)
            self.menu.print_text("4", 15, self.lvl4x, self.lvl4y, self.menu.WHITE)
            self.menu.print_text("5", 15, self.lvl5x, self.lvl5y, self.menu.WHITE)
            self.menu.print_text("Press left and right keys to navigate.", 15,
                                 self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 + 135, self.menu.WHITE)
            self.menu.print_text("Press esc to return to the main menu.", 15, self.mid_w, self.mid_h + 150,
                                 self.menu.WHITE)
            self.menu.print_text("Press enter to select.", 15,
                                 self.menu.DISPLAY_W / 2, self.menu.DISPLAY_H / 2 + 165, self.menu.WHITE)
            self.print_cursor_2()
            self.blit_screen()

    def check_input(self):  # Checks for the users input and updates the display accordingly.
        if self.menu.BACK_KEY:
            self.menu.curr_display = self.menu.main_menu
            self.run_display = False
        elif self.menu.RIGHT_KEY:
            if self.state == 'Lvl1':
                self.cursor_rect.midtop = (self.lvl2x, self.lvl2y + self.offset_2)
                self.state = 'Lvl2'
            elif self.state == 'Lvl2':
                self.cursor_rect.midtop = (self.lvl3x, self.lvl3y + self.offset_2)
                self.state = 'Lvl3'
            elif self.state == 'Lvl3':
                self.cursor_rect.midtop = (self.lvl4x, self.lvl4y + self.offset_2)
                self.state = 'Lvl4'
            elif self.state == 'Lvl4':
                self.cursor_rect.midtop = (self.lvl5x, self.lvl5y + self.offset_2)
                self.state = 'Lvl5'
            elif self.state == 'Lvl5':
                self.cursor_rect.midtop = (self.lvl1x, self.lvl1y + self.offset_2)
                self.state = 'Lvl1'
        elif self.menu.LEFT_KEY:
            if self.state == 'Lvl1':
                self.cursor_rect.midtop = (self.lvl5x, self.lvl5y + self.offset_2)
                self.state = 'Lvl5'
            elif self.state == 'Lvl2':
                self.cursor_rect.midtop = (self.lvl1x, self.lvl1y + self.offset_2)
                self.state = 'Lvl1'
            elif self.state == 'Lvl3':
                self.cursor_rect.midtop = (self.lvl2x, self.lvl2y + self.offset_2)
                self.state = 'Lvl2'
            elif self.state == 'Lvl4':
                self.cursor_rect.midtop = (self.lvl3x, self.lvl3y + self.offset_2)
                self.state = 'Lvl3'
            elif self.state == 'Lvl5':
                self.cursor_rect.midtop = (self.lvl4x, self.lvl4y + self.offset_2)
                self.state = 'Lvl4'
        if self.menu.ENTER_KEY:
            if self.state == 'Lvl1':
                self.menu.curr_display = self.menu.level1
            if self.state == 'Lvl2':
                self.menu.curr_display = self.menu.level2
            if self.state == 'Lvl3':
                self.menu.curr_display = self.menu.level3
            if self.state == 'Lvl4':
                self.menu.curr_display = self.menu.level4
            if self.state == 'Lvl5':
                self.menu.curr_display = self.menu.level5
            self.run_display = False
