from scapy.all import rdpcap, IP, TCP
import argparse

def main(pcap_file, client_ip):
    try:
        packets = rdpcap(pcap_file)
    except Exception as e:
        print("Error Reading {}: {}".format(pcap_file, e))

    in_request = False
    start_time = 0
    last_time = 0
    byte_count = 0
    response_packets = 0

    for i, pkt in enumerate(packets):
        # skip any no checkable packets
        if not (pkt.haslayer(IP) and pkt.haslayer(TCP)):
            continue 

        if in_request and pkt[IP].src != client_ip:
            last_time = float(pkt.time)
            response_packets += 1
            byte_count += (pkt.wirelen)

        if pkt[IP].dst != client_ip and in_request:
            elapsed = round((last_time - start_time) * 1000, 2)
            if response_packets > 1 and byte_count > 105:
                print(pkt[IP].src, pkt[IP].dst, elapsed, byte_count, response_packets)
            start_time = 0
            last_time = 0
            byte_count = 0
            response_packets = 0
            in_request = False

        if pkt[IP].src == client_ip and not in_request:
            in_request = True
            start_time = float(pkt.time)
            last_time = float(pkt.time)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="response_timer", description="Given the client get me the server response times")
    parser.add_argument("--pcap-file", help="The pcap file", required=True)
    parser.add_argument("--client-ip", help="The client ip address", required=True)
    args = parser.parse_args()
    main(args.pcap_file, args.client_ip)
