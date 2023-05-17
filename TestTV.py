# Import TV class from Tv file
from Tv import TV
def test_drive():
# TV1
    TV1 = TV()
    TV1.turn_on()
    TV1.set_channel(30)
    TV1.set_channel(3)
    # Print the output
    print(f"The TV1's channel is {TV1.get_channel()}, and volume level is {TV1.get_volume_level()}")
# TV2
    TV2 = TV()
    TV2.turn_on()
    TV2.set_channel(3)
    TV2.set_channel(2)
    # Print the output
    print(f"The TV2's channel is {TV2.get_channel()}, and volume level is {TV2.get_volume_level()}")
test_drive()