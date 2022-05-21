#include "stack_dfs.h"

void stackDFS(std::vector<std::set<int>> *adj, int root, std::vector<bool> *visited) {
    std::stack<int> s;
    s.push(root);

    while (!s.empty()) {
        int u = s.top();

        (*visited)[u] = true;
        s.pop();

        for (auto v : (*adj)[u]) {
            if (!(*visited)[v])
                s.push(v);
        }
    }
}
