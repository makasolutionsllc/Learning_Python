"""
This is a simple class to handle serial communication with a device connected to the computer
The class has methods to send data to the device, read data from the device, open the serial connection and close the serial connection
The class also has a constructor that takes the port number and baudrate as arguments
The class uses the pyserial library to handle the serial communication
The class has a __repr__ method that returns the port number and baudrate of the serial connection
The class has a close_connection method that closes the serial connection
The class has an open_connection method that opens the serial connection
The class has a send_data method that sends data to the device


Basic building block in order to communicate with devices via serial port; you'll find it'll require some modification to work with your specific device

"""


import serial # pip install pyserial


class SerialCommunication:
    """
    Class to handle serial communication with a device connected to the computer
    port is a port number i.e COM1, COM2, COM3 etc. You can check the port number of the device in the device manager
    baudrate is the speed of communication between the computer and the device in bits per second. This can be found
    in the device's datasheet or manual.
    """
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = serial.Serial(port, baudrate) # Create a serial connection object
        self.serial_connection.timeout = 0.5 # Set the timeout for the serial connection to 0.5 seconds, this means that if the device does not respond within 0.5 seconds, the connection will be closed.

    def send_data(self, data):
        """
        Method to send data to the device, the data must be in bytes format i.e b"Hello"
        Some devices require a specific format for the data to be sent, this can be found in the device's datasheet or manual
        :param data:
        :return:
        """
        #lets make sure the data is in bytes format
        if not isinstance(data, bytes):
            raise ValueError("Data must be in bytes format")

        self.serial_connection.write(data)

    def read_data(self):
        """
        Method to read data from the device connected to the computer, sometimes the device may not respond
        so it is important to set a timeout for the serial connection. In addition, some devices may require a specific
        format for the data to be read, this can be found in the device's datasheet or manual.

        It may require .decode() method to convert the data to a readable format
        i.e data = self.serial_connection.readline().decode()

        :return:
        """
        return self.serial_connection.readline()

    def close_connection(self):
        """
        Method to close the serial connection, this is important to prevent the serial port from being blocked
        :return: None
        """
        self.serial_connection.close()
        print("Serial connection closed")

    def open_connection(self):
        """
        Method to open the serial connection
        :return: boolean True if the connection is open, False if the connection is not open
        """
        #Check if the serial connection is open
        if not self.serial_connection.isOpen():
            #we want to wrap this into a try/except block to catch any errors that may occur
            #so it won't crash the program
            try:
                self.serial_connection.open()
                return True

            except Exception as e:
                print(f"Error opening serial connection: {e}")
                return False


    def __repr__(self):
        return f"Port: {self.port}, Baudrate: {self.baudrate}"