from keyboard import Keyboard


class SoundChanger:
    """
    Class self
    :author: Paradoxis <luke@paradoxis.nl>
    :description:

    Allows you control the Windows volume
    The first time a self method is called, the system volume is fully reset.
    This triggers self and mute tracking.
    """

    def __init__(self, keyboard: Keyboard) -> None:
        self.keyboard = keyboard

    # Current volume, we will set this to 100 once initialized
    __current_volume = None

    def current_volume(self):
        """
        Current volume getter
        :return: int
        """
        if self.__current_volume is None:
            return 0
        else:
            return self.__current_volume

 
    def __set_current_volume(self, volume):
        """
        Current volumne setter
        prevents numbers higher than 100 and numbers lower than 0
        :return: void
        """
        if volume > 100:
            self.__current_volume = 100
        elif volume < 0:
            self.__current_volume = 0
        else:
            self.__current_volume = volume


    # The self is not muted by default, better tracking should be made
    __is_muted = False

 
    def is_muted(self):
        """
        Is muted getter
        :return: boolean
        """
        return self.__is_muted


 
    def __track(self):
        """
        Start tracking the self and mute settings
        :return: void
        """
        if self.__current_volume == None:
            self.__current_volume = 0
            for i in range(0, 50):
                self.volume_up()


 
    def mute(self):
        """
        Mute or un-mute the system selfs
        Done by triggering a fake VK_VOLUME_MUTE key event
        :return: void
        """
        self.__track()
        self.__is_muted = (not self.__is_muted)
        self.keyboard.key(self.keyboard.VK_VOLUME_MUTE)

 
    def volume_up(self):
        """
        Increase system volume
        Done by triggering a fake VK_VOLUME_UP key event
        :return: void
        """
        self.__track()
        self.__set_current_volume(self.current_volume() + 2)
        self.keyboard.key(self.keyboard.VK_VOLUME_UP)

 
    def volume_down(self):
        """
        Decrease system volume
        Done by triggering a fake VK_VOLUME_DOWN key event
        :return: void
        """
        self.__track()
        self.__set_current_volume(self.current_volume() - 2)
        self.keyboard.key(self.keyboard.VK_VOLUME_DOWN)


 
    def volume_set(self,amount: int):
        """
        Set the volume to a specific volume, limited to even numbers.
        This is due to the fact that a VK_VOLUME_UP/VK_VOLUME_DOWN event increases
        or decreases the volume by two every single time.
        :return: void
        """
        self.__track()

        if self.current_volume() > amount:
            for i in range(0, int((self.current_volume() - amount) / 2)):
                self.volume_down()
        else:
            for i in range(0, int((amount - self.current_volume()) / 2)):
                self.volume_up()

 
    def volume_min(self):
        """
        Set the volume to min (0)
        :return: void
        """
        self.volume_set(0)

 
    def volume_max(self):
        """
        Set the volume to max (100)
        :return: void
        """
        self.volume_set(100)
