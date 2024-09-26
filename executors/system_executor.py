from mouse_keyboard_bot import Bot
import subprocess


class SystemExecutor:
    def _open_program(self, program):
        if program not in self.programs.keys():
            self.speak("Я не знаю такой программы. Проверьте файл \"programs.json\"")
            return
        self.speak(f"Открываю {program}")
        subprocess.Popen(self.programs[program])

    # def _close_program(self, program):
    #     if program not in self.programs.keys():
    #         self.speak("Я не знаю такой программы. Проверьте файл \"programs.json\"")
    #         return
    #     self.speak(f"закрываю {program}")
    #     image = self.return_image(program)
    #     bot.find(image)
    #     bot.click()

    def _change_volume(self, units: int, is_up: bool=True):
        if is_up:
            self.Sound.volume_set(self.Sound.current_volume() + int(units))
        else:
            self.Sound.volume_set(self.Sound.current_volume() - int(units))
        
    def _set_volume(self, units: int):
        self.Sound.volume_set(int(units))

    def _load_programs(self, config_file: str="programs.json"):
        with open(config_file, "r") as file:
            programs = load(file)
            print("Программы загружены!", programs)
            self.programs = programs