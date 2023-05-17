# Import TV class from Tv file
from Tv import TV
def test_drive():
# TV1
    print("\033[94m-" * 50)
    print("\033[92m\033[1mTV1".center(58))
    print("\033[94m-" * 50)
    TV1 = TV(channel = 30, volume_level = 3)
    TV1.turn_on()
    # Print the output
    print(f"\033[1m\033[92mThe TV1's channel is {TV1.get_channel()}, and volume level is {TV1.get_volume_level()}")
    print("\033[94m-" * 50)
    print()
    print("\033[94m-" * 50)

    print()
    print()
    print()

# TV2
    print("\033[95m-" * 50)
    print("\033[91m\033[1mTV2".center(58))
    print("\033[95m-" * 50)
    TV2 = TV(channel = 3, volume_level = 2)
    TV2.turn_on()
    # Print the output
    print(f"\033[1m\033[91mThe TV2's channel is {TV2.get_channel()}, and volume level is {TV2.get_volume_level()}")
    print("\033[95m-" * 50)
    print()
    print("\033[95m-" * 50)

test_drive()