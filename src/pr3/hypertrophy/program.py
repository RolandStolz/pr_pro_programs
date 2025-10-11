from pathlib import Path
from pr3.hypertrophy.w5 import add_w5_sessions
from pr3.hypertrophy.w6 import add_w6_sessions
from pr3.hypertrophy.w7 import add_w7_sessions
from pr3.hypertrophy.w8 import add_w8_sessions
from pr3.visualization import (
    extract_progression_from_program,
    plot_reps_weight_exercise_progression,
)
from pr_pro.configs import ComputeConfig
from pr_pro.exercises.common import backsquat, bench_press, deadlift, power_clean
from pr_pro.functions import Epley1RMCalculator
from pr_pro.program import Program

from pr3.hypertrophy.w1 import add_w1_sessions
from pr3.hypertrophy.w2 import add_w2_sessions
from pr3.hypertrophy.w3 import add_w3_sessions
from pr3.hypertrophy.w4 import add_w4_sessions
from pr3.hypertrophy.exercises import *  # noqa: F403


def get_phase1() -> Program:
    # program = (
    #     Program(name='WL Hypertrophy Lenz')
    #     .add_best_exercise_value(backsquat, 110)
    #     .add_best_exercise_value(deadlift, 140)
    #     .add_best_exercise_value(bench_press, 110)
    #     .add_best_exercise_value(clean_jerk, 80)
    #     .add_best_exercise_value(snatch, 60)
    # )

    program = (
        Program(name='WL Hypertrophy Phase 1 - Roland')
        .add_best_exercise_value(backsquat, 130)
        .add_best_exercise_value(deadlift, 180)
        .add_best_exercise_value(bench_press, 110)
        .add_best_exercise_value(clean_jerk, 110)
        .add_best_exercise_value(snatch, 85)
        .add_best_exercise_value(barbell_row, 180 * 0.6)
    )

    add_w1_sessions(program)
    add_w2_sessions(program)
    add_w3_sessions(program)
    add_w4_sessions(program)

    return program


def get_phase2(phase1: Program) -> Program:
    program = (
        Program(name='WL Hypertrophy Phase 2 - Roland')
        # .add_best_exercise_value(backsquat, 136.5)
        .add_best_exercise_value(backsquat, 140)
        .add_best_exercise_value(deadlift, 180)
        # .add_best_exercise_value(bench_press, 117.333)
        .add_best_exercise_value(bench_press, 120)
        .add_best_exercise_value(clean_jerk, 110)
        .add_best_exercise_value(snatch, 85)
        .add_best_exercise_value(barbell_row, 180 * 0.6)
    )

    add_w5_sessions(program, phase1)
    add_w6_sessions(program)
    add_w7_sessions(program)
    add_w8_sessions(program)

    return program


compute_config = ComputeConfig(
    one_rm_calculator=Epley1RMCalculator(),
    exercise_associations={
        power_clean: clean_jerk,
        push_press: clean_jerk,
        jerk: clean_jerk,
        power_snatch: snatch,
        muscle_snatch: snatch,
        low_hang_power_snatch: snatch,
        snatch_high_pull: snatch,
    },
)


if __name__ == '__main__':
    # calculator = Epley1RMCalculator()
    # print(calculator.one_rep_max(88, 10))
    # print(calculator.one_rep_max(105, 9))
    # quit()

    phase1 = get_phase1()
    phase2 = get_phase2(phase1)

    phase1.compute_values(compute_config)
    phase1.export_to_pdf(Path('roland_phase1.pdf'))

    phase2.compute_values(compute_config)
    phase2.export_to_pdf(Path('roland_phase2.pdf'))
    # program.export_to_pdf(Path('lenz.pdf'))

    # Plotting
    # exercise = backsquat
    # exercise = bench_press
    exercise = deadlift
    sets = extract_progression_from_program(phase1, exercise)
    sets2 = extract_progression_from_program(phase2, exercise)
    print(sets2)
    sets.extend(sets2)

    for s in sets:
        print(s)

    plot_reps_weight_exercise_progression(phase1, exercise, sets, show=True)  # pyright: ignore[reportArgumentType]
