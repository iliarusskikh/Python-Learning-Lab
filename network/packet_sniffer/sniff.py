from scapy.all import sniff, Raw

def catch_packet(packet):
    if packet.haslayer(Raw):
        data = packet[Raw].load.decode(
            errors="ignore"
            )
        
        if len(data) > 10:
            print(data)

print("Sniffer Started on Wifi...")
sniff(
    iface="Wi-Fi",
    filter="tcp port 80",
    prn=catch_packet
    )
                                       )
