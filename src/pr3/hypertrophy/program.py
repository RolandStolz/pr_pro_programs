from pr_pro.configs import ComputeConfig
from pr_pro.exercises.common import backsquat, bench_press, deadlift, power_clean
from pr_pro.program import Program

from pr3.hypertrophy.w1 import get_w1_sessions
from pr3.hypertrophy.exercises import snatch, clean_jerk, power_snatch, muscle_snatch, push_press


def get_program() -> Program:
    program = (
        Program(name='WL Hypertrophy')
        .add_best_exercise_value(backsquat, 150)
        .add_best_exercise_value(deadlift, 180)
        .add_best_exercise_value(bench_press, 110)
        .add_best_exercise_value(clean_jerk, 110)
        .add_best_exercise_value(snatch, 80)
    )

    w1_sessions = get_w1_sessions(program)

    program.add_program_phase('W1', [ws.id for ws in w1_sessions])

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
            }
        )
    )
    print(program)
