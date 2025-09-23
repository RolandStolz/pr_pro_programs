from pr_pro.exercises.common import backsquat, pullup, bench_press, deadlift, power_clean, pushup
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise
from pr_pro.workout_session import (
    ExerciseGroup,
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)

from pr3.hypertrophy.exercises import *


def add_w3_sessions(program: Program) -> list[WorkoutSession]:
    w2d1 = program.get_workout_session_by_id('W2D1')
    w2d2 = program.get_workout_session_by_id('W2D2')
    w2d3 = program.get_workout_session_by_id('W2D3')
    w2d4 = program.get_workout_session_by_id('W2D4')
    assert w2d1 and w2d2 and w2d3 and w2d4

    d1 = (
        WorkoutSession(id='W3D1')
        .add_component(
            SingleExercise(exercise=pogo_jump).add_repeating_set(5, pogo_jump.create_set(5))
        )
        .add_component(single_exercise_from_prev_session(w2d1, power_snatch, percentage=+0.075))
        .add_component(
            single_exercise_from_prev_session(w2d1, backsquat, percentage=+0.05, reps=-2)
        )
        .add_component(
            exercise_group_from_prev_session(
                w2d1, [reverse_hyperextension, russian_twist], reps=(+2, +2)
            )
        )
    )

    d2 = (
        WorkoutSession(id='W3D2')
        .add_component(
            single_exercise_from_prev_session(w2d2, bench_press, percentage=+0.1, reps=-2, sets=+1)
        )
        .add_component(single_exercise_from_prev_session(w2d2, pullup, reps=+1))
        .add_component(
            exercise_group_from_prev_session(
                w2d2, [bo_dumbbell_row, dumbbell_press], reps=(-2, -2), weight=(+5, +4)
            ).set_notes('Add some weight from W2D2. Should be somewhat tough.')
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    d3 = (
        WorkoutSession(id='W3D3')
        .add_component(single_exercise_from_prev_session(w2d3, backsquat, percentage=+0.025))
        .add_component(single_exercise_from_prev_session(w2d3, muscle_snatch, percentage=+0.05))
        .add_component(
            single_exercise_from_prev_session(w2d3, deadlift, reps=-2, percentage=+0.075)
        )
        .add_component(
            exercise_group_from_prev_session(
                w2d3, [calf_raise, side_plank_leg_raise], reps=(-2, +2), weight=(+10, None)
            )
        )
    )

    d4 = (
        WorkoutSession(id='W3D4')
        .add_component(single_exercise_from_prev_session(w2d4, eurostep_to_land, reps=+1))
        .add_component(
            ExerciseGroup(exercises=[power_clean, push_press, jerk]).add_repeating_group_sets(
                4,
                {
                    power_clean: power_clean.create_set(3, percentage=0.675),
                    push_press: push_press.create_set(2, percentage=0.675),
                    jerk: jerk.create_set(1, percentage=0.675),
                },
            )
        )
        .add_component(single_exercise_from_prev_session(w2d4, bench_press, percentage=+0.05))
        # .add_component(SingleExercise(exercise=bench_press).add_repeating_set(4, bench_press.create_set(4, percentage=0.8)))
        .add_component(
            exercise_group_from_prev_session(w2d4, [pullup, pushup, lunges], reps=(+10, +20, +20))
        )
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W3', [s.id for s in sessions])

    return sessions
