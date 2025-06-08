from pr_pro.exercises.common import backsquat, pullup
from pr_pro.program import Program
from pr_pro.workout_session import (
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)

from pr3.weightlifting_3_days.exercises import (
    box_jump,
    bulgarian_split_squat,
    clean_jerk,
    clean_pull,
    frontsquat,
    incline_dumbbell_press,
    low_hang_snatch,
    pendlay_row,
    power_snatch,
    reverse_hyperextension,
    russian_twist,
    sg_bhtn_press,
    side_plank_leg_raise,
    snatch,
    snatch_high_pull,
    strict_press,
)


def get_w3_sessions(program: Program) -> list[WorkoutSession]:
    w2d1 = program.get_workout_session_by_id('W2D1')
    w2d2 = program.get_workout_session_by_id('W2D2')
    w2d3 = program.get_workout_session_by_id('W2D3')
    assert w2d1 and w2d2 and w2d3

    d1 = (
        WorkoutSession(id='W3D1')
        .add_component(
            single_exercise_from_prev_session(w2d1, box_jump, sets=-2)
            .add_set(box_jump.create_set(1))
            .set_notes('Proceed to max height')
        )
        .add_component(
            single_exercise_from_prev_session(w2d1, power_snatch, percentage=+0.05, reps=-1)
        )
        .add_component(
            single_exercise_from_prev_session(w2d1, backsquat, percentage=+0.05).set_notes(
                'First 4 paused'
            )
        )
        .add_component(
            single_exercise_from_prev_session(
                w2d1, incline_dumbbell_press, rpe=+1, sets=-4
            ).set_notes('+2-5 kg')
        )
        .add_component(
            exercise_group_from_prev_session(
                w2d1, [reverse_hyperextension, russian_twist], reps=(+2, +2)
            )
        )
    )

    d2 = (
        WorkoutSession(id='W3D2')
        .add_component(single_exercise_from_prev_session(w2d2, snatch, percentage=+0.05))
        .add_component(single_exercise_from_prev_session(w2d2, clean_jerk, percentage=+0.05))
        .add_component(
            single_exercise_from_prev_session(w2d2, frontsquat, percentage=+0.05, sets=-1, reps=+1)
        )
        .add_component(
            exercise_group_from_prev_session(
                w2d2,
                [pendlay_row, sg_bhtn_press],
                reps=(-2, -4),
                weight=(None, +5),
                percentage=(+0.1, None),
            )
        )
    )

    d3 = (
        WorkoutSession(id='W3D3')
        .add_component(
            exercise_group_from_prev_session(
                w2d3, [snatch_high_pull, low_hang_snatch], percentage=(+0.05, +0.05), reps=(-1, +1)
            )
        )
        .add_component(
            single_exercise_from_prev_session(w2d3, bulgarian_split_squat, reps=-3, percentage=+0.1)
        )
        .add_component(single_exercise_from_prev_session(w2d3, clean_pull, percentage=+0.05))
        .add_component(single_exercise_from_prev_session(w2d3, strict_press, reps=+2))
        .add_component(
            exercise_group_from_prev_session(w2d3, [pullup, side_plank_leg_raise], reps=(+1, +2))
        )
    )

    program.add_workout_session(d1)
    program.add_workout_session(d2)
    program.add_workout_session(d3)

    return [d1, d2, d3]
