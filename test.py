from graph_impls.undirected_graph import UndirectedGraph
from graph_impls.directed_graph import DirectedGraph

def test_directed():
    dg = DirectedGraph()
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(2, 4)
    dg.add_edge(3, 4)
    dg.add_edge(5, 2)
    dg.add_edge(5, 4)
    print(dg)

    dg.add_edge(1, 15)
    dg.add_edge(4, 5)
    dg.add_node(20)
    print(dg)

    print(dg.incoming_neighbours(4))
    print(dg.outcoming_neighbours(2))

    dg.remove_edge(3, 4)
    print(dg)

    dg.remove_node(2)
    print(dg)


def test_undirected():
    ug = UndirectedGraph()
    ug.add_edge(1, 2)
    ug.add_edge(2, 3)
    ug.add_edge(2, 4)
    ug.add_edge(3, 4)
    ug.add_edge(5, 2)
    ug.add_edge(5, 4)
    print(ug)

    ug.add_edge(1, 15)
    ug.add_edge(4, 5)
    ug.add_node(20)
    print(ug)

    print(ug.node_neighbours(2))

    ug.remove_edge(3, 4)
    print(ug)

    ug.remove_node(2)
    print(ug)


if __name__ == '__main__':
    test_directed()
    test_undirected()


    # def dfs(adj: dict, root):
    #     # нерекурсивный ДФС
    #     # потом надо вынести отдельно и мб преобразовать, добавив всякие там время выхода, входа
    #
    #     explored, stack = {root}, [root]
    #
    #     while stack:
    #         u = stack.pop()
    #         explored.add(u)
    #         for v in reversed(adj[u]):
    #             if v not in explored:
    #                 stack.append(v)
    #     return explored
    #
    #
    # def getConnectedComponents(adj):
    #     connected_components = 0
    #     visited = {key: False for key in adj.keys()}
    #
    #     for i in adj.keys():
    #         if not visited[i]:
    #             explored = dfs(adj, i)
    #             for v in explored:
    #                 visited[v] = True
    #             connected_components += 1
    #     return connected_components

