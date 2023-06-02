# SEM1 2021/2022
# CSCI 2304 SECTION 2 INTELLIGENT SYSTEMS
# ASSIGNMENT 1
# TITLE: GUESS THE MOVIE
# INSTRUCTOR: ASSOC. PROF. TS. DR. AMELIA RITAHANI BINTI ISMAIL
# DONE BY: AHMED FAISAL 1921967 & MUHAMMAD ISMAIL 1922235
import math
import pygame


class Level:
    def __init__(self, level):  # Initialization.
        self.level = level
        self.mid_w, self.mid_h = self.level.DISPLAY_W / 2, self.level.DISPLAY_H / 2
        self.letter_rect = pygame.Rect(0, 0, 0, 0)
        self.run_display = True
        self.alphabets = ["a", False, "b", False, "c", False, "d", False, "e", False, "f", False, "g", False,
                          "h", False, "i", False, "j", False, "k", False, "l", False, "m", False, "n", False,
                          "o", False, "p", False, "q", False, "r", False, "s", False, "t", False, "u", False,
                          "v", False, "w", False, "x", False, "y", False, "z", False]
        self.total_alphabets = len(self.alphabets)
        self.unique_letters, self.total_lives, self.lives_lost, self.correct_letters = 0, 0, 0, 0
        self.lose, self.win = False, False

    def check_input(self, level_num):  # Checks for user input.
        if self.level.BACK_KEY:
            self.reset_level()
            self.level.curr_display = self.level.main_menu
            self.run_display = False
        if self.lose is True and self.level.ENTER_KEY:
            self.reset_level()
        if self.win is True and self.level.ENTER_KEY:
            self.reset_level()
            if level_num == "1":
                self.level.curr_display = self.level.level2
            if level_num == "2":
                self.level.curr_display = self.level.level3
            if level_num == "3":
                self.level.curr_display = self.level.level4
            if level_num == "4":
                self.level.curr_display = self.level.level5
            if level_num == "5":
                self.level.curr_display = self.level.credits
            self.run_display = False
        if self.lose is False and self.win is False:
            if self.level.a_KEY:
                self.alphabets[1] = True
            if self.level.b_KEY:
                self.alphabets[3] = True
            if self.level.c_KEY:
                self.alphabets[5] = True
            if self.level.d_KEY:
                self.alphabets[7] = True
            if self.level.e_KEY:
                self.alphabets[9] = True
            if self.level.f_KEY:
                self.alphabets[11] = True
            if self.level.g_KEY:
                self.alphabets[13] = True
            if self.level.h_KEY:
                self.alphabets[15] = True
            if self.level.i_KEY:
                self.alphabets[17] = True
            if self.level.j_KEY:
                self.alphabets[19] = True
            if self.level.k_KEY:
                self.alphabets[21] = True
            if self.level.l_KEY:
                self.alphabets[23] = True
            if self.level.m_KEY:
                self.alphabets[25] = True
            if self.level.n_KEY:
                self.alphabets[27] = True
            if self.level.o_KEY:
                self.alphabets[29] = True
            if self.level.p_KEY:
                self.alphabets[31] = True
            if self.level.q_KEY:
                self.alphabets[33] = True
            if self.level.r_KEY:
                self.alphabets[35] = True
            if self.level.s_KEY:
                self.alphabets[37] = True
            if self.level.t_KEY:
                self.alphabets[39] = True
            if self.level.u_KEY:
                self.alphabets[41] = True
            if self.level.v_KEY:
                self.alphabets[43] = True
            if self.level.w_KEY:
                self.alphabets[45] = True
            if self.level.x_KEY:
                self.alphabets[47] = True
            if self.level.y_KEY:
                self.alphabets[49] = True
            if self.level.z_KEY:
                self.alphabets[51] = True

    def level_loop(self, level_num, movie_name, movie_name_length):  # This is looped every frame when playing a level.
        self.level.check_events()
        self.check_input(level_num)
        self.level.display.fill(self.level.BLACK)
        self.level.print_text("Level " + level_num, 40, self.mid_w, self.mid_h - 100, self.level.WHITE)
        self.level.print_text("Press the letters you think are in this movie name", 20, self.mid_w, self.mid_h - 60,
                              self.level.WHITE)
        self.level.print_text(str(self.total_lives), 40, self.mid_w + 360, self.mid_h - 150, self.level.WHITE)
        self.level.print_text("Lives", 20, self.mid_w + 360, self.mid_h - 115, self.level.WHITE)
        self.level.print_text("Press esc to return to the main menu.", 15, self.mid_w, self.mid_h + 165,
                              self.level.WHITE)
        self.print_blanks(movie_name_length, movie_name)
        self.search_print_letter(movie_name, movie_name_length)
        self.calc_total_lives(movie_name, movie_name_length)
        self.victory_state(movie_name, movie_name_length)
        self.blit_screen()

    def blit_screen(self):  # Updates the screen display.
        self.level.window.blit(self.level.display, (0, 0))
        pygame.display.update()
        self.level.reset_keys()

    def reset_level(self):  # Resets the level.
        self.lose, self.win = False, False
        for i in range(self.total_alphabets):
            if i % 2 == 1:
                self.alphabets[i] = False

    def print_blanks(self, movie_name_length, movie_name):  # Prints dashes according the movie name.
        for i in range(movie_name_length):
            if movie_name[i] != " ":
                self.level.print_text('_', 30, self.mid_w - 10 - ((movie_name_length - 2) * 10) + (20 * i), self.mid_h,
                                      self.level.WHITE)

    def search_print_letter(self, movie_name, movie_name_length):  # Searches and prints letters chosen by the user.
        for i in range(movie_name_length):
            for j in range(self.total_alphabets):
                if j % 2 == 0:
                    if movie_name[i] == self.alphabets[j] and self.alphabets[j + 1]:
                        self.level.print_text(movie_name[i], 25,
                                              self.mid_w - 10 - ((movie_name_length - 2) * 10) + (20 * i),
                                              self.mid_h - 5, self.level.WHITE)

    def calc_total_lives(self, movie_name, movie_name_length):  # Calculates total number of lives left.
        alphabets = ["a", False, "b", False, "c", False, "d", False, "e", False, "f", False, "g", False,
                     "h", False, "i", False, "j", False, "k", False, "l", False, "m", False, "n", False,
                     "o", False, "p", False, "q", False, "r", False, "s", False, "t", False, "u", False,
                     "v", False, "w", False, "x", False, "y", False, "z", False]
        self.unique_letters = 0
        self.lives_lost = 0
        for i in range(movie_name_length):
            for j in range(self.total_alphabets):
                if j % 2 == 0:
                    if movie_name[i] == alphabets[j]:
                        alphabets[j + 1] = True
        for i in range(self.total_alphabets):
            if i % 2 == 1:
                if alphabets[i]:
                    self.unique_letters += 1
            if i % 2 == 0 and alphabets[i + 1] is False:
                for j in range(movie_name_length):
                    if alphabets[i] != movie_name[j] and self.alphabets[i + 1]:
                        self.lives_lost += 1
                        break
        self.total_lives = math.ceil(self.unique_letters / 2) - self.lives_lost

    def victory_state(self, movie_name, movie_name_length):  # Checks if the user has lost or won the game.
        if self.total_lives == 0:
            self.lose = True
            self.level.print_text("You lost!", 40, self.mid_w, self.mid_h + 100, (255, 0, 0))
            self.level.print_text("Press enter to try again!", 20, self.mid_w, self.mid_h + 120, (255, 0, 0))
        if self.total_lives != 0:
            self.correct_letters = 0
            for i in range(movie_name_length):
                if movie_name[i] == " ":
                    self.correct_letters += 1
                for j in range(self.total_alphabets):
                    if j % 2 == 0:
                        if movie_name[i] == self.alphabets[j] and self.alphabets[j + 1]:
                            self.correct_letters += 1
                            if self.correct_letters == movie_name_length:
                                self.win = True
                                self.level.print_text("You won!", 40, self.mid_w, self.mid_h + 100, (0, 255, 0))
                                self.level.print_text("Press enter to continue!", 20, self.mid_w,
                                                      self.mid_h + 120, (0, 255, 0))


class Level1(Level):
    def __init__(self, level):  # Initializes level 1.
        Level.__init__(self, level)
        self.level_num = "1"
        self.movie_name = "captain america"
        self.movie_name_length = len(self.movie_name)

    def display(self):  # Level 1 loop.
        self.run_display = True
        while self.run_display:
            self.level_loop(self.level_num, self.movie_name, self.movie_name_length)


class Level2(Level):
    def __init__(self, level):  # Initializes level 2.
        Level.__init__(self, level)
        self.level_num = "2"
        self.movie_name = "interstellar"
        self.movie_name_length = len(self.movie_name)

    def display(self):  # Level 2 loop.
        self.run_display = True
        while self.run_display:
            self.level_loop(self.level_num, self.movie_name, self.movie_name_length)


class Level3(Level):
    def __init__(self, level):  # Initializes level 3.
        Level.__init__(self, level)
        self.level_num = "3"
        self.movie_name = "elysium"
        self.movie_name_length = len(self.movie_name)

    def display(self):  # Level 3 loop.
        self.run_display = True
        while self.run_display:
            self.level_loop(self.level_num, self.movie_name, self.movie_name_length)


class Level4(Level):
    def __init__(self, level):  # Initializes level 4.
        Level.__init__(self, level)
        self.level_num = "4"
        self.movie_name = "tinker tailor soldier spy"
        self.movie_name_length = len(self.movie_name)

    def display(self):  # Level 4 loop.
        self.run_display = True
        while self.run_display:
            self.level_loop(self.level_num, self.movie_name, self.movie_name_length)


class Level5(Level):
    def __init__(self, level):  # Initializes level 5.
        Level.__init__(self, level)
        self.level_num = "5"
        self.movie_name = "the curious case of benjamin button"
        self.movie_name_length = len(self.movie_name)

    def display(self):  # Level 5 loop.
        self.run_display = True
        while self.run_display:
            self.level_loop(self.level_num, self.movie_name, self.movie_name_length)
