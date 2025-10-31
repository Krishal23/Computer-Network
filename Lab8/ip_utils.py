def ip_to_binary(ip_address: str) -> str:
    #Converts a dotted-decimal IP address string to a 32-bit binary string.
    octets = ip_address.split('.')
    binary_octets = [f'{int(octet):08b}' for octet in octets]
    return "".join(binary_octets)

def get_network_prefix(ip_cidr: str) -> str:
    #Converts a CIDR string to its binary network prefix.
    ip_address, prefix_length = ip_cidr.split('/')
    prefix_length = int(prefix_length)
    binary_ip = ip_to_binary(ip_address)
    return binary_ip[:prefix_length]
