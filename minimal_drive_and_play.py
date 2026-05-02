import math

import AuroraMR as amr

# create motion object
s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
# moves object forward by a distance and at a speed
s.forward(1.5, 1)
#rotate the object ccw for an angla and at an angular speed
s.turn_left(math.pi / 4, 2.0)
s.forward(0.5, 0.5)
#rotate the object cw for an angla and at an angular speed
s.turn_right(math.pi / 6, 1.0)
s.forward(0.5, 0.5)
s.turn_left(math.pi, 1.0)
s.forward(1.0, 0.5)

amr.play_motion(s, playback_speed=2.0, log=True, show=True)
