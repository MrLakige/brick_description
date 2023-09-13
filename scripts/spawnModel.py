#!/bin/python3
'''
    Provides different plug and play visualizers from an urdf
    can be used as script to visualize the models from the command line
    author: G. Fadini
'''
import roslaunch
import tf
import numpy as np
import rospy as ros
from rospy import Time

def spawnModel(model_name, pos, tf_broadcaster):
    package = 'gazebo_ros'
    executable = 'spawn_model'
    name = 'spawn_brick'
    namespace = '/'
    param_name = model_name+'_description'
    
    args = '-urdf -param '+param_name+' -model '+model_name+' -x '+  str(pos[0])+ ' -y '+  str(pos[1])+ ' -z '+  str(pos[2])
    node = roslaunch.core.Node(package, executable, name, namespace,args=args,output="screen")
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()
    process = launch.launch(node)
    
    tf_broadcaster.sendTransform(pos, (0.0, 0.0, 0.0, 1.0), ros.Time.now(),'/'+model_name, '/world')


if __name__ == '__main__':
    ros.init_node('spawn_node_python', anonymous=True)
    
    broadcaster1 = tf.TransformBroadcaster()    
    broadcaster2 = tf.TransformBroadcaster()    
    spawnModel('X1-Y3-Z2', np.array([1.5, 0.,0.]), broadcaster1)
    spawnModel('X2-Y2-Z2', np.array([2.0, 0.,0.]), broadcaster2)
    
    spin()
