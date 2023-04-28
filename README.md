# Red Thread - hóng xiàn (红线)

Hóng Xiàn is a Python script designed to communicate with Quectel M35A modules and manage the sending and receiving of SMS messages. The script supports multiple modules and can automatically detect and connect to available modules.

## Prerequisites

   Python 3.x
   PySerial library
   Python-dotenv library

## Installation

   Clone or download the Red Thread repository.
   Install the required libraries by running the following command in the terminal:

    pip install pyserial python-dotenv

Create a .env file in the root directory of the script with the following format:


    SIM1=(PIN CODE FOR SIM 1)
    SIM2=(PIN CODE FOR SIM 2)
    SIM3=(PIN CODE FOR SIM 3)
    '''


Replace (PIN CODE FOR SIM X) with the actual PIN code for each Quectel M35A module that you want to use with the script. Note that you can include as many SIM cards as you need.
Usage

   Connect the Quectel M35A modules to the computer via USB.
   Open a terminal and navigate to the directory where the script is located.
   Run the script by typing the following command in the terminal:

    python hong_xian.py

   The script will automatically detect and connect to available Quectel M35A modules, and start monitoring for incoming SMS messages.
   When a new SMS message is received, the script will display a message indicating the connected phone number and alert the user that a new message is available.
   
## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the GitHub repository.

## License

[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)
