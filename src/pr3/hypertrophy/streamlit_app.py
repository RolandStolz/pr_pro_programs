from pr_pro.streamlit_vis.streamlit_app import run_streamlit_app

from pr3.hypertrophy.program import get_phase1, get_phase2, compute_config


def main():
    phase1 = get_phase1()
    program = get_phase2(phase1)
    program.compute_values(compute_config)
    run_streamlit_app(program, use_persistent_state=False)


if __name__ == '__main__':
    main()
