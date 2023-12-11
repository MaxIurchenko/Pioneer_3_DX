"""rxr_demo_template controller."""

from controller import Robot

# Get pointer to the robot.
robot = Robot()

# Get pointer to each wheel of our robot.
leftWheel = robot.getDevice('left wheel')
rightWheel = robot.getDevice('right wheel')
leftWheel.setVelocity(5)
rightWheel.setVelocity(5)

# Repeat the following 4 times (once for each side).
for i in range(0, 4):
    # First set both wheels to go forward, so the robot goes straight.
    leftWheel.setPosition(200)
    rightWheel.setPosition(200)
    # Wait for the robot to reach a corner.
    robot.step(4100)
    # Then, set the right wheel backward, so the robot will turn right.
    leftWheel.setPosition(100)
    rightWheel.setPosition(-100)
    # Wait until the robot has turned 90 degrees clockwise.
    robot.step(500)

# Stop the robot when path is completed, as the robot performance
# is only computed when the robot has stopped.
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)
