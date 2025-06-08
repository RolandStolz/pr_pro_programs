import streamlit as st
from pr_pro.configs import ComputeConfig
from pr_pro.exercises.common import backsquat, bench_press, deadlift
from pr_pro.program import Program

from pr3.weightlifting_3_days.exercises import (
    bulgarian_split_squat,
    clean_jerk,
    clean_pull,
    frontsquat,
    low_hang_snatch,
    pendlay_row,
    power_clean,
    power_snatch,
    push_press,
    sg_bhtn_press,
    snatch,
    snatch_high_pull,
    strict_press,
)
from pr3.weightlifting_3_days.w1 import get_w1_sessions
from pr3.weightlifting_3_days.w2 import get_w2_sessions
from pr3.weightlifting_3_days.w3 import get_w3_sessions


@st.cache_data
def get_program() -> Program:
    program = (
        Program(name='Weightlifting 3 days')
        .add_best_exercise_value(backsquat, 160)
        .add_best_exercise_value(deadlift, 190)
        .add_best_exercise_value(frontsquat, 130)
        .add_best_exercise_value(bench_press, 120)
        .add_best_exercise_value(strict_press, 70)
        .add_best_exercise_value(clean_jerk, 120)
        .add_best_exercise_value(snatch, 90)
    )
    program.add_best_exercise_value(pendlay_row, program.best_exercise_values[deadlift] * 0.6)
    program.add_best_exercise_value(
        bulgarian_split_squat, program.best_exercise_values[backsquat] * 0.55
    )

    w1_sessions = get_w1_sessions(program)
    program.add_program_phase('W1', [ws.id for ws in w1_sessions])

    w2_sessions = get_w2_sessions(program)
    program.add_program_phase('W2', [ws.id for ws in w2_sessions])

    w3_sessions = get_w3_sessions(program)
    program.add_program_phase('W3', [ws.id for ws in w3_sessions])

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
