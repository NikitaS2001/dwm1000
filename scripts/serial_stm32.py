#!/usr/bin/ python3

import serial
import rospy
from dwm1000.msg import BeaconDataArray, BeaconData

def main():
	#get param
	port = "/dev/ttyUSB0" #rospy.get_param('port')
	baud = "115200" # rospy.get_param('baud')
	topic_pub = "dwm1000/beacons" #rospy.get_param('topic_pub')
	
	pub = rospy.Publisher(topic_pub, BeaconDataArray, queue_size=10)
	rospy.init_node("dwm1000", anonymous=True)
	rate = rospy.Rate(40)
	pub_msg = BeaconDataArray()
	
	#dwm1000
	ser = serial.Serial(port, int(baud), timeout=1)
	ser.flush()
	while not rospy.is_shutdown():
		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			rospy.loginfo(line)
			beacon = BeaconData()
			beacon.id = 0
			beacon.dist = 1
			a = []
			a.append(beacon)
			a.append(beacon)
			pub_msg = a
			pub.publish(pub_msg)
			rate.sleep()
if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException():
		pass
	
    
