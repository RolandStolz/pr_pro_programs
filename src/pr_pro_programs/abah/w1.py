import datetime

from pr_pro.exercises.common import backsquat, bench_press, deadlift, pullup, pushup
from pr_pro.program import Program
from pr_pro.workout_component import ExerciseGroup, SingleExercise
from pr_pro.workout_session import WorkoutSession

from pr_pro_programs.abah.exercises import (
    box_jump,
    cable_pulldown,
    dumbbell_shoulder_press,
    dumbbell_split_squat,
    hanging_knee_raise,
    hip_thrust,
    pallov_press,
    pendlay_row,
    reverse_hyperextension,
    side_plank_leg_raise,
    squat_hold,
)


def get_w1_sessions(program: Program) -> list[WorkoutSession]:
    w1d1 = (
        WorkoutSession(id='W1D1')
        .add_component(
            SingleExercise(exercise=box_jump, notes='Good warmup please!').add_repeating_set(
                5, box_jump.create_set(4)
            )
        )
        .add_component(
            SingleExercise(exercise=backsquat).add_repeating_set(
                4, backsquat.create_set(5, percentage=0.55)
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[pendlay_row, dumbbell_shoulder_press],
                notes='Put down completely for pendlay row.',
            ).add_repeating_group_sets(
                4,
                {
                    pendlay_row: pendlay_row.create_set(6, percentage=0.6),
                    dumbbell_shoulder_press: dumbbell_shoulder_press.create_set(10, rpe=6),
                },
            )
        )
        .add_component(
            ExerciseGroup(exercises=[hip_thrust, side_plank_leg_raise]).add_repeating_group_sets(
                4,
                {
                    hip_thrust: hip_thrust.create_set(8, weight=60),
                    side_plank_leg_raise: side_plank_leg_raise.create_set(10),
                },
            )
        )
    )

    w1d2 = (
        WorkoutSession(id='W1D2')
        .add_component(
            SingleExercise(exercise=deadlift, notes='Squeeze glutes!').add_repeating_set(
                3, deadlift.create_set(12, percentage=0.5)
            )
        )
        .add_component(
            SingleExercise(exercise=dumbbell_split_squat).add_repeating_set(
                4, dumbbell_split_squat.create_set(6, rpe=6)
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[pullup, pushup], notes='Pullup with reverse grip'
            ).add_repeating_group_sets(
                5,
                {pullup: pullup.create_set(1), pushup: pushup.create_set(6)},
            )
        )
        .add_component(
            ExerciseGroup(exercises=[cable_pulldown, pallov_press]).add_repeating_group_sets(
                4,
                {
                    cable_pulldown: cable_pulldown.create_set(10, rpe=6),
                    pallov_press: pallov_press.create_set(10, rpe=6),
                },
            )
        )
    )

    w1d3 = (
        WorkoutSession(id='W1D3')
        .add_component(
            SingleExercise(exercise=squat_hold).add_repeating_set(
                3, squat_hold.create_set(duration=datetime.timedelta(minutes=1))
            )
        )
        .add_component(
            SingleExercise(exercise=backsquat).add_repeating_set(
                4, backsquat.create_set(8, percentage=0.6)
            )
        )
        .add_component(
            SingleExercise(exercise=deadlift, notes='Every minute on the minute').add_repeating_set(
                10, deadlift.create_set(2, percentage=0.5)
            )
        )
        .add_component(
            SingleExercise(exercise=bench_press).add_repeating_set(
                4, bench_press.create_set(10, percentage=0.6)
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[hanging_knee_raise, reverse_hyperextension]
            ).add_repeating_group_sets(
                4,
                {
                    hanging_knee_raise: hanging_knee_raise.create_set(6, weight=10),
                    reverse_hyperextension: reverse_hyperextension.create_set(6),
                },
            )
        )
    )

    program.add_workout_session(w1d1)
    program.add_workout_session(w1d2)
    program.add_workout_session(w1d3)

    return [w1d1, w1d2, w1d3]
