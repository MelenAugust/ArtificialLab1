# Make sure to have the server side running in V-REP:
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
import random
import Lab1_Agents_Task1_World as World
from Agent import Agent

# connect to the server
robot = World.init()
agent = Agent()
# print important parts of the robot
print(sorted(robot.keys()))

motorSpeed = dict(speedLeft=0.0, speedRight=0.0)

while robot:
    simulationTime = World.getSimulationTime()


    if simulationTime%10000==0:
        # print some useful info, but not too often
        print ('Time:',simulationTime,\
               'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
               "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))

    #agent.random_action()
    #agent.fixed_action(simulationTime)
    agent.reflex_action()
    #agent.memory_action(simulationTime)

    # assign speed to the wheels
    World.setMotorSpeeds(agent.motorSpeed)
    # try to collect energy block (will fail if not within range)
    #if simulationTime % 1000 == 0:
     #   print("Trying to collect a block...", World.collectNearestBlock())




