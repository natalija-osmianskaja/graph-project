import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(num_vertices, probability):
    G = nx.erdos_renyi_graph(n=num_vertices, p=probability)
    return G

num_vertices = 5  # Specify the number of vertices
probability = 0.8  # Probability of edge creation

random_graph = generate_random_graph(num_vertices, probability)

# Draw the graph
nx.draw(random_graph, with_labels=True)
plt.show()