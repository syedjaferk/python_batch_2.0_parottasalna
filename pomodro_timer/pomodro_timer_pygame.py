import pygame
import time
import os

# Constants
WORK_DURATION = 25 * 60  # 25 minutes
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60
CYCLES_BEFORE_LONG_BREAK = 4

# Sound Files
START_SOUND = 'start.wav'
END_SOUND = 'end.wav'

class PomodoroTimer:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pomodoro Timer")
        self.font = pygame.font.SysFont("Arial", 72)
        self.small_font = pygame.font.SysFont("Arial", 36)

        self.clock = pygame.time.Clock()
        self.running = True
        self.timer_active = False

        self.session_type = "Work"
        self.session_count = 0
        self.start_time = 0
        self.duration = WORK_DURATION
        self.completed_sessions = []

    def play_sound(self, filename):
        if os.path.exists(filename):
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
        else:
            print(f"Sound file not found: {filename}")

    def start_session(self, duration, session_type):
        self.start_time = time.time()
        self.duration = duration
        self.session_type = session_type
        self.timer_active = True
        self.play_sound(START_SOUND)

    def stop_timer(self):
        self.timer_active = False
        self.session_type = "Work"

    def format_time(self, remaining):
        mins, secs = divmod(int(remaining), 60)
        return f"{mins:02}:{secs:02}"

    def draw(self, remaining):
        self.screen.fill((30, 30, 30))

        title_text = self.small_font.render(f"{self.session_type} Session", True, (255, 255, 255))
        self.screen.blit(title_text, (self.WIDTH // 2 - title_text.get_width() // 2, 100))

        timer_text = self.font.render(self.format_time(remaining), True, (255, 255, 255))
        self.screen.blit(timer_text, (self.WIDTH // 2 - timer_text.get_width() // 2, 200))

        instructions = self.small_font.render("Press SPACE to Start / Stop | ESC to Quit", True, (180, 180, 180))
        self.screen.blit(instructions, (self.WIDTH // 2 - instructions.get_width() // 2, 500))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)
            current_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_SPACE:
                        if not self.timer_active:
                            if self.session_type == "Work":
                                self.session_count += 1
                                self.start_session(WORK_DURATION, "Work")
                            elif self.session_type == "Break":
                                if self.session_count % CYCLES_BEFORE_LONG_BREAK == 0:
                                    self.start_session(LONG_BREAK, "Break")
                                else:
                                    self.start_session(SHORT_BREAK, "Break")
                        else:
                            self.stop_timer()

            if self.timer_active:
                elapsed = current_time - self.start_time
                remaining = self.duration - elapsed

                if remaining <= 0:
                    self.play_sound(END_SOUND)
                    if self.session_type == "Work":
                        self.completed_sessions.append(time.time())
                        self.session_type = "Break"
                    else:
                        self.session_type = "Work"
                    self.timer_active = False
                else:
                    self.draw(remaining)
            else:
                self.draw(self.duration)

        pygame.quit()

if __name__ == "__main__":
    PomodoroTimer().run()
