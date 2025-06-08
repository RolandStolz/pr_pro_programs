from pr_pro.exercises.common import (
    backsquat,
    bench_press,
    deadlift,
    power_clean,
    pullup,
    pushup,
)
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise
from pr_pro.workout_session import (
    WorkoutSession,
    exercise_group_from_prev_session,
    single_exercise_from_prev_session,
)

from pr3.abah.exercises import (
    banded_side_plank_leg_raise,
    box_jump,
    cmj,
    dumbbell_shoulder_press,
    dumbbell_split_squat,
    eurostep_to_vert_jump,
    hanging_knee_raise,
    hip_thrust,
    pendlay_row,
    reverse_hyperextension,
)


def get_w6_sessions(program: Program) -> list[WorkoutSession]:
    w5d1 = program.get_workout_session_by_id('W5D1')
    w5d2 = program.get_workout_session_by_id('W5D2')
    w5d3 = program.get_workout_session_by_id('W5D3')
    assert w5d1 and w5d2 and w5d3

    d1 = (
        WorkoutSession(id='W6D1')
        .add_component(single_exercise_from_prev_session(w5d1, cmj, sets=-2))
        .add_component(
            SingleExercise(exercise=box_jump)
            .add_set(box_jump.create_set(1))
            .set_notes('Go to max height.')
        )
        .add_component(single_exercise_from_prev_session(w5d1, power_clean, weight=+5))
        .add_component(single_exercise_from_prev_session(w5d1, backsquat, percentage=+0.025))
        .add_component(
            exercise_group_from_prev_session(
                w5d1, [pendlay_row, dumbbell_shoulder_press], reps=(+1, +2)
            ).set_notes('Same weight as last week.')
        )
    )

    d2 = (
        WorkoutSession(id='W6D2')
        .add_component(single_exercise_from_prev_session(w5d2, power_clean, weight=+5))
        .add_component(single_exercise_from_prev_session(w5d2, backsquat, percentage=+0.05))
        .add_component(
            exercise_group_from_prev_session(
                w5d2, [hip_thrust, banded_side_plank_leg_raise], reps=(+4, 0), weight=(-10, None)
            )
        )
        .add_component(
            exercise_group_from_prev_session(w5d2, [pullup, pushup], reps=(+1, 0)).set_notes(
                'Normal grip for pullup'
            )
        )
    )

    d3 = (
        WorkoutSession(id='W6D3')
        .add_component(
            SingleExercise(exercise=eurostep_to_vert_jump).add_repeating_set(
                5, box_jump.create_set(2)
            )
        )
        .add_component(
            single_exercise_from_prev_session(w5d3, deadlift, reps=+1, sets=-1, percentage=+0.025)
        )
        .add_component(
            single_exercise_from_prev_session(w5d3, dumbbell_split_squat).set_notes(
                'Same weight as last week'
            )
        )
        .add_component(
            single_exercise_from_prev_session(w5d3, bench_press, reps=-1, sets=+1, percentage=+0.05)
        )
        .add_component(
            exercise_group_from_prev_session(
                w5d3, [hanging_knee_raise, reverse_hyperextension], reps=(-4, 0), weight=(+5, None)
            ).set_notes('Pause 1s for reverse hyperextension.')
        )
    )

    program.add_workout_session(d1)
    program.add_workout_session(d2)
    program.add_workout_session(d3)

    return [d1, d2, d3]
