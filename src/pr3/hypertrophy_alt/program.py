from pathlib import Path
from pr3.hypertrophy.w5 import add_w5_sessions
from pr3.visualization import (
    extract_progression_from_program,
    plot_reps_weight_exercise_progression,
)
from pr_pro.configs import ComputeConfig
from pr_pro.exercises.common import backsquat, bench_press, deadlift
from pr_pro.functions import Epley1RMCalculator
from pr_pro.program import Program

from pr3.hypertrophy_alt.w1 import add_w1_sessions
from pr3.hypertrophy_alt.w2 import add_w2_sessions
from pr3.hypertrophy_alt.w3 import add_w3_sessions
from pr3.hypertrophy_alt.w4 import add_w4_sessions
from pr3.hypertrophy_alt.exercises import *  # noqa: F403


def get_phase1() -> Program:
    program = (
        Program(name='WL Hypertrophy Phase 1 - Amelie')
        .add_best_exercise_value(backsquat, 70)
        .add_best_exercise_value(deadlift, 110)
        .add_best_exercise_value(bench_press, 52.5)
        .add_best_exercise_value(barbell_row, 110 * 0.6)
    )

    add_w1_sessions(program)
    add_w2_sessions(program)
    add_w3_sessions(program)
    add_w4_sessions(program)

    return program


def get_phase2(phase1: Program) -> Program:
    program = (
        Program(name='WL Hypertrophy Phase 2 - Amelie')
        .add_best_exercise_value(backsquat, 70)
        .add_best_exercise_value(deadlift, 110)
        .add_best_exercise_value(bench_press, 52.5)
        .add_best_exercise_value(barbell_row, 110 * 0.6)
    )

    add_w5_sessions(program, phase1)

    return program


if __name__ == '__main__':
    compute_config = ComputeConfig(one_rm_calculator=Epley1RMCalculator())

    phase1 = get_phase1()
    # phase2 = get_phase2(phase1)

    phase1.compute_values(compute_config)
    phase1.export_to_pdf(Path('amelie_phase1.pdf'))

    # phase2.compute_values(compute_config)
    # phase2.export_to_pdf(Path('amelie_phase2.pdf'))

    sets = extract_progression_from_program(phase1, bench_press)
    for s in sets:
        print(s)
    plot_reps_weight_exercise_progression(phase1, bench_press, sets, show=True)  # pyright: ignore[reportArgumentType]
