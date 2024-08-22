#!/usr/bin/python3

import socket

# Define the host and port
host = "192.168.168.101"  # Replace with the actual IP address or hostname
port = 8888

# Create the socket
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    conn.connect((host, port))
    print("Connected to the server.")

    # Function to receive and decode data with error handling
    def receive_data():
        try:
            # Receive data from the server
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                print("No data received from server.")
            else:
                print("Received from server:", data)
            return data
        except socket.error as e:
            print(f"Socket error: {e}")
            return ""
        except Exception as e:
            print(f"Error receiving data: {e}")
            return ""

    # Function to extract numbers from a received message
    def extract_number(message):
        try:
            # Split the message by spaces or other delimiters
            parts = message.split()
            # Extract the last part as a number
            number = int(parts[-1])  # Assuming the number is the last part
            return number
        except (ValueError, IndexError) as e:
            print(f"Error extracting number: {e}")
            return None

    # Receive and process data
    print("Receiving data...")
    a_message = receive_data()  # Receive the message with the first number
    b_message = receive_data()  # Receive the message with the second number
    c_message = receive_data()  # Receive the message with the third number

    # Extract numbers from messages
    a = extract_number(a_message)
    b = extract_number(b_message)
    c = extract_number(c_message)

    # Ensure all numbers are valid
    if a is None or b is None or c is None:
        print("Error: One or more numbers could not be extracted.")
        raise SystemExit

    # Perform the calculation: (a + b) * c
    result = (a + b) * c
    print(f"Calculated result: {result}")

    # Send the result back to the server
    try:
        conn.sendall(str(result).encode('utf-8'))
        print("Result sent to server.")
    except socket.error as e:
        print(f"Socket error when sending result: {e}")
    except Exception as e:
        print(f"Error sending result to server: {e}")

    # Optionally, receive and print the final message or flag from the server
    final_message = receive_data()
    print("Final message from server:", final_message)

finally:
    # Close the connection
    conn.close()
    print("Connection closed.")
