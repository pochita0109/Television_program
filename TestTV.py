# Import TV class from Tv file
from Tv import TV
def test_drive():
# TV1
    TV1 = TV(channel = 30, volume_level = 3)
    TV1.turn_on()
    # Print the output
    print(f"The TV1's channel is {TV1.get_channel()}, and volume level is {TV1.get_volume_level()}")
# TV2
    TV2 = TV(channel = 3, volume_level = 2)
    TV2.turn_on()
    # Print the output
    print(f"The TV2's channel is {TV2.get_channel()}, and volume level is {TV2.get_volume_level()}")
test_drive()