import serial
import os
import time
from serial.tools import list_ports
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Find all Quectel M35A modules
modules = []
for port in list_ports.comports():
    try:
        ser = serial.Serial(port.device, 115200, timeout=1)
        ser.write(b'AT\r\n')
        response = ser.read(1000).decode('utf-8')
        if 'Quectel' in response and 'M35A' in response:
            modules.append(port.device)
            ser.write(b'AT+CMGF=1\r\n')
            response = ser.read(1000).decode('utf-8')
            print(f"Phone {response.strip()} is connected.")
        ser.close()
    except:
        pass

# Set up a list of pins
pins = [os.environ.get(f'SIM{i+1}') for i in range(len(modules))]

# Set up serial connections for all modules
serials = [serial.Serial(port, 115200, timeout=1) for port in modules]

# Send PIN for each module
for i, pin in enumerate(pins):
    cmd = f'AT+CPIN="{pin}"\r\n'.encode('utf-8')
    serials[i].write(cmd)
    response = serials[i].read(1000).decode('utf-8')
    if 'OK' in response:
        print(f'Module {i+1}: PIN validated.')
    else:
        print(f'Module {i+1}: PIN validation failed.')
        continue

# Continuously read SMS messages for all modules
while True:
    for i, ser in enumerate(serials):
        # Check for new SMS messages
        ser.write(b'AT+CMGL="ALL"\r\n')
        response = ser.read(1000).decode('utf-8')

        # Print SMS messages
        if '+CMGL:' in response:
            messages = response.split('+CMGL:')
            for message in messages[1:]:
                print(f'Module {i+1}: {message.strip()}')

        # Check if module is ready to receive SMS
        ser.write(b'AT+CPMS?\r\n')
        response = ser.read(1000).decode('utf-8')
        if '+CPMS:' in response:
            message_info = response.split('+CPMS: ')[1].split(',')
            message_count = int(message_info[0]) - int(message_info[1])
            print(f'Module {i+1}: {message_count} new message(s) ready to read.')

    # Wait for a few seconds before checking again
    time.sleep(5)

# Close serial connections for all modules
for ser in serials:
    ser.close()
