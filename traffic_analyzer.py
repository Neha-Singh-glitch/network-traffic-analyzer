import pyshark

capture = pyshark.LiveCapture(interface='Wi-Fi')

print("Starting packet capture...")

for packet in capture.sniff_continuously(packet_count=10):
    try:
        print(f"Protocol: {packet.highest_layer}")
    except:
        pass