from pr_pro.exercises.common import (
    backsquat,
    bench_press,
    deadlift,
    power_clean,
    pullup,
    pushup,
)
from pr_pro.program import Program
from pr_pro.workout_component import ExerciseGroup
from pr_pro.workout_session import (
    WorkoutSession,
    exercise_group_from_prev_session,
    single_exercise_from_prev_session,
)

from pr_pro_programs.abah.exercises import (
    banded_side_plank_leg_raise,
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


def get_w5_sessions(program: Program) -> list[WorkoutSession]:
    w4d1 = program.get_workout_session_by_id("W4D1")
    w4d2 = program.get_workout_session_by_id("W4D2")
    w4d3 = program.get_workout_session_by_id("W4D3")
    assert w4d1 and w4d2 and w4d3

    d1 = (
        WorkoutSession(id="W5D1")
        .add_component(single_exercise_from_prev_session(w4d1, cmj))
        .add_component(
            single_exercise_from_prev_session(w4d1, power_clean, weight=+5).set_notes("")
        )
        .add_component(
            single_exercise_from_prev_session(w4d1, backsquat, reps=-1, sets=+1, percentage=+0.05)
        )
        .add_component(
            exercise_group_from_prev_session(
                w4d1, [pendlay_row, dumbbell_shoulder_press], reps=(-3, -2), percentage=(+0.1, None)
            ).set_notes("Heavier dumbbell for shoulder press.")
        )
    )

    exercise_group = w4d2.get_component_by_exercise_group([hip_thrust, side_plank_leg_raise])
    hip_thrust_weight: int = exercise_group.exercise_sets_dict[hip_thrust][0].weight  # type: ignore

    d2 = (
        WorkoutSession(id="W5D2")
        .add_component(single_exercise_from_prev_session(w4d2, power_clean, weight=+5))
        .add_component(single_exercise_from_prev_session(w4d2, backsquat, percentage=+0.05))
        .add_component(
            ExerciseGroup(exercises=[hip_thrust, banded_side_plank_leg_raise])
            .add_repeating_group_sets(
                4,
                {
                    hip_thrust: hip_thrust.create_set(6, weight=hip_thrust_weight + 10),
                    banded_side_plank_leg_raise: banded_side_plank_leg_raise.create_set(10),
                },
            )
            .set_notes("Light band")
        )
        .add_component(
            exercise_group_from_prev_session(w4d2, [pullup, pushup], reps=(+1, +2)).set_notes(
                "Normal grip for pullup"
            )
        )
    )

    d3 = (
        WorkoutSession(id="W5D3")
        .add_component(single_exercise_from_prev_session(w4d3, single_leg_box_jump, reps=+1))
        .add_component(
            single_exercise_from_prev_session(w4d3, deadlift, reps=-3, sets=+1, percentage=+0.075)
        )
        .add_component(
            single_exercise_from_prev_session(w4d3, dumbbell_split_squat, rpe=+1).set_notes(
                "Next heavier dumbbell"
            )
        )
        .add_component(single_exercise_from_prev_session(w4d3, bench_press, reps=+1, sets=-1))
        .add_component(
            exercise_group_from_prev_session(
                w4d3, [hanging_knee_raise, reverse_hyperextension], reps=(+2, -4)
            ).set_notes("Pause 1s for reverse hyperextension.")
        )
    )

    program.add_workout_session(d1)
    program.add_workout_session(d2)
    program.add_workout_session(d3)

    return [d1, d2, d3]
