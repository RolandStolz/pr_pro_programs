from pr_pro.exercise import (
    DurationExercise,
    RepsAndWeightsExercise,
    RepsDistanceExercise,
    RepsExercise,
    RepsRPEExercise,
    PowerExercise,
)

box_jump = RepsExercise(name='Box jump')
single_leg_box_jump = RepsExercise(name='Single leg box jump')
cmj = RepsExercise(name='Counter movement jump')
eurostep_to_vert_jump = RepsExercise(name='Eurostep to vertical jump')
side_plank_leg_raise = RepsExercise(name='Side plank leg raise')
banded_side_plank_leg_raise = RepsExercise(name='Banded side plank leg raise')
reverse_hyperextension = RepsExercise(name='Reverse hyperextension')

pendlay_row = RepsAndWeightsExercise(name='Pendlay row')
clean_pull = RepsAndWeightsExercise(name='Clean pull')
hip_thrust = RepsAndWeightsExercise(name='Hip thrust')
hanging_knee_raise = RepsAndWeightsExercise(name='Hanging knee raise')
frontsquat = RepsAndWeightsExercise(name='Frontsquat')
strict_press = RepsAndWeightsExercise(name='Strict press')
sg_bhtn_press = RepsAndWeightsExercise(name='Snatch grip behind the neck press')
bulgarian_split_squat = RepsAndWeightsExercise(name='Bulgarian split squat')
russian_twist = RepsAndWeightsExercise(name='Russian twist')

dumbbell_shoulder_press = RepsRPEExercise(name='Dumbbell shoulder press')
cable_pulldown = RepsRPEExercise(name='Straight arm cable pulldown')
dumbbell_split_squat = RepsRPEExercise(name='Dumbbell split squat')
pallov_press = RepsRPEExercise(name='Pallov press')
incline_dumbbell_press = RepsRPEExercise(name='Inclined dumbbell press')

clean_jerk = PowerExercise(name='Clean & jerk')
power_clean = PowerExercise(name='Power clean')
snatch = PowerExercise(name='Snatch')
power_snatch = PowerExercise(name='Power snatch')
snatch_high_pull = PowerExercise(name='Snatch high pull')
low_hang_snatch = PowerExercise(name='Low hang snatch')
push_press = PowerExercise(name='Push press')

squat_hold = DurationExercise(name='Squat hold')

depth_jump = RepsDistanceExercise(name='Depth jump')
