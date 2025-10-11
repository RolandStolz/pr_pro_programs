from pr_pro.exercises.common import backsquat, bench_press, deadlift, power_clean, pullup
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise
from pr_pro.workout_session import (
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)
from pr3.hypertrophy.exercises import *  # noqa: F403


def add_w7_sessions(program: Program) -> list[WorkoutSession]:
    w6d1 = program.get_workout_session_by_id('W6D1')
    w6d2 = program.get_workout_session_by_id('W6D2')
    w6d3 = program.get_workout_session_by_id('W6D3')
    w6d4 = program.get_workout_session_by_id('W6D4')
    assert w6d1 and w6d2 and w6d3 and w6d4

    d1 = (
        WorkoutSession(id='W7D1')
        .add_component(single_exercise_from_prev_session(w6d1, hurdle_jumps_to_box))
        .add_component(single_exercise_from_prev_session(w6d1, power_snatch, percentage=+0.03))
        .add_component(single_exercise_from_prev_session(w6d1, backsquat, percentage=+0.04))
        .add_component(
            exercise_group_from_prev_session(
                w6d1, [reverse_hyperextension, pallof_press], reps=(+1, -4), weight=(None, +5)
            ).set_notes('1s paused reverse hypers')
        )
    )

    d2 = (
        WorkoutSession(id='W7D2')
        .add_component(single_exercise_from_prev_session(w6d2, bench_press, percentage=+0.03))
        .add_component(single_exercise_from_prev_session(w6d2, weighted_pullup, reps=+1, sets=-1))
        .add_component(
            exercise_group_from_prev_session(
                w6d2,
                [barbell_row, snatch_grip_btn_press],
                reps=(-2, -2),
                percentage=(+0.05, None),
                weight=(None, +2.5),
            )
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    d3 = (
        WorkoutSession(id='W7D3')
        .add_component(
            exercise_group_from_prev_session(
                w6d3, [snatch_high_pull, low_hang_power_snatch], percentage=(+0.05, +0.05)
            )
        )
        .add_component(single_exercise_from_prev_session(w6d3, backsquat, percentage=+0.04))
        .add_component(single_exercise_from_prev_session(w6d3, leg_curl_machine, reps=+2))
        .add_component(
            exercise_group_from_prev_session(
                w6d3,
                [single_leg_calf_raise, banded_toes_to_bar],
                weight=(+5, None),
                reps=(-2, None),
            )
        )
    )

    d4 = (
        WorkoutSession(id='W7D4')
        .add_component(
            exercise_group_from_prev_session(
                w6d4,
                [power_clean, push_press, jerk],
                percentage=(+0.025, +0.025, +0.025),
            )
        )
        .add_component(
            single_exercise_from_prev_session(w6d4, deadlift, reps=-2, percentage=+0.075)
        )
        .add_component(single_exercise_from_prev_session(w6d4, bench_press, percentage=+0.04))
        .add_component(single_exercise_from_prev_session(w6d4, bulgarian_split_squats, weight=+5))
        .add_component(single_exercise_from_prev_session(w6d4, pullup, reps=+1))
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W7', [s.id for s in sessions])

    return sessions
