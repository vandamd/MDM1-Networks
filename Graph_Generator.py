"""
Graph Generator

Made with love by Vandam :)
"""

import matplotlib.pyplot as plt
import networkx as nx

# INPUT - Matrix as a List
Matrix = [(0.09518089791960394, 'BD'), (0.1277378312985179, 'AB'), (0.1419332372816624, 'CD'), 
          (0.533477090542755, 'AD'), (0.6790313116299046, 'AC'), (0.7306722553371253, 'BC')]

N = int(len(Matrix))

WeightList = [str(item[0])[:6] for item in Matrix]
FromEdgeList = [item[1][0] for item in Matrix]
ToEdgeList = [item[1][1] for item in Matrix]
EdgeList = list(zip(FromEdgeList[::1],ToEdgeList[::1]))                     # Pairs the edges together e.g. [('B', 'D'), ('A', 'B'),...]
WeightDict = {EdgeList[i]: WeightList[i] for i in range(len(EdgeList))}     # Dictionary pairing Edgelist with Weight // Needed for labelling edges

def GenerateGraph(N):
    G = nx.Graph()
    for i in range(N):
        # Adding Edges of all the Nodes to a list
        G.add_edge(str(Matrix[i][1][0]), str(Matrix[i][1][1]), weight=int(Matrix[i][0]))
    
    # List of Edges
    edges = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] >= 0]
    
    # Position of all Nodes
    pos = nx.spring_layout(G, scale=9,seed=200)
    
    # Characteristics of the Nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    
    # Characteristics of the Edges
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=2)
    
    # Labels
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    labels = WeightDict
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    # Removes Background
    plt.axis("off")
    
    # Constrains overall size for better visibility
    plt.tight_layout()
    
    # Lets see this beauty!
    plt.show()

GenerateGraph(N)