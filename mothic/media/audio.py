from pygame import mixer


class AudioManager:
    """
    Handles playing sound effects for a scene
    """

    def __init__(self):
        mixer.init()

        self.sounds = {}
        self.__play_queue = []

    def add_sound(self, name: str, filename: str):
        """
        Store a sound under a given name, loaded from the given filename
        """
        self.sounds[name] = mixer.Sound(f"resources/sounds/{filename}")

    def play_sound(self, name: str):
        """
        Play a sound, given its name
        """
        if name in self.sounds and name not in self.__play_queue:
            self.__play_queue.append(name)

    def execute(self):
        """
        Play the queued sounds
        """
        for name in self.__play_queue:
            self.sounds[name].play()
        self.__play_queue = []
