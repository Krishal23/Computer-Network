# bgp_simulation.py

class AS:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        # Routing table: {prefix: as_path}
        self.routing_table = {}
        # We simulate one prefix, 'Network_X'
        self.best_path = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def announce_self(self):
        self.best_path = [self.name]
        self.routing_table['Network_X'] = [self.name]

    def receive_announcement(self, neighbor, announced_path):
        # 3. Loop Prevention
        if self.name in announced_path:
            return False # Loop detected, discard
            
        new_path = [self.name] + announced_path
        
        # 2. Path Selection
        if not self.best_path or len(new_path) < len(self.best_path):
            self.best_path = new_path
            self.routing_table['Network_X'] = new_path
            return True # Path was updated
        return False

    def print_table(self):
        print(f"--- BGP Table for {self.name} ---")
        if not self.best_path:
            print("No path to Network_X")
        else:
            print(f"Dest: Network_X | Path: {' -> '.join(self.best_path)}")
        print("\n")

# --- Simulation ---
if __name__ == "__main__":
    # 1. Define AS-level topology
    as1 = AS('AS1')
    as2 = AS('AS2')
    as3 = AS('AS3')
    as4 = AS('AS4') # The "origin" AS for Network_X

    as1.add_neighbor(as2)
    as1.add_neighbor(as3)
    
    as2.add_neighbor(as1)
    as2.add_neighbor(as3)
    
    as3.add_neighbor(as1)
    as3.add_neighbor(as2)
    as3.add_neighbor(as4)
    
    as4.add_neighbor(as3)

    ases = [as1, as2, as3, as4]
    
    # AS4 originates the prefix
    as4.announce_self()

    # 2. Simulate BGP UPDATE exchanges
    converged = False
    while not converged:
        updated = False
        for as_node in ases:
            if not as_node.best_path:
                continue
            
            for neighbor in as_node.neighbors:
                if neighbor.receive_announcement(as_node, as_node.best_path):
                    updated = True
        
        if not updated:
            converged = True

    print("--- BGP CONVERGENCE REACHED ---\n")
    
    # 4. Show final routing tables
    for as_node in ases:
        as_node.print_table()