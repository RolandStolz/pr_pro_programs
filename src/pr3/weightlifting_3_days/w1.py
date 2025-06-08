from pr_pro.exercises.common import backsquat, pullup
from pr_pro.program import Program
from pr_pro.workout_component import ExerciseGroup, SingleExercise
from pr_pro.workout_session import WorkoutSession

from pr3.weightlifting_3_days.exercises import (
    box_jump,
    bulgarian_split_squat,
    clean_jerk,
    clean_pull,
    frontsquat,
    incline_dumbbell_press,
    low_hang_snatch,
    pendlay_row,
    power_snatch,
    reverse_hyperextension,
    russian_twist,
    sg_bhtn_press,
    side_plank_leg_raise,
    snatch,
    snatch_high_pull,
    strict_press,
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
            SingleExercise(exercise=backsquat)
            .add_repeating_set(5, backsquat.create_set(6, percentage=0.55))
            .set_notes('First half paused 1s.')
        )
        .add_component(
            SingleExercise(exercise=incline_dumbbell_press, notes='Around 20 kg').add_repeating_set(
                4, incline_dumbbell_press.create_set(10, rpe=6)
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

    max_snatch = program.best_exercise_values[snatch]
    w1d2 = (
        WorkoutSession(id='W1D2')
        .add_component(
            SingleExercise(exercise=snatch).add_repeating_set(
                8, snatch.create_set(2, percentage=0.65)
            )
        )
        .add_component(
            SingleExercise(exercise=clean_jerk).add_repeating_set(
                5, clean_jerk.create_set(2, percentage=0.65)
            )
        )
        .add_component(
            SingleExercise(exercise=frontsquat).add_repeating_set(
                5, frontsquat.create_set(5, percentage=0.65)
            )
        )
        .add_component(
            ExerciseGroup(exercises=[pendlay_row, sg_bhtn_press]).add_repeating_group_sets(
                5,
                {
                    pendlay_row: pendlay_row.create_set(6, percentage=0.6),
                    sg_bhtn_press: sg_bhtn_press.create_set(10, weight=0.4 * max_snatch),
                },
            )
        )
    )

    w1d3 = (
        WorkoutSession(id='W1D3')
        .add_component(
            ExerciseGroup(exercises=[snatch_high_pull, low_hang_snatch]).add_repeating_group_sets(
                5,
                {
                    snatch_high_pull: snatch_high_pull.create_set(2, percentage=0.6),
                    low_hang_snatch: low_hang_snatch.create_set(2, percentage=0.6),
                },
            )
        )
        .add_component(
            SingleExercise(exercise=bulgarian_split_squat).add_repeating_set(
                4, bulgarian_split_squat.create_set(6, percentage=0.6)
            )
        )
        .add_component(
            SingleExercise(exercise=clean_pull).add_repeating_set(
                4, clean_pull.create_set(6, percentage=0.5)
            )
        )
        .add_component(
            SingleExercise(exercise=strict_press).add_repeating_set(
                4, strict_press.create_set(8, percentage=0.6)
            )
        )
        .add_component(
            ExerciseGroup(exercises=[pullup, side_plank_leg_raise]).add_repeating_group_sets(
                4,
                {
                    pullup: pullup.create_set(6),
                    side_plank_leg_raise: side_plank_leg_raise.create_set(8),
                },
            )
        )
    )

    program.add_workout_session(w1d1)
    program.add_workout_session(w1d2)
    program.add_workout_session(w1d3)

    return [w1d1, w1d2, w1d3]
