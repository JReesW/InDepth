class ParticleManager:
    """
    Handles the particle system
    """

    def __init__(self):
        self.__particles = []

    def add(self, particle: "Particle"):
        self.__particles.append(particle)

    def update(self):
        """
        Update all the particles stored in this manager
        """
        for particle in self.__particles:
            particle.update()
            particle.age += 1
            if particle.age >= particle.lifespan:
                self.__particles.remove(particle)
                del particle

    def render(self, surface, camera):
        """
        Render all the particles onto the given surface
        """
        for particle in self.__particles:
            particle.render(surface, camera)


class Particle:
    """
    Base particle class
    """

    def __init__(self, pos: (int, int), lifespan: int):
        self.pos = pos
        self.lifespan = lifespan
        self.age = 0

    def update(self):
        """
        Update the particle's state
        """
        pass

    def render(self, surface, camera):
        """
        Draw the particle onto the surface
        """
        pass
