import time
import random

# Sender side
def sender(data, timeout=2):
    for i, packet in enumerate(data):
        while True:
            print(f"Sending packet {i + 1}: {packet}")
            ack = simulate_receiver(packet, timeout)  # Wait for ACK from receiver
            if ack:
                print(f"Packet {i + 1} acknowledged.")
                break
            else:
                print(f"Timeout. Resending packet {i + 1}...")

# Receiver side (simulates receiving a packet and sending an ACK)
def simulate_receiver(packet, timeout):
    # Simulate random packet loss or delay
    time.sleep(1)
    if random.random() < 0.3:  # 30% chance of packet loss
        print("Simulating packet loss.")
        return False
    return True  # 70% chance of successful ACK

# Example data (packets)
data = ["Packet 1", "Packet 2", "Packet 3"]
sender(data)
