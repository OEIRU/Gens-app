import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph):
    """
    Строит граф.
    :param graph: Граф NetworkX.
    """
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

def plot_results(results):
    """
    Строит графики решения системы.
    :param results: Решение системы.
    """
    for i, y in enumerate(results.y):
        plt.plot(results.t, y, label=f"y{i+1}")
    plt.xlabel("Время")
    plt.ylabel("Концентрация")
    plt.legend()
    plt.show()
