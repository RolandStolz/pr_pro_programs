import datetime

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
    box_jump,
    dumbbell_shoulder_press,
    dumbbell_split_squat,
    hanging_knee_raise,
    hip_thrust,
    pendlay_row,
    reverse_hyperextension,
    side_plank_leg_raise,
    squat_hold,
)


def get_w3_sessions(program: Program) -> list[WorkoutSession]:
    w2d1 = program.get_workout_session_by_id('W2D1')
    w2d2 = program.get_workout_session_by_id('W2D2')
    w2d3 = program.get_workout_session_by_id('W2D3')
    assert w2d1 and w2d2 and w2d3

    d1 = (
        WorkoutSession(id='W3D1')
        .add_component(
            single_exercise_from_prev_session(w2d1, box_jump, reps=-2).set_notes(
                'Difficult height.'
            )
        )
        .add_component(
            SingleExercise(exercise=power_clean).add_repeating_set(5, power_clean.create_set(3, 20))
        )
        .add_component(
            single_exercise_from_prev_session(w2d1, backsquat, reps=-1, sets=+1, percentage=+0.05)
        )
        .add_component(
            exercise_group_from_prev_session(
                w2d1, [pendlay_row, dumbbell_shoulder_press], reps=(0, -4), percentage=(+0.05, None)
            ).set_notes('Heavier dumbbell for shoulder press')
        )
    )

    d2 = (
        WorkoutSession(id='W3D2')
        .add_component(
            SingleExercise(exercise=power_clean)
            .add_repeating_set(5, power_clean.create_set(3, 20))
            .set_notes('+5kg if you feel good.')
        )
        .add_component(
            single_exercise_from_prev_session(w2d2, dumbbell_split_squat, rpe=+1).set_notes(
                'Next heavier dumbbell'
            )
        )
        .add_component(
            exercise_group_from_prev_session(
                w2d1, [hip_thrust, side_plank_leg_raise], reps=(+2, +2)
            )
        )
        .add_component(exercise_group_from_prev_session(w2d2, [pullup, pushup], reps=(0, +2)))
    )

    d3 = (
        WorkoutSession(id='W3D3')
        .add_component(
            single_exercise_from_prev_session(
                w2d3, squat_hold, duration=datetime.timedelta(seconds=30)
            )
        )
        .add_component(single_exercise_from_prev_session(w2d3, backsquat, percentage=+0.05))
        .add_component(
            SingleExercise(exercise=deadlift).add_repeating_set(
                5, deadlift.create_set(5, percentage=0.7)
            )
        )
        .add_component(
            single_exercise_from_prev_session(w2d3, bench_press, reps=-2, percentage=+0.05)
        )
        .add_component(
            exercise_group_from_prev_session(
                w2d3, [hanging_knee_raise, reverse_hyperextension], reps=(+2, +2)
            )
        )
    )

    program.add_workout_session(d1)
    program.add_workout_session(d2)
    program.add_workout_session(d3)

    return [d1, d2, d3]
