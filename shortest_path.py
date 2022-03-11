from queue import PriorityQueue
GRAPH = {
            'Rabat': {'Sueca': 1063, 'Hamburg': 30},
            'Sueca': {'Rudow': 2656, 'Rabat': 1063},
            'Rudow': {'Mosu': 1352, 'Sueca': 2656},
            'Mosu': {'Le Plessis Trevise': 1841, 'Rudow':1352},
            'Le Plessis Trevise': {'Kang Dong': 61, 'Mosu': 1841},
            'Kang Dong': {'Nezahualcoyotl': 1634, 'Le Plessis Trevise': 61},
            'Nezahualcoyotl': {'Lindenwold': 151, 'Kang Dong': 1634},
            'Lindenwold': {'Queanbeyan': 285, 'Nezahualcoyotl':151},
            'Queanbeyan': {'Saint Chamond': 146, 'Lindenwold': 285},
            'Saint Chamond': {'Cheektowaga': 11, 'Queanbeyan': 146},
            'Cheektowaga': {'Tirupati': 380, 'Saint Chamond': 11},
            'Tirupati': {'Snezhinsk': 2547, 'Cheektowaga': 380},
            'Snezhinsk': {'Glazov': 2524, 'Tirupati':2547},
            'Glazov': {'Gaoyou': 97, 'Snezhinsk':2524},
            'Gaoyou': {'Nola': 6999, 'Glazov':97},
            'Nola': {'Rutigliano': 63, 'Gaoyou':6999},
            'Rutigliano': {'Colombo': 105, 'Nola':63},
            'Colombo': {'Meckenheim': 244, 'Rutigliano': 105},
            'Meckenheim': {'Hamburg': 502, 'Colombo': 244},
            'Hamburg': {'Rabat': 30, 'Meckenheim': 502}
        }

def dfs_paths(source, destination, path=None):
    if path is None:
        path = [source]
    if source == destination:
        yield path
    for next_node in set(GRAPH[source].keys()) - set(path):
        yield from dfs_paths(next_node, destination, path + [next_node])

def uniform_cost(source, destination):
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            if not next_node in visited or visited[next_node] >= current_cost:
                visited[next_node] = current_cost
                priority_queue.put((current_cost, next_node, path + [next_node]))
def main():
    print('ENTER SOURCE :', end=' ')
    source = input().strip()
    print('ENTER GOAL :', end=' ')
    destination = input().strip()
    if source not in GRAPH or destination not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        print('\nALL POSSIBLE PATHS:')
        paths = dfs_paths(source, destination)
        for path in paths:
            print(' -> '.join(city for city in path))
        print('\nCHEAPEST PATH:')
        cost, cheapest_path = uniform_cost(source, destination)
        print('PATH COST =', cost)
        print(' -> '.join(city for city in cheapest_path))


if __name__ == '__main__':
    main()