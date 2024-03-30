def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list(edge_list):
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1])])
    return graph_dict


def read_graph_as_neigh_matrix(edge_list):
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = 1

    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


def DFS(graph, v, visited=[], ans=[]):
    ans.append(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS(graph, neigh, visited)
    return ans


def has_cycle(graph, v, visited=[]):
    result = False
    for neigh in graph[v]:
        if neigh in visited:
            result = True
            return result

        visited.append(v)

        if result == False:
            result = has_cycle(graph, neigh, visited)
            visited = []
    return result


# Поиск нахождения количества путей решил с помощью матрицы смежности.
# Основной алгоритм на пальцах --> https://youtu.be/KqUlbUdgcko?si=xxjnnz08Nf3JJkZG
def support_function_road_a_b(graph_matrix, a, b):
    work_matrix = [[0 for i in range(len(graph_matrix))] for j in range(len(graph_matrix))]
    zero_matrix = [[0 for i in range(len(graph_matrix))] for j in range(len(graph_matrix))]

    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix)):
            work_matrix[i][j] = graph_matrix[i][j]

    ans = 0
    ans += graph_matrix[a-1][b-1]

    while work_matrix != zero_matrix:
        calculate_matrix = [[0 for i in range(len(graph_matrix))] for j in range(len(graph_matrix))]

        for i in range(len(graph_matrix)):
            for j in range(len(work_matrix)):
                for k in range(len(graph_matrix)):
                    calculate_matrix[i][j] += work_matrix[i][k] * graph_matrix[k][j]

        for i in range(len(graph_matrix)):
            for j in range(len(work_matrix)):
                work_matrix[i][j] = calculate_matrix[i][j]

        ans += work_matrix[a-1][b-1]
    return ans


def road_a_b(graph_list, graph_matrix, a, b):
    flag = has_cycle(graph_list, 1)
    if flag == False:
        ans = support_function_road_a_b(graph_matrix, a, b)
    else:
        ans = 'В графе присутсвует цикл'
    return ans


def father_a_b(graph_list, a, b):
    flag = False
    ans_list = DFS(graph_list, a)
    if b in ans_list:
        flag = True
    return flag

'''def bfs(graph, v):
    queue = []
    d = {}
    for keys in graph.keys():
        d[keys] = 100000
    visited = []
    visited.append(v)
    queue.append(v)
    d[v] = 0

    while queue:
        u = queue.pop(0)
        print(u, end = ' ')

        for neighdour in graph[u]:
            if neighdour not in visited:
                visited.append(neighdour)
                queue.append(neighdour)
                d[neighdour] = d[u] + 1
    return d'''


edge_list = read_graph_as_edges()
graph_list = read_graph_as_neigh_list(edge_list)
graph_matrix = read_graph_as_neigh_matrix(edge_list)
#print(DFS(graph_list, 1))
#print(has_cycle(graph_list, 1))
#print(graph_list)
#print_matrix(graph_matrix)
#print(road_a_b(graph_list, graph_matrix, 1, 8))
print(father_a_b(graph_list, 1, 5))


# Граф с циклами
'''
8
1 4 6
1 2 1
3 2 2
2 5 3
2 6 1
5 3 1
6 2 2
6 4 1
'''

# Для количества путей (ориентированный ациклический граф) (пример 1)
'''
7
1 4 6
1 2 1
2 3 2
2 5 3
2 6 1
3 5 1
6 4 1
'''

# Для количества путей (ориентированный ациклический граф) (пример 2)
'''
10
1 2 1
1 3 1
2 5 1
3 5 1
3 4 1
4 6 1
5 6 1
5 7 1
6 8 1
7 8 1
'''