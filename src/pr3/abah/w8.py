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
    depth_jump,
    dumbbell_shoulder_press,
    dumbbell_split_squat,
    eurostep_to_vert_jump,
    hanging_knee_raise,
    hip_thrust,
    pendlay_row,
    reverse_hyperextension,
)


def get_w8_sessions(program: Program) -> list[WorkoutSession]:
    w7d1 = program.get_workout_session_by_id('W7D1')
    w7d2 = program.get_workout_session_by_id('W7D2')
    w7d3 = program.get_workout_session_by_id('W7D3')
    assert w7d1 and w7d2 and w7d3

    d1 = (
        WorkoutSession(id='W8D1')
        .add_component(single_exercise_from_prev_session(w7d1, depth_jump, distance=+0.15))
        .add_component(
            single_exercise_from_prev_session(w7d1, power_clean, sets=-1, weight=+5).set_notes(
                'Use max weight from last week.'
            )
        )
        .add_component(
            SingleExercise(exercise=backsquat)
            .add_repeating_set(3, backsquat.create_set(2, percentage=0.7))
            .add_repeating_set(2, backsquat.create_set(1, percentage=0.8))
            .set_notes('Should be pretty easy')
        )
        .add_component(
            exercise_group_from_prev_session(
                w7d1,
                [pendlay_row, dumbbell_shoulder_press],
                reps=(+2, 0),
                rpe=(None, +1),
                sets=-1,
            ).set_notes('Heavier dumbbell for shoulder press.')
        )
    )

    d2 = (
        WorkoutSession(id='W8D2')
        .add_component(single_exercise_from_prev_session(w7d2, power_clean))
        .add_component(
            SingleExercise(exercise=backsquat)
            .add_set(backsquat.create_set(1, percentage=0))
            .set_notes('Proceed to max.')
        )
        .add_component(
            exercise_group_from_prev_session(
                w7d2, [hip_thrust, banded_side_plank_leg_raise], sets=-1
            )
        )
        .add_component(
            exercise_group_from_prev_session(w7d2, [pullup, pushup], reps=(-2, -9)).set_notes(
                'Explosive pullups and pushups'
            )
        )
    )

    d3 = (
        WorkoutSession(id='W8D3')
        .add_component(single_exercise_from_prev_session(w7d3, eurostep_to_vert_jump, reps=+1))
        .add_component(
            SingleExercise(exercise=deadlift)
            .add_set(deadlift.create_set(1, percentage=0))
            .set_notes('Proceed to max.')
        )
        .add_component(
            single_exercise_from_prev_session(
                w7d3, dumbbell_split_squat, rpe=+1, sets=-1
            ).set_notes('Next heavier dumbbell')
        )
        .add_component(
            SingleExercise(exercise=bench_press)
            .add_set(bench_press.create_set(3, relative_percentage=1.1))
            .set_notes('Proceed to three reps max.')
        )
        .add_component(
            exercise_group_from_prev_session(
                w7d3, [hanging_knee_raise, reverse_hyperextension]
            ).set_notes('Pause 1s for reverse hyperextension.')
        )
    )

    program.add_workout_session(d1)
    program.add_workout_session(d2)
    program.add_workout_session(d3)

    return [d1, d2, d3]
