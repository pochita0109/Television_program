# Kenneth John Costa
# Assignment 6
# TV Program

# Create a TV class
class TV:
# Set attributes for TV class
    def __init__ (self, channel = 1, volume_level = 1, switch = False):
        self.channel = channel
        self.volume_level = volume_level
        self.switch = switch
# Turn on the TV
    def turn_on(self):
        self.switch == True
        print("The TV is on")
# Turn off the TV
    def turn_off(self):
        self.switch == False
        print("The TV is off")
# Get the channel of TV
    def get_channel(self):
        return self.channel
# Set new channel of TV
    def set_channel(self, channel):
        if 1 <= channel >= 120:
            self.channel = channel
# Get the volume of TV
    def get_volume_level(self):
        return self.volume_level
# Set new volume of TV
    def set_volume_level(self, volume_level):
        if 1 <= volume_level >=7:
            self.volume_level = volume_level
# Increase the channel by 1
    def channel_increase(self):
        self.channel += 1
# Decrease the channel by 1
    def channel_decrease(self):
        self.channel -= 1
# Increase the volume by 1
# Decrease the volume by 1