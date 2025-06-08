import streamlit as st
from pr_pro.configs import ComputeConfig
from pr_pro.exercises.common import backsquat, bench_press, deadlift
from pr_pro.program import Program

from pr3.weightlifting_3_days.exercises import (
    pendlay_row,
    frontsquat,
    strict_press,
    clean_jerk,
    snatch,
    push_press,
    power_clean,
    power_snatch,
    sg_bhtn_press,
    snatch_high_pull,
    low_hang_snatch,
    clean_pull,
)
from pr3.weightlifting_3_days.w1 import get_w1_sessions


@st.cache_data
def get_program() -> Program:
    program = (
        Program(name='Weightlifting 3 days')
        .add_best_exercise_value(backsquat, 170)
        .add_best_exercise_value(deadlift, 200)
        .add_best_exercise_value(frontsquat, 140)
        .add_best_exercise_value(bench_press, 130)
        .add_best_exercise_value(strict_press, 70)
        .add_best_exercise_value(clean_jerk, 120)
        .add_best_exercise_value(snatch, 90)
    )
    program.add_best_exercise_value(pendlay_row, program.best_exercise_values[deadlift] * 0.6)

    w1_sessions = get_w1_sessions(program)
    program.add_program_phase('W1', [ws.id for ws in w1_sessions])

    program.compute_values(
        ComputeConfig(
            exercise_associations={
                push_press: clean_jerk,
                power_clean: clean_jerk,
                power_snatch: snatch,
                sg_bhtn_press: snatch,
                snatch_high_pull: snatch,
                low_hang_snatch: snatch,
                clean_pull: deadlift,
            }
        )
    )

    return program
