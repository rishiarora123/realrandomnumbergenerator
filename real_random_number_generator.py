import hashlib
import time
import psutil  # You may need to install this library: pip install psutil

def generate_random_number():
    # Get timestamp
    current_time = time.time()
    timestamp_hash = hashlib.sha256(str(current_time).encode()).hexdigest()

    # Get CPU speed
    cpu_speed = psutil.cpu_freq().current
    cpu_speed_hash = hashlib.sha256(str(cpu_speed).encode()).hexdigest()

    # XOR the two hashes
    random_number = int(timestamp_hash, 16) ^ int(cpu_speed_hash, 16)

    return random_number

# Example usage
random_number = generate_random_number()
print("Random Number:", random_number)
