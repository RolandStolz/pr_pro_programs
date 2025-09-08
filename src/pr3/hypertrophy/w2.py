from pr_pro.exercises.common import backsquat, pullup, bench_press, deadlift, power_clean, pushup
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise
from pr_pro.workout_session import (
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)

from pr3.hypertrophy.exercises import *  # noqa: F403


def add_w2_sessions(program: Program) -> list[WorkoutSession]:
    w1d1 = program.get_workout_session_by_id('W1D1')
    w1d2 = program.get_workout_session_by_id('W1D2')
    w1d3 = program.get_workout_session_by_id('W1D3')
    w1d4 = program.get_workout_session_by_id('W1D4')
    assert w1d1 and w1d2 and w1d3 and w1d4

    d1 = (
        WorkoutSession(id='W2D1')
        .add_component(single_exercise_from_prev_session(w1d1, box_jump, reps=+1))
        .add_component(single_exercise_from_prev_session(w1d1, power_snatch, percentage=+0.05))
        .add_component(single_exercise_from_prev_session(w1d1, backsquat, percentage=+0.05))
        .add_component(
            exercise_group_from_prev_session(
                w1d1, [reverse_hyperextension, russian_twist], reps=(+2, +2)
            )
        )
    )

    d2 = (
        WorkoutSession(id='W2D2')
        .add_component(single_exercise_from_prev_session(w1d2, bench_press, percentage=+0.05))
        .add_component(single_exercise_from_prev_session(w1d2, pullup, reps=+2))
        .add_component(
            exercise_group_from_prev_session(w1d2, [bo_dumbbell_row, dumbbell_press], reps=(+2, +2))
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    d3 = (
        WorkoutSession(id='W2D3')
        .add_component(single_exercise_from_prev_session(w1d3, backsquat, percentage=+0.05))
        .add_component(single_exercise_from_prev_session(w1d3, muscle_snatch, percentage=+0.075))
        .add_component(single_exercise_from_prev_session(w1d3, deadlift, reps=-2, percentage=+0.1))
        .add_component(
            exercise_group_from_prev_session(
                w1d3, [calf_raise, side_plank_leg_raise], reps=(None, +2), weight=(+10, None)
            )
        )
    )

    d4 = (
        WorkoutSession(id='W2D4')
        .add_component(single_exercise_from_prev_session(w1d4, eurostep_to_land, reps=+1))
        .add_component(
            exercise_group_from_prev_session(
                w1d4, [power_clean, push_press], percentage=(+0.1, +0.1)
            )
        )
        .add_component(single_exercise_from_prev_session(w1d4, bench_press, percentage=+0.075))
        .add_component(
            exercise_group_from_prev_session(w1d4, [pullup, pushup, lunges]).set_notes(
                'Goal is one minute faster than W1D4'
            )
        )
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W2', [s.id for s in sessions])

    return sessions
