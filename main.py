import argparse
from analyzer.sniffer import start_sniffer

def main():

    parser = argparse.ArgumentParser(description="Simple Packet Analyzer")
    parser.add_argument("--interface", type=str, help="Network interface (e.g., eth0, wlan0)", default=None)
    parser.add_argument("--protocol", type=str, help="Filter by protocol (tcp, udp, icmp)", default=None)
    args = parser.parse_args()

    start_sniffer(interface=args.interface, protocol_filter=args.protocol)
if __name__ =="__main__":
    main()
