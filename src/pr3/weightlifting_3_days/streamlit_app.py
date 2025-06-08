from pr_pro.streamlit_vis.streamlit_app import run_streamlit_app

from pr3.weightlifting_3_days.program import get_program


def main():
    program = get_program()
    run_streamlit_app(program, use_persistent_state=True)


if __name__ == '__main__':
    main()
