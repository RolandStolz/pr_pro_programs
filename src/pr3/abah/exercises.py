from pr_pro.exercise import (
    DurationExercise,
    RepsAndWeightsExercise,
    RepsDistanceExercise,
    RepsExercise,
    RepsRPEExercise,
)

box_jump = RepsExercise(name='Box jump')
single_leg_box_jump = RepsExercise(name='Single leg box jump')
cmj = RepsExercise(name='Counter movement jump')
depth_jump = RepsDistanceExercise(name='Depth jump')
eurostep_to_vert_jump = RepsExercise(name='Eurostep to vertical jump')

pendlay_row = RepsAndWeightsExercise(name='Pendlay row')
dumbbell_shoulder_press = RepsRPEExercise(name='Dumbbell shoulder press')
hip_thrust = RepsAndWeightsExercise(name='Hip thrust')
side_plank_leg_raise = RepsExercise(name='Side plank leg raise')
banded_side_plank_leg_raise = RepsExercise(name='Banded side plank leg raise')
cable_pulldown = RepsRPEExercise(name='Straight arm cable pulldown')
dumbbell_split_squat = RepsRPEExercise(name='Dumbbell split squat')
pallov_press = RepsRPEExercise(name='Pallov press')
squat_hold = DurationExercise(name='Squat hold')
hanging_knee_raise = RepsAndWeightsExercise(name='Hanging knee raise')
reverse_hyperextension = RepsExercise(name='Reverse hyperextension')
