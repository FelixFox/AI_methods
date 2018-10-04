import networkx as nx
from graph import Graph
import random
import matplotlib.pyplot as plt


def visualize_graph(graph: Graph):
    G = nx.Graph()
    edge_list = graph.edges()
    G.add_edges_from(edge_list)
    node_list = graph.vertices()
    n_nodes = len(node_list)
    pos = {node: (random.randint(0, 50), random.randint(0, 100))
           for i, node in enumerate(node_list)}
    print(pos)
    plt.figure(num=None, figsize=(80, 60), dpi=80, facecolor='w', edgecolor='k')
    nx.draw_networkx_nodes(G, pos, edge_labels=True, node_size=2000)
    nx.draw_networkx_edges(G, pos, alpha=0.5, width=6)
    labels = nx.draw_networkx_labels(G, pos)
    plt.show()


if __name__ == "__main__":
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    graph = Graph(g)
    visualize_graph(graph)
