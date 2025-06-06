import streamlit as st
from pr_pro_programs.abah.w1 import get_w1_sessions
from pr_pro_programs.abah.w2 import get_w2_sessions
from pr_pro_programs.abah.w3 import get_w3_sessions
from pr_pro_programs.abah.w4 import get_w4_sessions
from pr_pro_programs.abah.w5 import get_w5_sessions
from pr_pro_programs.abah.w6 import get_w6_sessions
from pr_pro_programs.abah.w7 import get_w7_sessions
from pr_pro_programs.abah.w8 import get_w8_sessions
from pr_pro.configs import ComputeConfig
from pr_pro.exercises.common import backsquat, bench_press, deadlift
from pr_pro.program import Program
from pr_pro_programs.abah.exercises import pendlay_row


@st.cache_data
def get_program() -> Program:
    program = (
        Program(name='Amelie becoming a horse 🐴')
        .add_best_exercise_value(backsquat, 55)
        .add_best_exercise_value(deadlift, 100)
        .add_best_exercise_value(bench_press, 50)
    )
    program.add_best_exercise_value(pendlay_row, program.best_exercise_values[deadlift] * 0.6)

    w1_sessions = get_w1_sessions(program)
    program.add_program_phase('W1', [ws.id for ws in w1_sessions])

    w2_sessions = get_w2_sessions(program)
    program.add_program_phase('W2', [ws.id for ws in w2_sessions])

    w3_sessions = get_w3_sessions(program)
    program.add_program_phase('W3', [ws.id for ws in w3_sessions])

    w4_sessions = get_w4_sessions(program)
    program.add_program_phase('W4', [ws.id for ws in w4_sessions])

    w5_sessions = get_w5_sessions(program)
    program.add_program_phase('W5', [ws.id for ws in w5_sessions])

    w6_sessions = get_w6_sessions(program)
    program.add_program_phase('W6', [ws.id for ws in w6_sessions])

    w7_sessions = get_w7_sessions(program)
    program.add_program_phase('W7', [ws.id for ws in w7_sessions])

    w8_sessions = get_w8_sessions(program)
    program.add_program_phase('W8', [ws.id for ws in w8_sessions])

    program.compute_values(ComputeConfig())

    return program
