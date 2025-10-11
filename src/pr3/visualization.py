from matplotlib.axes import Axes
from pr_pro.exercise import Exercise_t, RepsAndWeightsExercise
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pr_pro.pdf_export.pdf_generator import SingleExercise
from pr_pro.program import Program
from pr_pro.sets import RepsAndWeightsSet, WorkingSet_t


def extract_progression_from_program(
    program: Program, exercise: Exercise_t
) -> list[tuple[int, WorkingSet_t]]:
    exercise_sets = []

    for _, session in program.workout_session_dict.items():
        for comp in session.workout_components:
            if isinstance(comp, SingleExercise):
                if comp.exercise == exercise and len(comp.sets) > 0:
                    exercise_sets.append((len(comp.sets), comp.sets[0]))

    print(f'Found {len(exercise_sets)} sets for exercise {exercise.name}')
    return exercise_sets


def plot_reps_weight_exercise_progression(
    program: Program,
    exercise: RepsAndWeightsExercise,
    exercise_sets: list[tuple[int, RepsAndWeightsSet]] | None = None,
    ax: Axes | None = None,
    show: bool = False,
) -> Figure:
    if exercise_sets is None:
        exercise_sets = extract_progression_from_program(program, exercise)  # pyright: ignore[reportAssignmentType]

    assert exercise_sets is not None
    assert len(exercise_sets) > 0, f'No sets found for exercise {exercise.name}'

    # Extract data from sets
    steps = list(range(1, len(exercise_sets) + 1))
    reps_list = []
    n_sets_list = []
    percentage_list = []
    relative_percentage_list = []

    for n_sets, s in exercise_sets:
        reps_list.append(s.reps)
        n_sets_list.append(n_sets)
        percentage_list.append(s.percentage)
        relative_percentage_list.append(s.relative_percentage)

    # Create plot
    if ax is None:
        fig, ax = plt.subplots()  # pyright: ignore[reportAssignmentType]
    else:
        fig = plt.gcf()

    # Create twin y # Primary axis for percentages (both lines)
    line1 = ax.plot(steps, percentage_list, 'b-', linewidth=2, label='Intensity (%)', marker='o')
    line2 = ax.plot(
        steps,
        relative_percentage_list,
        'g-',
        linewidth=2,
        label='Relative Intensity (%)',
        marker='o',
    )

    # Secondary axis for reps
    ax2 = ax.twinx()
    line3 = ax2.plot(steps, reps_list, 'r--', linewidth=1, label='Reps', marker='x', alpha=0.8)
    line4 = ax2.plot(steps, n_sets_list, 'm--', linewidth=1, label='# Sets', marker='x', alpha=0.8)

    # Formatting for primary axis (percentages)
    ax.set_xlabel('Progression Step', fontsize=12)
    ax.set_ylabel('Percentage Intensity', fontsize=12, color='black')
    # ax.set_ylim(0.5, 1.0)  # Scale for percentages
    ax.tick_params(axis='y', labelcolor='black')

    # Formatting for secondary axis (reps)
    ax2.set_ylabel('Reps / # Sets', fontsize=12)
    ax2.yaxis.get_major_locator().set_params(integer=True)  # pyright: ignore[reportCallIssue]

    # Title and combined legend
    ax.set_title(f'{exercise.name} Progression', fontsize=14, fontweight='bold')

    # Combined legend
    lines = line1 + line2 + [line3[0]] + [line4[0]]
    labels = ['Intensity (%)', 'Relative Intensity (%)', 'Reps', 'Sets']
    ax.legend(lines, labels, loc='upper left')

    # Grid and layout
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    if show:
        plt.show()
    return fig
