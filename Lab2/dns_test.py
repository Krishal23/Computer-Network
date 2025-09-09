import socket
import dns.resolver
from datetime import datetime

def resolve_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except Exception as e:
        return f"Error resolving IP: {e}"

# Function to get A, MX, and CNAME records
def get_records(domain):
    a_records = []
    mx_records = []
    cname_records = []
    record_types = ['A', 'MX', 'CNAME']

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            for rdata in answers:
                if record_type == 'A':
                    a_records.append(rdata.to_text())
                elif record_type == 'MX':
                    mx_records.append(rdata.to_text())
                elif record_type == 'CNAME':
                    cname_records.append(rdata.to_text())
                print(f"{record_type} : {rdata.to_text()}")
        except Exception as e:
            print(f"Could not resolve {record_type} records: {e}")

    return a_records, mx_records, cname_records

# Function to log the results into a file
def log_results(domain, ip_address, a_records, mx_records, cname_records):
    filename = "dns_query_log.txt"
    with open(filename, "a") as file:
        file.write(f"\nDNS Query for {domain} at {datetime.now()}\n")
        file.write(f"Resolved IP Address: {ip_address}\n\n")

        file.write("A Records:\n")
        if a_records:
            for record in a_records:
                file.write(f"  {record}\n")
        else:
            file.write("  No A records found.\n")

        file.write("\nMX Records:\n")
        if mx_records:
            for record in mx_records:
                file.write(f"  {record}\n")
        else:
            file.write("  No MX records found.\n")

        file.write("\nCNAME Records:\n")
        if cname_records:
            for record in cname_records:
                file.write(f"  {record}\n")
        else:
            file.write("  No CNAME records found.\n")

# Main function
def main():
    domain = input("Enter domain name: ")

    ip_address = resolve_ip(domain)
    print(f"\nResolved IP Address: {ip_address}\n")

    # Get the DNS records
    a_records, mx_records, cname_records = get_records(domain)

    # Log the results
    log_results(domain, ip_address, a_records, mx_records, cname_records)

    print(f"\nResults logged to 'dns_query_log.txt'")

if __name__ == "__main__":
    main()
