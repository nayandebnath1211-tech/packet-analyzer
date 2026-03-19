from collections import defaultdict

total_packets = 0
tcp_count = 0
udp_count = 0
icmp_count = 0

ip_counter = defaultdict(int)

def update_stats(protocol, dst_ip):
    global total_packets, tcp_count, udp_count, icmp_count

    total_packets += 1
    ip_counter[dst_ip] += 1

    if protocol == "TCP":
        tcp_count += 1
    elif protocol == "UDP":
        udp_count += 1
    elif protocol == "ICMP":
        icmp_count += 1

def print_summary():

    print("\n===== TRAFFIC SUMMARY =====")
    print(f"Total Packets: {total_packets}")
    print(f"TCP: {tcp_count}")
    print(f"UDP: {udp_count}")
    print(f"ICMP: {icmp_count}")

    print("\nTop Destination IPs")

    top_ips = sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)[:5]

    for ip, count in top_ips:
        print(f"{ip} : {count}")

    print("===================================\n")
