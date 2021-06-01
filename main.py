from locorobo import LocoRobo
from locorobo import MotorDirection
from locorobo import Data
from locorobo import WaitType
from locorobo import Song
from locorobo import Note

def get_robot(robots, name):
    robot = None

    # Search through robots found during the scan for
    # the one we want
    for r in robots.values():
        if r.name == name:
            robot = r

            # We found the robot, so stop the for loop
            break

    # If we did not find the robot during the scan, stop the program
    if not robot:
        raise Exception('Could not find robot with specified name')

    return robot


def main():
    # Tell LocoRobo what serial port to use
    LocoRobo.setup("/dev/tty.usbmodem1")
    
    # Scan for robots
    robots = LocoRobo.scan(2000)

    # Use get_robots to find robot with name lr 00:07 in the scan result
    robot = get_robot(robots, "lr 44:bb")

    robot.connect()
    robot.activate_motors()
    robot.enable_sensor(Data.ULTRASONIC, True)

    # Your code
    # Play song and don't wait

    # Play Song and wait
    robot.enable_sensor(Data.ULTRASONIC, True)
    while True:
        robot.move(MotorDirection.FORWARD, MotorDirection.BACKWARD, 1, 0)
        LocoRobo.wait(1)
        robot.setup_wait(WaitType.SONG)
        robot.play_song(Song.EyeOfTheTiger, False)
        distance = robot.get_sensor_value(Data.ULTRASONIC)
        print(distance)
        if distance < 5:
            robot.move(MotorDirection.FORWARD, MotorDirection.BACKWARD, 1, 1)
            LocoRobo.wait(1)
        

    

    robot.deactivate_motors()
    robot.disconnect()

# If we are on the main thread, run the program
if __name__ == "__main__":

    try:
        main()
    except:
        LocoRobo.stop()
        raise

    LocoRobo.stop()

    # For compatibility with webapp's python, we can't use finally.
    # If you are using local python, you can do the following
    #
    # try:
    #     main()
    # finally:
    #     LocoRobo.stop()
