# rip_simulation.py

class Router:
    def __init__(self, name):
        self.name = name
        self.routing_table = {name: (name, 0)}  # (next_hop, cost)
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        self.routing_table[neighbor.name] = (neighbor.name, 1)

    def update_table(self):
        updated = False
        for neighbor in self.neighbors:
            for dest, (neighbor_next_hop, neighbor_cost) in neighbor.routing_table.items():
                new_cost = neighbor_cost + 1
                
                if dest not in self.routing_table or new_cost < self.routing_table[dest][1]:
                    # Update routing table
                    self.routing_table[dest] = (neighbor.name, new_cost)
                    updated = True
        return updated

    def print_table(self):
        print(f"--- Routing Table for {self.name} ---")
        print("Dest | Next Hop | Cost")
        print("-----------------------")
        for dest, (next_hop, cost) in sorted(self.routing_table.items()):
            print(f" {dest}   |    {next_hop}     |  {cost}")
        print("\n")


# --- Simulation ---
if __name__ == "__main__":
    # 1. Create network topology
    rA = Router('A')
    rB = Router('B')
    rC = Router('C')
    rD = Router('D')

    rA.add_neighbor(rB)
    rA.add_neighbor(rC)
    
    rB.add_neighbor(rA)
    rB.add_neighbor(rC)
    rB.add_neighbor(rD)
    
    rC.add_neighbor(rA)
    rC.add_neighbor(rB)
    rC.add_neighbor(rD)
    
    rD.add_neighbor(rB)
    rD.add_neighbor(rC)

    routers = [rA, rB, rC, rD]

    # 2. Simulate periodic updates until convergence
    converged = False
    iteration = 0
    while not converged:
        iteration += 1
        print(f"--- Iteration {iteration} ---")
        updates_made = False
        for router in routers:
            if router.update_table():
                updates_made = True
        
        if not updates_made:
            converged = True
        
        if iteration > len(routers): # Simple convergence check
            converged = True
    
    print("\n--- CONVERGENCE REACHED ---\n")

    # 3. Display final routing tables
    for router in routers:
        router.print_table()