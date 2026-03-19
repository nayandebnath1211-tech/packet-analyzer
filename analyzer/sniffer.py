from scapy.all import sniff
from analyzer.parser import parse_packet
from analyzer.statistics import update_stats, print_summary, total_packets

def start_sniffer(interface=None, protocol_filter=None):

    print("Starting packet analyzer...")
    
    def filtered_process(packet):
        result = parse_packet(packet)

        if result is None:
            return

        protocol, src_ip, src_port, dst_ip, dst_port, length = result

        if protocol_filter:
            if protocol.lower() != protocol_filter.lower():
                return
        
        update_stats(protocol, dst_ip)

        print("----- Packet ------")
        print(f"Protocol: {protocol}")
        print(f"Source: {src_ip}:{src_port}")
        print(f"Destination: {dst_ip}:{dst_port}")
        print(f"Packet Length: {length} bytes")

        if total_packets % 10 == 0:
            print_summary()
    
    sniff(prn=filtered_process, store=False, iface=interface)
            
