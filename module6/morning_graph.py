from collections import deque

g = {
    "wake-up": ["exercise", "brush teeth", "pack lunch"],
    "exercise": ['shower'],
    'shower': ['get dressed'],
    'brush teeth': ["eat  breakfast"]
}


def breadth_first_search(start):
    visited = set([start])
    queue = deque([start])

    while queue:
        top = queue.popleft()
        print(top)

        if not g.get(top):
            g[top] = []

        for element in g[top]:
            if element not in visited:
                queue.append(element)
                visited.add(element)


breadth_first_search("wake-up")
