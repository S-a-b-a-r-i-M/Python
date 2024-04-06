class Graph:
    def __init__(self, edges):
        self.graph = {}
        for start, end in edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]

        print(self.graph)

    def get_paths(self, start, end, paths=None):
        if paths is None:
            paths = []
        paths += [start]

        if start == end:
            return [paths]

        if start not in self.graph:
            return []

        path = []
        for vertex in self.graph[start]:
            if vertex not in paths:
                path += self.get_paths(vertex, end, paths)
                paths.pop()

        return path


def build_graph():
    paths = [('Mumbai', 'Paris'), ('Mumbai', 'Dubai'), ('Paris', 'Dubai'),
             ('Dubai', 'New York'), ('Paris', 'New York'), ('New York', 'Toronto')]
    return Graph(paths)


if __name__ == '__main__':
    graph = build_graph()

    print(graph.get_paths('Dubai', 'Dubai'))
    print(graph.get_paths('Toronto', 'Mumbai'))
    print(graph.get_paths('Mumbai', 'New York'))
