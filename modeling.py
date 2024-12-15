import numpy as np
import networkx as nx  # Добавлен импорт NetworkX
from scipy.integrate import solve_ivp

def hill_function(x, k, n):
    """
    Функция Хилла.
    :param x: Концентрация вещества.
    :param k: Константа.
    :param n: Степень.
    :return: Результат функции Хилла.
    """
    return x**n / (k**n + x**n)

def system_of_equations(t, y, params):
    """
    Система дифференциальных уравнений для генной сети.
    :param t: Время.
    :param y: Вектор состояний.
    :param params: Параметры модели.
    :return: Производные.
    """
    dydt = []
    for i, _ in enumerate(y):
        # Для каждого узла i, находим активацию и ингибирование
        activation = sum(hill_function(y[j], params["k"][str(j)], params["n"][str(j)]) for j in params["activators"].get(str(i), []))
        inhibition = sum(hill_function(y[j], params["k"][str(j)], params["n"][str(j)]) for j in params["inhibitors"].get(str(i), []))
        decay = params["decay"].get(str(i), 0.1) * y[i]  # Если decay не указан, используем значение по умолчанию (0.1)
        dydt.append(activation - inhibition - decay)
    return dydt

def solve_differential_equations(graph, initial_conditions, time_range):
    """
    Решает систему ДУ для заданного графа.
    :param graph: Граф NetworkX.
    :param initial_conditions: Начальные условия.
    :param time_range: Диапазон времени.
    :return: Решение системы.
    """
    params = {
        "k": nx.get_node_attributes(graph, "k"),
        "n": nx.get_node_attributes(graph, "n"),
        "activators": nx.get_node_attributes(graph, "activators"),
        "inhibitors": nx.get_node_attributes(graph, "inhibitors"),
        "decay": nx.get_node_attributes(graph, "decay"),
    }

    sol = solve_ivp(system_of_equations, time_range, initial_conditions, args=(params,))
    return sol
