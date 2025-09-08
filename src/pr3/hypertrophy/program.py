from pathlib import Path
from pr_pro.configs import ComputeConfig
from pr_pro.exercises.common import backsquat, bench_press, deadlift, power_clean
from pr_pro.program import Program

from pr3.hypertrophy.w1 import add_w1_sessions
from pr3.hypertrophy.w2 import add_w2_sessions
from pr3.hypertrophy.w3 import add_w3_sessions
from pr3.hypertrophy.w4 import add_w4_sessions
from pr3.hypertrophy.exercises import *  # noqa: F403


def get_program() -> Program:
    # program = (
    #     Program(name='WL Hypertrophy Lenz')
    #     .add_best_exercise_value(backsquat, 110)
    #     .add_best_exercise_value(deadlift, 140)
    #     .add_best_exercise_value(bench_press, 100)
    #     .add_best_exercise_value(clean_jerk, 80)
    #     .add_best_exercise_value(snatch, 60)
    # )

    program = (
        Program(name='WL Hypertrophy Roland')
        .add_best_exercise_value(backsquat, 130)
        .add_best_exercise_value(deadlift, 180)
        .add_best_exercise_value(bench_press, 110)
        .add_best_exercise_value(clean_jerk, 110)
        .add_best_exercise_value(snatch, 85)
    )

    add_w1_sessions(program)
    add_w2_sessions(program)
    add_w3_sessions(program)
    add_w4_sessions(program)

    return program


if __name__ == '__main__':
    program = get_program()
    program.compute_values(
        ComputeConfig(
            exercise_associations={
                power_clean: clean_jerk,
                push_press: clean_jerk,
                power_snatch: snatch,
                muscle_snatch: snatch,
                low_hang_power_snatch: snatch,
                snatch_high_pull: snatch,
            }
        )
    )
    # print(program)
    program.export_to_pdf(Path('roland.pdf'))
