from collections import deque

graph = {
    "you": ["alice", "bob", "claie"],
    "bob": ["anuj", "peggy"],
    "alice": ['peggy'],
    "clair": ["thom", 'jonny'],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def breadth_first_search(start):
    search_queue = deque([start])
    searched = set([start])

    while search_queue:
        current = search_queue.popleft()
        print(current)
        if not graph.get(current):
            graph[current] = []

        for neighbour in graph[current]:
            if not neighbour in searched:
                search_queue.append(neighbour)
                searched.add(neighbour)


breadth_first_search('you')
