from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP

# Define a callback function to process packets
def process_packet(packet):
    # Check if the packet has an Ethernet layer
    if Ether in packet:
        print("\nNew packet captured:")
        
        # Extract and print the Ethernet layer information
        eth = packet[Ether]
        print(f"Ethernet | Source: {eth.src} | Destination: {eth.dst} | Type: {eth.type}")
        
        # Check if the packet has an IP layer
        if IP in packet:
            ip = packet[IP]
            print(f"IP | Source: {ip.src} | Destination: {ip.dst} | Protocol: {ip.proto}")
            
            # Check if the packet has a TCP layer
            if TCP in packet:
                tcp = packet[TCP]
                print(f"TCP | Source Port: {tcp.sport} | Destination Port: {tcp.dport} | Flags: {tcp.flags}")
            
            # Check if the packet has a UDP layer
            elif UDP in packet:
                udp = packet[UDP]
                print(f"UDP | Source Port: {udp.sport} | Destination Port: {udp.dport}")
            
            # Check if the packet has an ICMP layer
            elif ICMP in packet:
                icmp = packet[ICMP]
                print(f"ICMP | Type: {icmp.type} | Code: {icmp.code}")
    

# Start sniffing packets
sniff(prn=process_packet, store=False)
