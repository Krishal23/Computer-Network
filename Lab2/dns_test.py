import socket
import dns.resolver
from datetime import datetime

def dns_lookup(domain_name):
    try:
        ip_addr = socket.gethostbyname(domain_name)
    except Exception as e:
        ip_addr = f"Unable to resolve IP: {e}"

    records = {}
    for rtype in ['A', 'MX', 'CNAME']:
        try:
            answers = dns.resolver.resolve(domain_name, rtype)
            records[rtype] = [str(answer) for answer in answers]
        except Exception as err:
            records[rtype] = [f"Error fetching {rtype} record: {err}"]

    print(f"\nDomain: {domain_name}")
    print(f"Resolved IP: {ip_addr}")
    for rtype, rec_list in records.items():
        print(f"{rtype} Records:")
        for rec in rec_list:
            print(f"  {rec}")

    log_file = "dns_query_log.txt"
    with open(log_file, "a") as f:
        f.write(f"\n=== DNS Query for {domain_name} at {datetime.now()} ===\n")
        f.write(f"Resolved IP: {ip_addr}\n")
        for rtype, rec_list in records.items():
            f.write(f"{rtype} Records:\n")
            for rec in rec_list:
                f.write(f"  {rec}\n")
        f.write("\n")

    print(f"\nResults saved to '{log_file}'")

def main():
    domain_input = input("Enter a domain name to check: ")
    dns_lookup(domain_input)

if __name__ == "__main__":
    main()
