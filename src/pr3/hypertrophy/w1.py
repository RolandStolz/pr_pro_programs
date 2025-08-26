from pr_pro.exercises.common import backsquat, pullup, bench_press, deadlift, power_clean, pushup
from pr_pro.program import Program
from pr_pro.workout_component import ExerciseGroup, SingleExercise
from pr_pro.workout_session import WorkoutSession

from pr3.hypertrophy.exercises import (
    power_snatch,
    arms,
    box_jump,
    reverse_hyperextension,
    russian_twist,
    bo_dumbbell_row,
    dumbbell_press,
    muscle_snatch,
    side_plank_leg_raise,
    calf_raise,
    push_press,
    lunges,
)


def get_w1_sessions(program: Program) -> list[WorkoutSession]:
    w1d1 = (
        WorkoutSession(id='W1D1')
        .add_component(
            SingleExercise(exercise=box_jump).add_repeating_set(5, box_jump.create_set(4))
        )
        .add_component(
            SingleExercise(exercise=power_snatch).add_repeating_set(
                6, power_snatch.create_set(3, percentage=0.6)
            )
        )
        .add_component(
            SingleExercise(exercise=backsquat).add_repeating_set(
                4, backsquat.create_set(10, percentage=0.55)
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[reverse_hyperextension, russian_twist],
            ).add_repeating_group_sets(
                4,
                {
                    reverse_hyperextension: reverse_hyperextension.create_set(6),
                    russian_twist: russian_twist.create_set(8, weight=10),
                },
            )
        )
    )

    w1d2 = (
        WorkoutSession(id='W1D2')
        .add_component(
            SingleExercise(exercise=bench_press).add_repeating_set(
                4, bench_press.create_set(10, percentage=0.55)
            )
        )
        .add_component(SingleExercise(exercise=pullup).add_repeating_set(5, pullup.create_set(5)))
        .add_component(
            ExerciseGroup(
                exercises=[bo_dumbbell_row, dumbbell_press], notes='22-28; 14-20'
            ).add_repeating_group_sets(
                4,
                {
                    bo_dumbbell_row: bo_dumbbell_row.create_set(10, weight=25),
                    dumbbell_press: dumbbell_press.create_set(10, weight=17),
                },
            )
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(4, arms.create_set(10)))
    )

    w1d3 = (
        WorkoutSession(id='W1D3')
        .add_component(
            SingleExercise(exercise=backsquat).add_repeating_set(
                5, backsquat.create_set(6, percentage=0.65)
            )
        )
        .add_component(
            SingleExercise(exercise=muscle_snatch).add_repeating_set(
                5, muscle_snatch.create_set(3, percentage=0.4)
            )
        )
        .add_component(
            SingleExercise(exercise=deadlift).add_repeating_set(
                4, deadlift.create_set(10, percentage=0.55)
            )
        )
        .add_component(
            ExerciseGroup(exercises=[calf_raise, side_plank_leg_raise]).add_repeating_group_sets(
                4,
                {
                    calf_raise: calf_raise.create_set(12, 100),
                    side_plank_leg_raise: side_plank_leg_raise.create_set(6),
                },
            )
        )
    )

    w1d4 = (
        WorkoutSession(id='W1D4')
        .add_component(
            ExerciseGroup(exercises=[power_clean, push_press]).add_repeating_group_sets(
                4,
                {
                    power_clean: power_clean.create_set(3, percentage=0.5),
                    push_press: push_press.create_set(3, percentage=0.5),
                },
            )
        )
        .add_component(
            SingleExercise(exercise=bench_press).add_repeating_set(
                4, bench_press.create_set(8, percentage=0.6)
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[pullup, pushup, lunges], notes='Complete all as fast as possible!'
            ).add_group_sets(
                {
                    pullup: pullup.create_set(30),
                    pushup: pushup.create_set(50),
                    lunges: lunges.create_set(50, 20),
                },
            )
        )
    )

    program.add_workout_session(w1d1)
    program.add_workout_session(w1d2)
    program.add_workout_session(w1d3)
    program.add_workout_session(w1d4)

    return [w1d1, w1d2, w1d3]
