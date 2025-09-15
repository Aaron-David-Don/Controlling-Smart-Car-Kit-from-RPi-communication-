#!/usr/bin/env python3

import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    print("Enter '1' to move the vehicle, '0' to stop. Type 'exit' to quit.")

    while True:
        user_input = input("Send to Arduino (0/1): ").strip()

        if user_input == 'exit':
            print("Exiting program.")
            break

        if user_input not in ['0', '1']:
            print("Invalid input! Please enter '0' or '1'.")
            continue

        ser.write(user_input.encode())


        print(f"Sent '{user_input}' to Arduino.")

        time.sleep(0.1)
