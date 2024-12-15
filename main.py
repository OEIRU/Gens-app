import json
from graph_utils import create_graph, analyze_graph
from modeling import solve_differential_equations
from visualization import plot_graph, plot_results

def add_parameters_to_graph(graph, params):
    for node in graph.nodes:
        graph.nodes[node]["k"] = params["k"].get(str(node), 1.0)
        graph.nodes[node]["n"] = params["n"].get(str(node), 1.0)
        graph.nodes[node]["activators"] = params["activators"].get(str(node), [])
        graph.nodes[node]["inhibitors"] = params["inhibitors"].get(str(node), [])
        graph.nodes[node]["decay"] = params["decay"].get(str(node), 0.1)

def main():
    # Загрузка параметров
    with open("data/example_params.json", "r") as file:
        params = json.load(file)

    # Создание графа
    graph = create_graph(params["nodes"], params["edges"])

    # Добавление параметров в граф
    add_parameters_to_graph(graph, params)

    # Анализ графа
    analyze_graph(graph)

    # Решение дифференциальных уравнений
    results = solve_differential_equations(graph, params["initial_conditions"], params["time_range"])

    # Визуализация
    plot_graph(graph)
    plot_results(results)
if __name__ == "__main__":
    main()
