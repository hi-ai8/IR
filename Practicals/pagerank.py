import networkx as nx

# Create the directed graph
G = nx.DiGraph()

# Add edges according to the given web graph structure
G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'),
                  ('B', 'C'), ('B', 'E'),
                  ('C', 'A'), ('C', 'D')])

# Apply the PageRank algorithm
pagerank = nx.pagerank(G, alpha=0.85)

print("PageRank values:")
for page, rank in pagerank.items():
    print(f"{page}: {rank:.4f}")
