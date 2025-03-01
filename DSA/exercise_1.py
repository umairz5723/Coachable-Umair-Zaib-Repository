""" Excersize 1 """

class Counter:
    """ Counter Class """
    def __init__(self, val: int) -> None:
        """ Function to initialize constructor"""
        self.count = val

    def get_count(self) -> int:
        """ Function to return count """
        return self.count

    def increment(self) -> None:
        """ Function to increment count """
        self.count += 1

    def reset_count(self) -> None:
        """ Function to reset count """
        self.count = 0


class LimitCounter(Counter):
    """ Limit Counter Class """
    def __init__(self, val: int) -> None:
        """ Function to initialize constructor"""

        self.max_threshold = 100

        if val > self.max_threshold:
            raise ValueError(f"The maximum threshold is {self.max_threshold}")
        super().__init__(val)

    def increment(self) -> None:
        """ Function to increment count """

        if self.count >= self.max_threshold:
            raise ValueError(f"Unable to increment, count is at maximum threshold of {self.max_threshold}")
        self.count += 1




class Thermostat:
    """ Theromstat Class """
    def __init__(self, temp: float = 72) -> None:
        """ Function to initialize constructor"""
        self.temp = temp

    def get_temperature(self) -> float:
        """ Function to return temperature """
        return self.temp

    def set_temperature(self, new_temp: float) -> None:
        """ Function to set temperature """

        if new_temp < 50 or new_temp > 90:
            raise ValueError ("Temperature you are trying to set must be between 50 to 90 degrees")

        self.temp = new_temp

    def __str__(self) -> str:
        """ Function to return string repr of object """
        return f"Thermostat temperature is currently {self.temp} degrees °F"


class SmartThermostat(Thermostat):
    """ SmartThermostat Class """
    def __init__(self, temp: float = 72) -> None:
        """ Function to initialize constructor """
        super().__init__(temp)
        self.eco_mode = False

    def set_temperature(self, new_temp: float) -> None:
        """ Function to set temperature """
        if self.eco_mode and (new_temp < 60 or new_temp > 78):
            raise ValueError ("Error: Eco Mode is on, temperature must be between 60-78 degrees")
        self.temp = new_temp

    def toggle_eco_mode(self) -> None:
        """ Function to toggle eco mode """
        self.eco_mode = not self.eco_mode

    def __str__(self) -> str:
        """ Function to return string repr of object """
        return super().__str__() + f" eco mode: {self.eco_mode}"
    
