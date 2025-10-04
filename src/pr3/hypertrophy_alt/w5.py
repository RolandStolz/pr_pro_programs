from pr_pro.exercises.common import backsquat, bench_press, deadlift, power_clean
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise, ExerciseGroup
from pr_pro.workout_session import (
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)
from pr_pro.functions import Brzycki1RMCalculator

from pr3.hypertrophy.exercises import *  # noqa: F403


def _reps_from_percentage_and_rel_percentage(percentage: float, rel_percentage: float) -> float:
    calculator = Brzycki1RMCalculator()
    return calculator.max_reps_from_weight(percentage, rel_percentage)


def add_w5_sessions(program: Program, phase_1_program: Program) -> list[WorkoutSession]:
    w4d1 = phase_1_program.get_workout_session_by_id('W4D1')
    w4d2 = phase_1_program.get_workout_session_by_id('W4D2')
    w4d3 = phase_1_program.get_workout_session_by_id('W4D3')
    w4d4 = phase_1_program.get_workout_session_by_id('W4D4')
    assert w4d1 and w4d2 and w4d3 and w4d4

    d1 = (
        WorkoutSession(id='W5D1')
        .add_component(
            SingleExercise(
                exercise=hurdle_jumps_to_box, notes='Box at around 60'
            ).add_repeating_set(5, hurdle_jumps_to_box.create_set(3))
        )
        .add_component(
            single_exercise_from_prev_session(w4d1, power_snatch, percentage=+0.05, reps=-1)
        )
        .add_component(
            SingleExercise(
                exercise=backsquat, notes='Adjust 1rm after last weeks test.'
            ).add_repeating_set(5, backsquat.create_set(5, percentage=0.725))
        )
        .add_component(
            ExerciseGroup(
                exercises=[reverse_hyperextension, pallof_press]
            ).add_repeating_group_sets(
                4,
                {
                    reverse_hyperextension: reverse_hyperextension.create_set(12),
                    pallof_press: pallof_press.create_set(10, weight=20),
                },
            )
        )
    )

    d2 = (
        WorkoutSession(id='W5D2')
        .add_component(
            SingleExercise(
                exercise=bench_press, notes='Adjust 1rm after last weeks test.'
            ).add_repeating_set(4, bench_press.create_set(6, percentage=0.725))
        )
        .add_component(single_exercise_from_prev_session(w4d2, weighted_pullup, reps=+1))
        .add_component(
            ExerciseGroup(exercises=[barbell_row, snatch_grip_btn_press]).add_repeating_group_sets(
                4,
                {
                    barbell_row: barbell_row.create_set(6, percentage=0.7),
                    snatch_grip_btn_press: snatch_grip_btn_press.create_set(6, weight=40),
                },
            )
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    d3 = (
        WorkoutSession(id='W5D3')
        .add_component(
            exercise_group_from_prev_session(
                w4d3,
                [snatch_high_pull, low_hang_power_snatch],
                percentage=(+0.05, +0.05),
                reps=(-1, -1),
            )
        )
        .add_component(
            exercise_group_from_prev_session(
                w4d4,
                [power_clean, push_press, jerk],
                percentage=(+0.025, +0.025, +0.025),
                # reps=(None, -1, None),
            )
        )
        .add_component(
            SingleExercise(exercise=backsquat).add_repeating_set(
                4,
                backsquat.create_set(reps=4, percentage=0.8),  # Maybe 0.775 if too heavy
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[single_leg_calf_raise, banded_toes_to_bar]
            ).add_repeating_group_sets(
                4,
                {
                    single_leg_calf_raise: single_leg_calf_raise.create_set(8, weight=40),
                    banded_toes_to_bar: banded_toes_to_bar.create_set(8),
                },
            )
        )
    )

    d4 = (
        WorkoutSession(id='W5D4')
        .add_component(
            SingleExercise(exercise=eurostep_to_box).add_repeating_set(
                5, eurostep_to_box.create_set(2)
            )
        )
        .add_component(
            SingleExercise(exercise=deadlift).add_repeating_set(
                5, deadlift.create_set(5, percentage=0.775)
            )
        )
        # .add_component(
        #     exercise_group_from_prev_session(
        #         w4d4, [power_clean, push_press, jerk], percentage=(+0.075, +0.075, +0.075)
        #     )
        # )
        .add_component(
            # single_exercise_from_prev_session(w4d4, bench_press, percentage=+0.05)
            SingleExercise(exercise=bench_press).add_repeating_set(
                4, bench_press.create_set(4, percentage=0.775)
            )
        )
        .add_component(
            SingleExercise(exercise=bulgarian_split_squats).add_repeating_set(
                4, bulgarian_split_squats.create_set(6, weight=60)
            )
        )
        # .add_component(
        #     exercise_group_from_prev_session(w4d4, [pullup, pushup, lunges]).set_notes(
        #         'Goal: 1 Minute faster than W3D4'
        #     )
        # )
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W5', [s.id for s in sessions])

    return sessions
