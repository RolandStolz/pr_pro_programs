from pr_pro.exercises.common import backsquat, pullup, bench_press, deadlift, power_clean, pushup
from pr_pro.program import Program
from pr_pro.workout_component import ExerciseGroup, SingleExercise
from pr_pro.workout_session import WorkoutSession

from pr3.hypertrophy.exercises import *  # noqa: F403


def add_w1_sessions(program: Program) -> list[WorkoutSession]:
    d1 = (
        WorkoutSession(id='W1D1')
        .add_component(
            SingleExercise(exercise=box_jump).add_repeating_set(5, box_jump.create_set(4))
        )
        .add_component(
            SingleExercise(exercise=power_snatch).add_repeating_set(
                6, power_snatch.create_set(3, percentage=0.6)
            )
        )
        .add_component(
            SingleExercise(exercise=backsquat).add_repeating_set(
                4, backsquat.create_set(10, percentage=0.55)
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[reverse_hyperextension, russian_twist],
            ).add_repeating_group_sets(
                4,
                {
                    reverse_hyperextension: reverse_hyperextension.create_set(6),
                    russian_twist: russian_twist.create_set(8, weight=10),
                },
            )
        )
    )

    d2 = (
        WorkoutSession(id='W1D2')
        .add_component(
            SingleExercise(exercise=bench_press).add_repeating_set(
                4, bench_press.create_set(10, percentage=0.55)
            )
        )
        .add_component(SingleExercise(exercise=pullup).add_repeating_set(5, pullup.create_set(5)))
        .add_component(
            ExerciseGroup(
                exercises=[bo_dumbbell_row, dumbbell_press], notes='22-28; 14-20'
            ).add_repeating_group_sets(
                4,
                {
                    bo_dumbbell_row: bo_dumbbell_row.create_set(10, weight=25),
                    dumbbell_press: dumbbell_press.create_set(10, weight=17),
                },
            )
        )
        .add_component(SingleExercise(exercise=arms).add_repeating_set(3, arms.create_set(10)))
    )

    d3 = (
        WorkoutSession(id='W1D3')
        .add_component(
            SingleExercise(exercise=backsquat).add_repeating_set(
                5, backsquat.create_set(6, percentage=0.65)
            )
        )
        .add_component(
            SingleExercise(exercise=muscle_snatch).add_repeating_set(
                5, muscle_snatch.create_set(3, percentage=0.5)
            )
        )
        .add_component(
            SingleExercise(exercise=deadlift).add_repeating_set(
                4, deadlift.create_set(10, percentage=0.55)
            )
        )
        .add_component(
            ExerciseGroup(exercises=[calf_raise, side_plank_leg_raise]).add_repeating_group_sets(
                4,
                {
                    calf_raise: calf_raise.create_set(12, 100),
                    side_plank_leg_raise: side_plank_leg_raise.create_set(6),
                },
            )
        )
    )

    d4 = (
        WorkoutSession(id='W1D4')
        .add_component(
            SingleExercise(exercise=eurostep_to_land, notes='each side').add_repeating_set(
                5, eurostep_to_land.create_set(2)
            )
        )
        .add_component(
            ExerciseGroup(exercises=[power_clean, push_press]).add_repeating_group_sets(
                4,
                {
                    power_clean: power_clean.create_set(3, percentage=0.5),
                    push_press: push_press.create_set(3, percentage=0.5),
                },
            )
        )
        .add_component(
            SingleExercise(exercise=bench_press).add_repeating_set(
                5, bench_press.create_set(8, percentage=0.6)
            )
        )
        .add_component(
            ExerciseGroup(
                exercises=[pullup, pushup, lunges], notes='Complete all as fast as possible!'
            ).add_group_sets(
                {
                    pullup: pullup.create_set(30),
                    pushup: pushup.create_set(60),
                    lunges: lunges.create_set(60, 20),
                },
            )
        )
    )

    sessions = [d1, d2, d3, d4]
    for s in sessions:
        program.add_workout_session(s)

    program.add_program_phase('W1', [s.id for s in sessions])

    return sessions
