import json
from graph_utils import create_graph, analyze_graph
from modeling import solve_differential_equations
from visualization import plot_graph, plot_results

def main():
    # Загрузка параметров
    with open("data/example_params.json", "r") as file:
        params = json.load(file)

    # Создание графа
    graph = create_graph(params["nodes"], params["edges"])

    # Анализ графа
    analyze_graph(graph)

    # Решение дифференциальных уравнений
    results = solve_differential_equations(graph, params["initial_conditions"], params["time_range"])

    # Визуализация
    plot_graph(graph)
    plot_results(results)

if __name__ == "__main__":
    main()
