from pr_pro.exercises.common import backsquat, bench_press, deadlift, power_clean, pullup
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise
from pr_pro.workout_session import (
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)
from pr3.hypertrophy.exercises import *  # noqa: F403


def add_w6_sessions(program: Program) -> list[WorkoutSession]:
    w5d1 = program.get_workout_session_by_id('W5D1')
    w5d2 = program.get_workout_session_by_id('W5D2')
    w5d3 = program.get_workout_session_by_id('W5D3')
    w5d4 = program.get_workout_session_by_id('W5D4')
    assert w5d1 and w5d2 and w5d3 and w5d4

    d1 = (
        WorkoutSession(id='W6D1')
        .add_component(single_exercise_from_prev_session(w5d1, hurdle_jumps_to_box))
        .add_component(single_exercise_from_prev_session(w5d1, power_snatch, percentage=+0.03))
        .add_component(single_exercise_from_prev_session(w5d1, backsquat, percentage=+0.025))
        .add_component(
            exercise_group_from_prev_session(
                w5d1, [reverse_hyperextension, pallof_press], reps=(-6, +2)
            ).set_notes('1s paused reverse hypers')
        )
    )

    d2 = (
        WorkoutSession(id='W6D2')
        .add_component(single_exercise_from_prev_session(w5d2, bench_press, percentage=+0.04))
        .add_component(single_exercise_from_prev_session(w5d2, weighted_pullup, weight=+5))
        .add_component(
            exercise_group_from_prev_session(
                w5d2, [barbell_row, snatch_grip_btn_press], reps=(+2, +2)
            )
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    d3 = (
        WorkoutSession(id='W6D3')
        # .add_component(single_exercise_from_prev_session(w5d3, eurostep_to_box, reps=+1))
        .add_component(
            exercise_group_from_prev_session(
                w5d3, [snatch_high_pull, low_hang_power_snatch], percentage=(+0.05, +0.05)
            )
        )
        .add_component(single_exercise_from_prev_session(w5d3, backsquat, percentage=+0.04))
        .add_component(single_exercise_from_prev_session(w5d3, leg_curl_machine, reps=+2))
        .add_component(
            exercise_group_from_prev_session(
                w5d3, [single_leg_calf_raise, banded_toes_to_bar], reps=(+2, +2)
            )
        )
    )

    d4 = (
        WorkoutSession(id='W6D4')
        .add_component(
            exercise_group_from_prev_session(
                w5d4,
                [power_clean, push_press, jerk],
                percentage=(+0.04, +0.04, +0.04),
                reps=(-1, -1, None),
            )
        )
        .add_component(
            # TODO: check
            single_exercise_from_prev_session(w5d4, deadlift, percentage=+0.025)
        )
        .add_component(single_exercise_from_prev_session(w5d4, bench_press, percentage=+0.04))
        .add_component(single_exercise_from_prev_session(w5d4, bulgarian_split_squats, weight=+5))
        .add_component(single_exercise_from_prev_session(w5d4, pullup, reps=+1))
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W6', [s.id for s in sessions])

    return sessions
