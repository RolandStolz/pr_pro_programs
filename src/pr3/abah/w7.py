from pr3.weightlifting_3_days.exercises import (
    banded_side_plank_leg_raise,
    dumbbell_shoulder_press,
    dumbbell_split_squat,
    hanging_knee_raise,
    hip_thrust,
    pendlay_row,
    reverse_hyperextension,
    eurostep_to_vert_jump,
    depth_jump,
)
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


def get_w7_sessions(program: Program) -> list[WorkoutSession]:
    w6d1 = program.get_workout_session_by_id('W6D1')
    w6d2 = program.get_workout_session_by_id('W6D2')
    w6d3 = program.get_workout_session_by_id('W6D3')
    assert w6d1 and w6d2 and w6d3

    d1 = (
        WorkoutSession(id='W7D1')
        .add_component(
            SingleExercise(exercise=depth_jump)
            .add_repeating_set(5, depth_jump.create_set(3, distance=0.15))
            .set_notes('Minimize ground contact time.')
        )
        .add_component(
            single_exercise_from_prev_session(w6d1, power_clean, sets=-2, weight=+5)
            .add_set(power_clean.create_set(1, 0))
            .set_notes('Proceed to max.')
        )
        .add_component(
            single_exercise_from_prev_session(w6d1, backsquat, reps=-2, sets=-2, percentage=+0.05)
        )
        .add_component(
            exercise_group_from_prev_session(
                w6d1, [pendlay_row, dumbbell_shoulder_press], reps=(0, +2), percentage=(+0.05, None)
            ).set_notes('Same weight as last week.')
        )
    )

    d2 = (
        WorkoutSession(id='W7D2')
        .add_component(single_exercise_from_prev_session(w6d2, power_clean, weight=+5))
        .add_component(
            single_exercise_from_prev_session(w6d2, backsquat, percentage=+0.05, reps=-1, sets=-1)
        )
        .add_component(
            exercise_group_from_prev_session(w6d2, [hip_thrust, banded_side_plank_leg_raise])
        )
        .add_component(
            exercise_group_from_prev_session(w6d2, [pullup, pushup], reps=(0, +3)).set_notes(
                'Normal grip for pullup'
            )
        )
    )

    d3 = (
        WorkoutSession(id='W7D3')
        .add_component(single_exercise_from_prev_session(w6d3, eurostep_to_vert_jump))
        .add_component(single_exercise_from_prev_session(w6d3, deadlift, sets=-2, percentage=+0.05))
        .add_component(
            single_exercise_from_prev_session(w6d3, dumbbell_split_squat, reps=-1).set_notes(
                'Next heavier dumbbell'
            )
        )
        .add_component(
            single_exercise_from_prev_session(w6d3, bench_press, reps=-1, sets=-1, percentage=+0.05)
        )
        .add_component(
            exercise_group_from_prev_session(
                w6d3, [hanging_knee_raise, reverse_hyperextension], reps=(+2, +2)
            ).set_notes('Pause 1s for reverse hyperextension.')
        )
    )

    program.add_workout_session(d1)
    program.add_workout_session(d2)
    program.add_workout_session(d3)

    return [d1, d2, d3]
