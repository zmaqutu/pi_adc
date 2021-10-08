import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
# create the spi bus 
 spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select) 
 cs = digitalio.DigitalInOut(board.D5)
# create the mcp object 
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0 
chan = AnalogIn(mcp, MCP.P0)
print(’Raw ADC Value: ’, chan.value)
print(’ADC Voltage: ’ + str(chan.voltage) + ’V’)
import threading

class prac4:
	def __init__(self):
		self.sample_rate = 10
		self.sampling_rates = [10, 5, 1]
		self.counter = 0
	def push_button(self, channel_number):
		if GPIO.input(channel_number == False):
			if i >=2:
				counter = 0
			self.counter += 1
			sample_rate = sampling_rates[self.counter]
	def calculate_temp(self, channel1_reading,channel2_reading):
		return round(100*(channel1_reading – 0.5) , 2) #round temp to 2dec 
def start_prac_thread(self):
	thread = threading.Timer(sample_rate, start_prac_thread)
	thead.start()
	channel1_reading = AnalogIn(mcp,MCP.P1)
	channel_2_reading = AnalogIn(mcp,MCP.P2 )
	temperature = calculate_temp(channel1_reading, channel2_reading)
	print(“”) # fix the formatting of this print statement empty for now
		

class driverClass:
	def main():
		print(“Inside driver”)
		practical4 = prac4()
		prac4.start_prac_thread()
		while True:
			continue
	if __name__ == “__main__”:
		main()
