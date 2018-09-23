#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32


def publish():

    time=1
    k = 1
    n = 4
    pub = rospy.Publisher('/budaraju', Float32, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(0.05) # 0.05hz
    while not rospy.is_shutdown():
        msg = float(k) #% rospy.get_time()
        rospy.loginfo(msg)
        pub.publish(msg)
        k+=n
        time+=1
        rate.sleep()


if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
