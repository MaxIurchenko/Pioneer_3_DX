"""square_path_supervisor controller."""

import os

from controller import Supervisor
from square_path_metric import SquarePathMetric

# Set to true to enable information displayed in labels.
ALLOW_LABELS = False

# The color used for the labels.
TEXT_COLOR = 0x0000ff


metric = SquarePathMetric(True)


# Create the Supervisor instance.
supervisor = Supervisor()

# Gets the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())

# Gets the reference to the robot.
pioneer = supervisor.getFromDef('PIONEER')

# Main loop starts here.
while (supervisor.step(timestep) != -1
       and not metric.isBenchmarkOver()):

    # Recovers current time and position/orientation of the robot.
    pos = pioneer.getPosition()
    pos2d = [pos[0], -pos[1]]

    orientation = pioneer.getOrientation()
    time = supervisor.getTime()

    metric.update(pos2d, orientation, time)

    if ALLOW_LABELS:
        metric.updateLabels(0x0000ff, supervisor, time)

    supervisor.wwiSendText('update:' + metric.getWebMetricUpdate())

    for pointMessage in metric.getWebNewPoints():
        supervisor.wwiSendText(pointMessage)

supervisor.wwiSendText('stop')

CI = os.environ.get("CI")
if CI:
    print(f"performance:{metric.getPerformance()}")
else:
    print(f"Benchmark finished with a performance of {metric.getPerformance()*100:.2f}%")

supervisor.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
