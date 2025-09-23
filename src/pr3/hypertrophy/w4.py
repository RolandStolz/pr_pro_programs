from pr_pro.exercises.common import backsquat, pullup, bench_press, deadlift, power_clean, pushup
from pr_pro.program import Program
from pr_pro.workout_component import SingleExercise, ExerciseGroup
from pr_pro.workout_session import (
    WorkoutSession,
    single_exercise_from_prev_session,
    exercise_group_from_prev_session,
)
from pr_pro.functions import Brzycki1RMCalculator

from pr3.hypertrophy.exercises import *  # noqa: F403


def _reps_from_percentage_and_rel_percentage(percentage: float, rel_percentage: float) -> float:
    calculator = Brzycki1RMCalculator()
    return calculator.max_reps_from_weight(percentage, rel_percentage)


def add_w4_sessions(program: Program) -> list[WorkoutSession]:
    w3d1 = program.get_workout_session_by_id('W3D1')
    w3d2 = program.get_workout_session_by_id('W3D2')
    w3d3 = program.get_workout_session_by_id('W3D3')
    w3d4 = program.get_workout_session_by_id('W3D4')
    assert w3d1 and w3d2 and w3d3 and w3d4

    d1 = (
        WorkoutSession(id='W4D1')
        .add_component(single_exercise_from_prev_session(w3d1, pogo_jump, reps=+1))
        .add_component(single_exercise_from_prev_session(w3d1, power_snatch, percentage=+0.05))
        .add_component(single_exercise_from_prev_session(w3d1, backsquat, percentage=+0.1, reps=-2))
        .add_component(
            exercise_group_from_prev_session(
                w3d1, [reverse_hyperextension, russian_twist], reps=(+2, -4), weight=(None, +10)
            )
        )
    )

    calculator = Brzycki1RMCalculator()
    d2 = (
        WorkoutSession(id='W4D2')
        .add_component(
            # single_exercise_from_prev_session(w3d2, bench_press, percentage=+0.1, reps=-2, sets=+1)
            SingleExercise(exercise=bench_press, notes='Reps is target for 100% relative intensity')
            .add_set(
                bench_press.create_set(
                    reps=int(calculator.max_reps_from_weight(1.0, 0.8)), percentage=0.8
                )
            )
            .add_set(
                bench_press.create_set(
                    reps=int(calculator.max_reps_from_weight(1.0, 0.7)), percentage=0.7
                )
            )
            # .add_set(
            #     bench_press.create_set(
            #         reps=int(calculator.max_reps_from_weight(1.0, 0.6)), percentage=0.6
            #     )
            # )
        )
        .add_component(
            SingleExercise(exercise=weighted_pullup, notes='5-10 kg').add_repeating_set(
                5, weighted_pullup.create_set(5, 5)
            )
        )
        .add_component(
            exercise_group_from_prev_session(
                w3d2, [bo_dumbbell_row, dumbbell_press], reps=(+2, 0)
            ).set_notes('')
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    d3 = (
        WorkoutSession(id='W4D3')
        .add_component(
            ExerciseGroup(
                exercises=[snatch_high_pull, low_hang_power_snatch],
            ).add_repeating_group_sets(
                5,
                {
                    snatch_high_pull: snatch_high_pull.create_set(3, percentage=0.7),
                    low_hang_power_snatch: low_hang_power_snatch.create_set(3, percentage=0.7),
                },
            )
        )
        .add_component(
            # single_exercise_from_prev_session(w3d3, backsquat, percentage=+0.05, sets=-1)
            SingleExercise(exercise=backsquat)
            .add_set(
                backsquat.create_set(
                    reps=int(calculator.max_reps_from_weight(1.0, 0.8)), percentage=0.8
                )
            )
            .add_set(
                backsquat.create_set(
                    reps=int(calculator.max_reps_from_weight(1.0, 0.7)), percentage=0.7
                )
            )
        )
        .add_component(
            SingleExercise(exercise=deadlift, notes='EMOM').add_repeating_set(
                8, deadlift.create_set(2, percentage=0.8)
            )
        )
        .add_component(
            exercise_group_from_prev_session(
                w3d3, [calf_raise, side_plank_leg_raise], reps=(-2, +2), weight=(+20, None)
            )
        )
    )

    d4 = (
        WorkoutSession(id='W4D4')
        .add_component(
            SingleExercise(exercise=eurostep_to_box).add_repeating_set(
                5, eurostep_to_box.create_set(2)
            )
        )
        .add_component(
            exercise_group_from_prev_session(
                w3d4, [power_clean, push_press, jerk], percentage=(+0.075, +0.075, +0.075)
            )
        )
        .add_component(
            SingleExercise(exercise=bench_press).add_repeating_set(
                4, bench_press.create_set(4, percentage=0.8)
            )
        )
        .add_component(
            exercise_group_from_prev_session(w3d4, [pullup, pushup, lunges]).set_notes(
                'Goal: 1 Minute faster than W3D4'
            )
        )
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W4', [s.id for s in sessions])

    return sessions
