import networkx as nx

def create_graph(nodes, edges):
    """
    Создает граф на основе узлов и рёбер.
    :param nodes: Список узлов.
    :param edges: Список рёбер (источник, цель, вес).
    :return: Граф NetworkX.
    """
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(edges)
    return graph

def analyze_graph(graph):
    """
    Анализирует свойства графа.
    :param graph: Граф NetworkX.
    """
    print("Количество узлов:", graph.number_of_nodes())
    print("Количество рёбер:", graph.number_of_edges())
    print("Список узлов:", list(graph.nodes))
    print("Список рёбер:", list(graph.edges))
