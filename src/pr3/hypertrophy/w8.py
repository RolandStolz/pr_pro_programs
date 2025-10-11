from pr_pro.exercises.common import backsquat, bench_press, deadlift, power_clean, pullup
from pr_pro.functions import Epley1RMCalculator
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise
from pr_pro.workout_session import (
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)
from pr3.hypertrophy.exercises import *  # noqa: F403


def add_w8_sessions(program: Program) -> list[WorkoutSession]:
    w7d1 = program.get_workout_session_by_id('W7D1')
    w7d2 = program.get_workout_session_by_id('W7D2')
    w7d3 = program.get_workout_session_by_id('W7D3')
    w7d4 = program.get_workout_session_by_id('W7D4')
    assert w7d1 and w7d2 and w7d3 and w7d4

    d1 = (
        WorkoutSession(id='W8D1')
        .add_component(single_exercise_from_prev_session(w7d1, hurdle_jumps_to_box))
        .add_component(
            single_exercise_from_prev_session(w7d1, power_snatch, percentage=+0.03, sets=-1)
        )
        .add_component(
            single_exercise_from_prev_session(w7d1, backsquat, percentage=+0.03, reps=-2)
        )
        .add_component(
            exercise_group_from_prev_session(
                w7d1, [reverse_hyperextension, pallof_press], reps=(+1, +2)
            ).set_notes('1s paused reverse hypers')
        )
    )

    d2 = (
        WorkoutSession(id='W8D2')
        .add_component(
            single_exercise_from_prev_session(w7d4, bench_press, percentage=+0.025, reps=-1)
        )
        .add_component(single_exercise_from_prev_session(w7d2, weighted_pullup, reps=-2, weight=+5))
        .add_component(
            exercise_group_from_prev_session(
                w7d2, [barbell_row, snatch_grip_btn_press], reps=(+2, +2)
            )
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    calculator = Epley1RMCalculator()
    # calculator = Brzycki1RMCalculator()
    d3 = (
        WorkoutSession(id='W8D3')
        .add_component(
            exercise_group_from_prev_session(
                w7d3, [snatch_high_pull, low_hang_power_snatch], percentage=(+0.025, +0.025)
            )
        )
        .add_component(
            SingleExercise(exercise=backsquat)
            .add_set(
                backsquat.create_set(reps=5, percentage=calculator.max_weight_from_reps(1.0, 5))
            )
            .add_set(
                backsquat.create_set(reps=8, percentage=calculator.max_weight_from_reps(1.0, 8))
            )
        )
        .add_component(
            single_exercise_from_prev_session(w7d3, leg_curl_machine, reps=-2, weight=+10)
        )
        .add_component(
            exercise_group_from_prev_session(
                w7d3, [single_leg_calf_raise, banded_toes_to_bar], reps=(+2, +2)
            )
        )
    )

    print(calculator.max_weight_from_reps(1.0, 5))
    d4 = (
        WorkoutSession(id='W8D4')
        .add_component(
            exercise_group_from_prev_session(
                w7d4,
                [power_clean, push_press, jerk],
                percentage=(+0.025, +0.025, +0.025),
            )
        )
        .add_component(
            SingleExercise(exercise=bench_press)
            .add_set(
                bench_press.create_set(reps=5, percentage=calculator.max_weight_from_reps(1.0, 5))
            )
            .add_set(
                bench_press.create_set(reps=8, percentage=calculator.max_weight_from_reps(1.0, 8))
            )
        )
        .add_component(single_exercise_from_prev_session(w7d4, deadlift, percentage=+0.05))
        .add_component(single_exercise_from_prev_session(w7d4, bulgarian_split_squats, weight=+5))
        .add_component(single_exercise_from_prev_session(w7d4, pullup))
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W8', [s.id for s in sessions])

    return sessions
