# Name:       Gaganveer Singh
# Student ID: 2210994783
impo
rt smbus  # Library for I2C communication
import time

# Address for BH1750 Sensor
BH1750_ADDRESS = 0x23
# Operating mode for BH1750: High-resolution mode
HIGH_RESOLUTION_MODE = 0x20

# Initialize the I2C bus
i2c_bus = smbus.SMBus(1)

# Function to get light value
def read_light_intensity():
    # Read the light intensity data in high-resolution mode
    raw_data = i2c_bus.read_i2c_block_data(BH1750_ADDRESS, HIGH_RESOLUTION_MODE)
    
    # Convert the raw data bytes to a lux value
    luminance = (raw_data[1] + (256 * raw_data[0])) / 1.2
    return luminance

try:
    while True:
        # Read the light intensity
        light_value = read_light_intensity()
        print(f"Light Intensity: {light_value} lux")
		
        # Classify and print light conditions based on the lux value
        if light_value < 1:
            print("Too Dark")
        elif 1 <= light_value < 10:
            print("Dark")
        elif 10 <= light_value < 100:
            print("Dimly Lit")
        elif 100 <= light_value < 1000:
            print("Medium")
        elif 1000 <= light_value < 25000:
            print("Bright")
        else:
            print("Too Bright")
		
        # Wait for 1 second before reading the next value
        time.sleep(1.0)

except KeyboardInterrupt:
    # Handle keyboard interrupt and exit the program gracefully
    print("Exiting the program...")
