# Packet Analyzer (CLI)

A lightweight command-line network packet analyzer built using Python and Scapy.
It captures live network traffic, analyzes packet data, and provides real-time statistics.

---

## Features

* Capture live network packets
* Detect protocols (TCP, UDP, ICMP)
* Extract source/destination IP and ports
* Real-time traffic statistics
* Top destination IP analysis
* Protocol-based filtering
* CLI interface for flexible usage

---

## Project Structure


packet-analyzer/
│
├── analyzer/
│   ├── sniffer.py
│   ├── parser.py
│   ├── statistics.py
│
├── main.py
├── requirements.txt
└── README.md

---

## Installation

git clone <your-repo-link>
cd packet-analyzer
pip install -r requirements.txt

---

## Usage

Run the analyzer:
sudo python3 main.py

Filter by protocol:
sudo python3 main.py --protocol tcp

Specify network interface:
sudo python3 main.py --interface eth0

---

## Example Output
![Packet Analyzer Output](screeshot.png)
---

## Tech Stack

* Python
* Scapy
* CLI (argparse)

---

## Key Concepts Learned

* Network packet structure (IP, TCP, UDP, ICMP)
* Real-time packet capture
* Data parsing and analysis
* CLI tool development
* Modular software design

---

## Disclaimer

This tool is for educational purposes only.
Use responsibly on networks you own or have permission to analyze.

---

