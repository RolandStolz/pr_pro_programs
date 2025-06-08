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
    cmj,
    dumbbell_shoulder_press,
    dumbbell_split_squat,
    hanging_knee_raise,
    hip_thrust,
    pendlay_row,
    reverse_hyperextension,
    side_plank_leg_raise,
    single_leg_box_jump,
)


def get_w4_sessions(program: Program) -> list[WorkoutSession]:
    w3d1 = program.get_workout_session_by_id('W3D1')
    w3d2 = program.get_workout_session_by_id('W3D2')
    w3d3 = program.get_workout_session_by_id('W3D3')
    assert w3d1 and w3d2 and w3d3

    d1 = (
        WorkoutSession(id='W4D1')
        .add_component(
            SingleExercise(exercise=cmj)
            .add_repeating_set(5, cmj.create_set(5))
            .set_notes('First 3 100% power.')
        )
        .add_component(
            single_exercise_from_prev_session(w3d1, power_clean, weight=+5).set_notes(
                'Work up to 30kg if possible.'
            )
        )
        .add_component(single_exercise_from_prev_session(w3d3, backsquat, reps=-4, percentage=+0.1))
        .add_component(
            exercise_group_from_prev_session(
                w3d1, [pendlay_row, dumbbell_shoulder_press], reps=(+2, +2)
            ).set_notes('Same weight as last week.')
        )
    )

    d2 = (
        WorkoutSession(id='W4D2')
        .add_component(
            single_exercise_from_prev_session(w3d2, power_clean, weight=+10, reps=-1).set_notes('')
        )
        .add_component(single_exercise_from_prev_session(w3d1, backsquat, percentage=+0.05))
        .add_component(
            exercise_group_from_prev_session(
                w3d2, [hip_thrust, side_plank_leg_raise], reps=(-4, +3), weight=(+10, None)
            )
        )
        .add_component(
            exercise_group_from_prev_session(w3d2, [pullup, pushup], reps=(-1, 0)).set_notes(
                'Normal grip for pullup'
            )
        )
    )

    d3 = (
        WorkoutSession(id='W4D3')
        .add_component(
            SingleExercise(exercise=single_leg_box_jump).add_repeating_set(
                5, single_leg_box_jump.create_set(3)
            )
        )
        .add_component(single_exercise_from_prev_session(w3d3, deadlift, percentage=+0.1))
        .add_component(
            single_exercise_from_prev_session(w3d2, dumbbell_split_squat, reps=-2).set_notes(
                'Next heavier dumbbell'
            )
        )
        .add_component(
            single_exercise_from_prev_session(w3d3, bench_press, reps=-2, percentage=+0.1)
        )
        .add_component(
            exercise_group_from_prev_session(
                w3d3, [hanging_knee_raise, reverse_hyperextension], reps=(+2, +2)
            )
        )
    )

    program.add_workout_session(d1)
    program.add_workout_session(d2)
    program.add_workout_session(d3)

    return [d1, d2, d3]
