# import numpy as np

# def page_rank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
#     n = len(graph)
#     # Create adjacency matrix
#     M = np.zeros((n, n))
#     for i, links in enumerate(graph):
#         if links:  # Avoid division by zero
#             M[:, i] = np.array([1 if j in links else 0 for j in range(n)]) / len(links)
    
#     # Initial PageRank values
#     pr = np.ones(n) / n
    
#     # Power iteration
#     for _ in range(max_iterations):
#         pr_prev = pr.copy()
#         pr = (1 - damping_factor) / n + damping_factor * M @ pr
        
#         # Check for convergence
#         if np.linalg.norm(pr - pr_prev) < tolerance:
#             break
            
#     return pr

# if __name__ == "__main__":
#     web_graph = [
#         [1, 2],  # node 0 has links to node 1 and 2
#         [0, 2],  # node 1 has links to node 0 and node 2
#         [0, 1],  # node 2 has links to node 0 and node 1
#         [1, 2],  # node 3 has links to node 1 and node 2
#     ]
    
#     result = page_rank(web_graph)
#     for i, pr in enumerate(result):
#         print(f"Page {i}: {pr:.6f}")




#!SLIP
# import numpy as np

# def simple_page_rank(graph, d=0.85, iterations=10):
#     n = len(graph)
#     # Initialize PageRank values
#     pr = np.ones(n) / n
    
#     # Run iterations
#     for _ in range(iterations):
#         new_pr = np.ones(n) * (1-d) / n
        
#         # Update based on links
#         for i, links in enumerate(graph):
#             if links:
#                 # Distribute PageRank to outgoing links
#                 for j in links:
#                     new_pr[j] += d * pr[i] / len(links)
        
#         pr = new_pr
    
#     return pr

# # Define the web graph as described
# # A=0, B=1, C=2, D=3, E=4
# web_graph = [
#     [1, 2, 3],  # Page A links to B, C, D
#     [2, 4],     # Page B links to C, E
#     [0, 3],     # Page C links to A, D
#     [],         # Page D has no outgoing links
#     []          # Page E has no outgoing links
# ]

# # Calculate PageRank
# page_names = ['A', 'B', 'C', 'D', 'E']
# ranks = simple_page_rank(web_graph)

# # Display results
# print("PageRank Results:")
# for i, (page, rank) in enumerate(sorted(zip(page_names, ranks), key=lambda x: x[1], reverse=True)):
#     print(f"Page {page}: {rank:.4f}")



#!small
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