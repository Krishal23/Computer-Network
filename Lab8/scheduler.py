from dataclasses import dataclass

@dataclass
class Packet:
    source_ip: str
    dest_ip: str
    payload: str
    priority: int  # 0=High, 1=Medium, 2=Low

def fifo_scheduler(packet_list: list) -> list:
    #Simulates a First-Come, First-Served scheduler.
    #The input list is already in arrival order.
    return packet_list.copy()

def priority_scheduler(packet_list: list) -> list:
    #Simulates a Priority Scheduler.
    #Sorts by priority number (lower is higher priority).
    return sorted(packet_list, key=lambda p: p.priority)

# Main test case
if __name__ == "__main__":
    # Create packets in arrival order
    packets = [
        Packet("10.0.0.1", "10.0.0.2", "Data Packet 1", 2),
        Packet("10.0.0.3", "10.0.0.4", "Data Packet 2", 2),
        Packet("10.0.1.1", "10.0.1.2", "VOIP Packet 1", 0),
        Packet("10.0.2.1", "10.0.2.2", "Video Packet 1", 1),
        Packet("10.0.1.3", "10.0.1.4", "VOIP Packet 2", 0)
    ]
    
    print("--- FIFO Scheduler Output ---")
    fifo_result = fifo_scheduler(packets)
    for p in fifo_result:
        print(p.payload)
        
    print("\n--- Priority Scheduler Output ---")
    priority_result = priority_scheduler(packets)
    for p in priority_result:
        print(p.payload)
