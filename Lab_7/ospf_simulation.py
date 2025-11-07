# ospf_simulation.py
import heapq

def calculate_dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    # (cost, current_node, path)
    priority_queue = [(0, start_node, [])]
    
    shortest_path_tree = {}
    routing_table = {}

    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)

        if current_cost > distances[current_node]:
            continue
            
        path = path + [current_node]
        shortest_path_tree[current_node] = (current_cost, path)

        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight
            if cost < distances[neighbor]:
                distances[neighbor] = cost
                heapq.heappush(priority_queue, (cost, neighbor, path))

    # Build routing table
    for node, (cost, path) in shortest_path_tree.items():
        if len(path) > 1:
            routing_table[node] = (path[1], cost)
        elif cost == 0:
            routing_table[node] = (start_node, 0)
            
    return shortest_path_tree, routing_table

def print_routing_table(router_name, table):
    print(f"--- OSPF Routing Table for {router_name} ---")
    print("Dest | Next Hop | Cost")
    print("-----------------------")
    for dest, (next_hop, cost) in sorted(table.items()):
        print(f" {dest}   |    {next_hop}     |  {cost}")
    print("\n")


# --- Simulation ---
if __name__ == "__main__":
    # 1. Create network graph with link costs
    # This represents the shared Link-State Database (LSDB)
    network_graph = {
        'A': {'B': 1, 'C': 5},
        'B': {'A': 1, 'C': 2, 'D': 1},
        'C': {'A': 5, 'B': 2, 'D': 4},
        'D': {'B': 1, 'C': 4}
    }
    
    routers = list(network_graph.keys())

    # 2. Simulate each router computing its own shortest path tree
    for router in routers:
        tree, table = calculate_dijkstra(network_graph, router)
        
        # 3. Display the routing table for each router
        print_routing_table(router, table)