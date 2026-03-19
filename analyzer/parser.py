from scapy.all import IP, TCP, UDP, ICMP

def parse_packet(packet):
    if not packet.haslayer(IP):
        return None

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    length = len(packet)

    protocol = "OTHER"
    src_port = "-"
    dst_port = "-"

    if packet.haslayer(TCP):
        protocol = "TCP"
        stc_port = packet[TCP].sport
        dst_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    elif packet.haslayer(ICMP):
        protocol = "ICMP"

    return protocol, src_ip, src_port, dst_ip, dst_port, length
