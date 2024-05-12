# Dijkstra's algorithm


############# Array for tracking node processing ###############
processed = []

def find_lowest_cost_node(costs):
    """Функция выбора узла с наименьшей стоимостью из уже виденных, но еще не обработанных."""
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    
    return lowest_cost_node


def graph_dijkstra(graph, costs, parents):
    """Функция поиска кратчайшего пути во взвешенном графе по алгоритму Дейкстры."""
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]  # Минимальная стоимость перехода

        neighbors = graph[node]  # Выбор всех соседей узла с наименьшей стоимостью

        for j in neighbors.keys():  # Перебор все соседей
            new_cost = cost + neighbors[j]  # Стоимость переходов к соседям от узла с наименьшей стоимостью

            if costs[j] > new_cost:  # Если начальная стоимость больше рассчетной,
                costs[j] = new_cost  # то обновляем стоимость
                parents[j] = node    # и обновляем родителя

        processed.append(node)       # узел добавляем в список обработанных
        node = find_lowest_cost_node(costs)  # Берем следующий узел в обработку

    return graph, costs, parents


if __name__ == '__main__':

    ############# Creating a graph ###############
    graph = {}

    graph["start"] = {}
    graph["start"]["a"] = 5
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["c"] = 4
    graph["a"]["d"] = 2

    graph["b"] = {}
    graph["b"]["a"] = 8
    graph["b"]["d"] = 7

    graph["c"] = {}
    graph["c"]["stop"] = 3
    graph["c"]["d"] = 6

    graph["d"] = {}
    graph["d"]["stop"] = 1

    graph["stop"] = {} 


    ############# Creating a cost table ###############
    costs = {}
    costs["a"] = 5
    costs["b"] = 2
    costs["c"] = float("inf")
    costs["d"] = float("inf")
    costs["stop"] = float("inf")

    ############# Creating a Parent table ###############
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["c"] = None
    parents["d"] = None
    parents["stop"] = None

    find_lowest_cost_node(costs)  # Нахождение первого узла с наименьшей стоимостью
    graph, costs, parents = graph_dijkstra(graph, costs, parents)

    print(graph)
    print(costs)
    print(parents)

    # {'start': {'a': 5, 'b': 2}, 'a': {'c': 4, 'd': 2}, 'b': {'a': 8, 'd': 7}, 'c': {'stop': 3, 'd': 6}, 'd': {'stop': 1}, 'stop': {}}
    # {'a': 5, 'b': 2, 'c': 9, 'd': 7, 'stop': 8}
    # {'a': 'start', 'b': 'start', 'c': 'a', 'd': 'a', 'stop': 'd'}
