#include "connectedComponents.h"

int getConnectedComponents(Graph g)
{
    // todo добавить так, чтобы ещё найти самую большую компоненту и куда-то её сохранить
    std::vector<std::vector<int>> *adj = &g.adj;
    int n = adj->size();
    int connected_components = 0;
    std::vector<bool> visited(n, false);
    bool nonRecursive = true; // todo

    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            if (nonRecursive)
                stackDFS(adj, i, &visited);
            else
                DFS(adj, i, &visited);
            connected_components++;
        }
    }
    return connected_components;
}