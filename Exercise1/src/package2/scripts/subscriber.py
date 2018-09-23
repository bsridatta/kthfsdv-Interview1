#!/usr/bin/env python
#from lib2to3.pgen2.conv import Converter

import rospy
from std_msgs.msg import Float32






q=0.15
result=0.0

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'Reading from nodeA :%s', data.data)
    result = float(data.data) / q
    ans = float(result)
    publish(ans)

def publish(ans):


    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
    rate = rospy.Rate(0.05)  # 0.05hz
    #while not rospy.is_shutdown():
    msg = ans  # % rospy.get_time()
    rospy.loginfo(msg)
    pub.publish(msg)
    rate.sleep()



def listener():

    rospy.init_node('nodeB', anonymous=True)
    rospy.Subscriber('/budaraju', Float32, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
