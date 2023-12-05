import logging

logging.basicConfig(
    format="%(asctime)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S"
)


class Circle:
    def __init__(self, radius):
        self._msg = '"radius" was %s. Current value: %s'
        self.radius = radius

    @property
    def radius(self):
        """The radius property"""
        logging.info(self._msg.format("accessed", str(self._radius)))
        return self._radius

    @radius.setter
    def radius(self, value):
        try:
            self._radius = float(value)
            logging.info(
                self._msg % ("mutated", str(self._radius))
            )
        except ValueError:
            logging.error(
                'validation error while mutating "radius"'
            )
