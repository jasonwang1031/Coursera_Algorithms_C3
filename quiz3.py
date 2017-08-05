def mst(edges,total_nodes):
    visited = []
    vertex = edges[0]
    TotalCost = 0
    while len(visited) < total_nodes:
        if vertex not in visited:
            visited.append(vertex)
        for edge in edges:
            if edge[0] in visited and edge[1] not in visited
                TotalCost += edge[2]
                vertex = edge[1]
    
            elif edge[1] in visited and edge[0] not in visited:
                overall_cost += e[2]
                vertex = edge[0]


        
print (overall_cost)

if __name__ == "__main__":
    graph = open("quiz3.txt", 'r')
    edges = []
    summay = graph.readlines()[0]
    g = graph.readline()[1:]
    total_nodes, total_edges = int (summary.split())
    for EachEdge in g:
        node1, node2, cost = int(EachEdge.split())
            edges.append([node1, node2, cost])
    edges = sorted(edges, key=lambda x: x[2])
    mst(edges,total_nodes)
