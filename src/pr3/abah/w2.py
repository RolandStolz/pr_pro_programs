from pr_pro.exercises.common import backsquat, bench_press, deadlift, pullup, pushup
from pr_pro.program import Program
from pr_pro.workout_session import (
    WorkoutSession,
    exercise_group_from_prev_session,
    single_exercise_from_prev_session,
)

from pr3.weightlifting_3_days.exercises import (
    box_jump,
    cable_pulldown,
    dumbbell_shoulder_press,
    dumbbell_split_squat,
    hanging_knee_raise,
    hip_thrust,
    pallov_press,
    pendlay_row,
    reverse_hyperextension,
    side_plank_leg_raise,
    squat_hold,
)


def get_w2_sessions(program: Program) -> list[WorkoutSession]:
    w1d1 = program.get_workout_session_by_id('W1D1')
    w1d2 = program.get_workout_session_by_id('W1D2')
    w1d3 = program.get_workout_session_by_id('W1D3')
    assert w1d1 and w1d2 and w1d3

    w2d1 = (
        WorkoutSession(id='W2D1')
        .add_component(single_exercise_from_prev_session(w1d1, box_jump, reps=+1))
        .add_component(single_exercise_from_prev_session(w1d1, backsquat, reps=-1, percentage=+0.1))
        .add_component(
            exercise_group_from_prev_session(
                w1d1, [pendlay_row, dumbbell_shoulder_press], reps=(+2, +2), rpe=(None, +1)
            ).set_notes('Same weight as last weak for shoulder press.')
        )
        .add_component(
            exercise_group_from_prev_session(w1d1, [hip_thrust, side_plank_leg_raise], reps=(+2, 0))
        )
    )

    w2d2 = (
        WorkoutSession(id='W2D2')
        .add_component(single_exercise_from_prev_session(w1d2, deadlift, percentage=+0.05))
        .add_component(
            single_exercise_from_prev_session(w1d2, dumbbell_split_squat).set_notes(
                'Same weight as last week'
            )
        )
        .add_component(exercise_group_from_prev_session(w1d2, [pullup, pushup], reps=(+1, +2)))
        .add_component(
            exercise_group_from_prev_session(
                w1d2, [cable_pulldown, pallov_press], reps=(+2, +2)
            ).set_notes('Same weight as last week.')
        )
    )

    w2d3 = (
        WorkoutSession(id='W2D3')
        .add_component(single_exercise_from_prev_session(w1d3, squat_hold))
        .add_component(single_exercise_from_prev_session(w1d3, backsquat, reps=+2))
        .add_component(single_exercise_from_prev_session(w1d3, deadlift, percentage=+0.1))
        .add_component(
            single_exercise_from_prev_session(w1d3, bench_press, reps=-2, percentage=+0.05)
        )
        .add_component(
            exercise_group_from_prev_session(
                w1d3, [hanging_knee_raise, reverse_hyperextension], reps=(+2, +2)
            )
        )
    )

    program.add_workout_session(w2d1)
    program.add_workout_session(w2d2)
    program.add_workout_session(w2d3)

    return [w2d1, w2d2, w2d3]
