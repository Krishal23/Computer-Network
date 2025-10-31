from ip_utils import ip_to_binary

class Router:

    def __init__(self, routes: list):
        self.table = []
        self._build_forwarding_table(routes)

    def _build_forwarding_table(self, routes: list):
        #Processes the routes list and stores binary prefixes.
        for cidr_str, link in routes:
            ip_address, prefix_len_str = cidr_str.split('/')
            prefix_len = int(prefix_len_str)
            
            binary_ip = ip_to_binary(ip_address)
            network_prefix = binary_ip[:prefix_len]
            
            self.table.append((network_prefix, link))
        
        # Sort the table by prefix length, longest to shortest
        self.table.sort(key=lambda item: len(item[0]), reverse=True)

    def route_packet(self, dest_ip: str) -> str:
        #Performs a longest prefix match on the destination IP.
        binary_dest_ip = ip_to_binary(dest_ip)
        
        for prefix, link in self.table:
            if binary_dest_ip.startswith(prefix):
                return link
        
        return "Default Gateway"

# Main test case as described in the assignment
if __name__ == "__main__":
    route_list = [
        ("223.1.1.0/24", "Link 0"),
        ("223.1.2.0/24", "Link 1"),
        ("223.1.3.0/24", "Link 2"),
        ("223.1.0.0/16", "Link 4 (ISP)")
    ]
    
    router = Router(route_list)
    
    # Test cases
    print(f'223.1.1.100 -> {router.route_packet("223.1.1.100")}')
    print(f'223.1.2.5 -> {router.route_packet("223.1.2.5")}')
    print(f'223.1.250.1 -> {router.route_packet("223.1.250.1")}')
    print(f'198.51.100.1 -> {router.route_packet("198.51.100.1")}')
