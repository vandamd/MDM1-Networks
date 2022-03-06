"""
Updated Graph Generator

Made with love by Vandam :)
"""
import matplotlib.pyplot as plt
import networkx as nx
#import coordinatesToDistance as Co


########################################################################################
# INPUT CONNECTIONS TO GENERATE GRAPH FOR
#Connections = [(0.023110363476152175, 'GL'), (0.03139124081650756, 'IJ'), (0.032234120121390555, 'OP'), (0.03363439459838521, 'PV'), (0.03557900645043125, 'HK'), (0.04002178656682023, 'KQ'), (0.04194098830500167, 'JR'), (0.04708216010337468, 'FH'), (0.0477840151096576, 'RS'), (0.05136593350655939, 'AQ'), (0.053787215023649255, 'CD'), (0.05398136437697734, 'MO'), (0.06464466876703727, 'NW'), (0.06530118681922956, 'EI'), (0.07282153115665721, 'HL'), (0.07305613184394555, 'EF'), (0.07733632781558615, 'GM'), (0.07907529892450624, 'OW'), (0.09309045332363644, 'BE'), (0.09547415252307608, 'DI'), (0.0998837709540434, 'ST'), (0.11818659240793346, 'SU'), (0.14168921624456773, 'NX')]
# INPUT COORDS OF ALL POINTS - first coord is A, second is B,...
#coords = [[51.366169, -2.591542],[51.60857, -2.52529], [51.59489, -2.40161], [51.54250, -2.41379], [51.51728, -2.54351], [51.52428, -2.61623], [51.50346, -2.69272], [51.47721, -2.61516], [51.48263, -2.48816], [51.45803, -2.50766], [51.45477, -2.58755], [51.48086, -2.68789], [51.48566, -2.76798], [51.44346, -2.85710], [51.43292, -2.75647], [51.41148, -2.73240], [51.41680, -2.60020], [51.41636, -2.50290], [51.40716, -2.45601], [51.37937, -2.36007], [51.28918, -2.462995], [51.38355, -2.71366], [51.38902, -2.82224], [51.34828, -2.96206]]
########################################################################################

def GenerateGraph(Connections, coords):

    N = int(len(Connections))
    G = nx.Graph()


    ########################################################################################
    # Locations of Nodes
    locations = {chr(ord('@')+int(i)+1): (coords[i][1], coords[i][0]) for i in range(len(coords))}
    ########################################################################################
    
    
    ########################################################################################
    # Edges
    for i in range(N):
        # Adding Edges of all the Nodes to a list
        G.add_edge(str(Connections[i][1][0]), str(Connections[i][1][1]), weight=int(Connections[i][0]))

    edges = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] >= 0]

    plt.figure(figsize=(12,16))
    ########################################################################################
    
    
    ########################################################################################
    # Labels
    WeightList = [str(item[0])[:6] for item in Connections]                                         # List of weights
    FromEdgeList = [item[1][0] for item in Connections]                                             # Starting node of connection
    ToEdgeList = [item[1][1] for item in Connections]                                               # Ending node of connection
    EdgeList = list(zip(FromEdgeList[::1],ToEdgeList[::1]))                                         # Pairs the edges together e.g. [('B', 'D'), ('A', 'B'),...]
    WeightDict = {EdgeList[i]: WeightList[i] for i in range(len(EdgeList))}                         # Dictionary pairing Edgelist with Weight // Needed for labelling edges
    labels = WeightDict
    nx.draw_networkx_labels(G, locations, font_color='w', font_size=15, font_family='sans-serif')
    nx.draw_networkx_nodes(G, locations, node_color='k', node_size=700)
    nx.draw_networkx_edges(G, locations, edgelist=edges, width=6, edge_color='k', style='solid')
    nx.draw_networkx_edge_labels(G, locations, edge_labels=labels, font_size=10, verticalalignment='center', horizontalalignment='center')
    ########################################################################################
    
    
    ########################################################################################
    # Show Graph
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    ########################################################################################


#GenerateGraph(Connections, coords)