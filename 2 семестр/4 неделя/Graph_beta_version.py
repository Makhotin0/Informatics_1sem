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
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2])])
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


def DFS(graph_list, v, visited=[], ans=[]):
    ans.append(v)
    visited.append(v)
    for neigh in graph_list[v]:
        if neigh[0] not in visited:
            DFS(graph_list, neigh[0], visited)
    return ans


def has_cycle(graph_list, v, visited=[]):
    result = False
    for neigh in graph_list[v]:
        if neigh[0] in visited:
            result = True
            return result

        visited.append(v)

        if result == False:
            result = has_cycle(graph_list, neigh[0], visited)
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
    flag = has_cycle(graph_list, a)
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


def BFS(graph_list, v):
    visited = []
    queue = []
    d = {}
    for keys in graph_list.keys():
        d[keys] = float('infinity')
    visited.append(v)
    queue.append(v)
    d[v] = 0

    while queue:
        u = queue.pop(0)
        print(u, end=" ")
        for neighdour in graph_list[u]:
            if neighdour[0] not in visited:
                visited.append(neighdour[0])
                queue.append(neighdour[0])
                d[neighdour[0]] = d[u] + 1
    return d


def Dijkstra_min_length(graph_list, v):
    d = {}
    visited = []
    end = []
    for key in graph_list.keys():
        d[key] = float('infinity')
    d[v] = 0
    visited.append([0, v])

    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph_list[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])
    return d


#Максимальный среди весов используемых рёбер (?)
#Как я понял, нужно найти максимальный среди весов при оптимальном пути (при минимальной стоимости пути)
def Dijkstra_max_edge(graph_list, v):
    d = {}
    visited = []
    end = []
    for key in graph_list.keys():
        d[key] = float('infinity')
    d[v] = 0
    visited.append([0, v])

    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph_list[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = max(d[c[1]], neigh[1])
                visited.append(neigh[::-1])
    return d


#Произведение весов рёбер. Сделал так, что выводится путь с наименьшей стоимостью при произведениях
def Dijkstra_comp_edge(graph_list, v):
    d = {}
    visited = []
    end = []
    for key in graph_list.keys():
        d[key] = float('infinity')
    d[v] = 1
    visited.append([0, v])

    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph_list[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] * neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] * neigh[1])
                visited.append(neigh[::-1])
    return d


#Конкатенация строк, написанных на рёбрах. Для оптимального пути
def Dijkstra_concatenation(graph_list, v):
    string_ans = {}
    d = {}
    visited = []
    end = []
    for key in graph_list.keys():
        d[key] = float('infinity')
        string_ans[key] = ''
    d[v] = 0
    visited.append([0, v])

    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph_list[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                    string_ans[neigh[0]] = string_ans[c[1]] + str(neigh[1])
                visited.append(neigh[::-1])
    return string_ans


#Максимальная стоимость пути
def Dijkstra_max_length(graph_list, v):
    d = {}
    visited = []
    end = []
    for key in graph_list.keys():
        d[key] = 0
    d[v] = 0
    visited.append([0, v])

    while visited:
        visited.sort()
        c = visited.pop(-1)
        end.append(c[1])
        for neigh in graph_list[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) > d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])
    return d


#Минимальный среди весов используемых рёбер при максимальной стоимости пути
def Dijkstra_min_edge(graph_list, v):
    d = {}
    visited = []
    end = []
    for key in graph_list.keys():
        d[key] = 0
    d[v] = float('infinity')
    visited.append([0, v])

    while visited:
        visited.sort()
        c = visited.pop(-1)
        end.append(c[1])
        for neigh in graph_list[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) > d[neigh[0]]:
                    d[neigh[0]] = min(d[c[1]], neigh[1])
                visited.append(neigh[::-1])
    d[v] = 0
    return d


edge_list = read_graph_as_edges()
graph_list = read_graph_as_neigh_list(edge_list)
graph_matrix = read_graph_as_neigh_matrix(edge_list)
print(DFS(graph_list, 1))
#print(has_cycle(graph_list, 1))
print(graph_list)
#print_matrix(graph_matrix)
print(road_a_b(graph_list, graph_matrix, 1, 8))
print(father_a_b(graph_list, 1, 5))
print(BFS(graph_list, 1))
print(Dijkstra_min_length(graph_list, 1))
print(Dijkstra_max_edge(graph_list, 1))
print(Dijkstra_comp_edge(graph_list, 1))
print(Dijkstra_concatenation(graph_list, 1))
print(Dijkstra_max_length(graph_list, 1))
print(Dijkstra_min_edge(graph_list, 1))


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
10
1 2 1
1 3 2
2 5 3
3 5 4
3 4 5
4 6 6
5 6 5
5 7 4
6 8 3
7 8 2
'''


# Для количества путей (ориентированный ациклический граф) (пример 2)
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

#1 2 3 5 4 6 7 8 {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4}
