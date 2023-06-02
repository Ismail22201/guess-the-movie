# SEM1 2021/2022
# CSCI 2304 SECTION 2 INTELLIGENT SYSTEMS
# ASSIGNMENT 1
# TITLE: GUESS THE MOVIE
# INSTRUCTOR: ASSOC. PROF. TS. DR. AMELIA RITAHANI BINTI ISMAIL
# DONE BY: AHMED FAISAL 1921967 & MUHAMMAD ISMAIL 1922235
from levels import *
from menu import *


class Game:
    def __init__(self):  # Initialization
        pygame.init()
        pygame.display.set_caption("Guess The Movie")
        self.running, self.playing = True, False
        self.ENTER_KEY, self.BACK_KEY = False, False
        self.DOWN_KEY, self.UP_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False
        self.a_KEY, self.b_KEY, self.c_KEY, self.d_KEY, self.e_KEY = False, False, False, False, False
        self.f_KEY, self.g_KEY, self.h_KEY, self.i_KEY, self.j_KEY = False, False, False, False, False
        self.k_KEY, self.l_KEY, self.m_KEY, self.n_KEY, self.o_KEY = False, False, False, False, False
        self.p_KEY, self.q_KEY, self.r_KEY, self.s_KEY, self.t_KEY = False, False, False, False, False
        self.u_KEY, self.v_KEY, self.w_KEY, self.x_KEY, self.y_KEY = False, False, False, False, False
        self.z_KEY = False
        self.DISPLAY_W, self.DISPLAY_H = 810, 360
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = "upheavtt.ttf"
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.levels_menu = LevelsMenu(self)
        self.credits = CreditsMenu(self)
        self.level1 = Level1(self)
        self.level2 = Level2(self)
        self.level3 = Level3(self)
        self.level4 = Level4(self)
        self.level5 = Level5(self)
        self.curr_display = self.main_menu

    def check_events(self):  # Checks for user input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_display.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_a:
                    self.a_KEY = True
                if event.key == pygame.K_b:
                    self.b_KEY = True
                if event.key == pygame.K_c:
                    self.c_KEY = True
                if event.key == pygame.K_d:
                    self.d_KEY = True
                if event.key == pygame.K_e:
                    self.e_KEY = True
                if event.key == pygame.K_f:
                    self.f_KEY = True
                if event.key == pygame.K_g:
                    self.g_KEY = True
                if event.key == pygame.K_h:
                    self.h_KEY = True
                if event.key == pygame.K_i:
                    self.i_KEY = True
                if event.key == pygame.K_j:
                    self.j_KEY = True
                if event.key == pygame.K_k:
                    self.k_KEY = True
                if event.key == pygame.K_l:
                    self.l_KEY = True
                if event.key == pygame.K_m:
                    self.m_KEY = True
                if event.key == pygame.K_n:
                    self.n_KEY = True
                if event.key == pygame.K_o:
                    self.o_KEY = True
                if event.key == pygame.K_p:
                    self.p_KEY = True
                if event.key == pygame.K_q:
                    self.q_KEY = True
                if event.key == pygame.K_r:
                    self.r_KEY = True
                if event.key == pygame.K_s:
                    self.s_KEY = True
                if event.key == pygame.K_t:
                    self.t_KEY = True
                if event.key == pygame.K_u:
                    self.u_KEY = True
                if event.key == pygame.K_v:
                    self.v_KEY = True
                if event.key == pygame.K_w:
                    self.w_KEY = True
                if event.key == pygame.K_x:
                    self.x_KEY = True
                if event.key == pygame.K_y:
                    self.y_KEY = True
                if event.key == pygame.K_z:
                    self.z_KEY = True

    def reset_keys(self):  # Resets all keys to False.
        self.ENTER_KEY, self.BACK_KEY = False, False
        self.DOWN_KEY, self.UP_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False
        self.a_KEY, self.b_KEY, self.c_KEY, self.d_KEY, self.e_KEY = False, False, False, False, False
        self.f_KEY, self.g_KEY, self.h_KEY, self.i_KEY, self.j_KEY = False, False, False, False, False
        self.k_KEY, self.l_KEY, self.m_KEY, self.n_KEY, self.o_KEY = False, False, False, False, False
        self.p_KEY, self.q_KEY, self.r_KEY, self.s_KEY, self.t_KEY = False, False, False, False, False
        self.u_KEY, self.v_KEY, self.w_KEY, self.x_KEY, self.y_KEY = False, False, False, False, False
        self.z_KEY = False

    def print_text(self, text, size, x, y, color):  # Prints text.
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
