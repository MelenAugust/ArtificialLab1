import random
import math, time
import Lab1_Agents_Task1_World as World
from Lab1_Agents_Task1_World import collectNearestBlock


class Agent:
    def __init__(self):
        self.motorSpeed = dict(speedLeft=0.0, speedRight=0.0)
        self.target_block = None
        self.previous_distance = float('inf')  # Start with an infinitely high initial distance
        self.last_check_time = 0

    def try_collect_block(self):

        collect_result = World.collectNearestBlock()

        if collect_result == 'Energy collected :)':
            print("Block collected successfully!")
            # Reset target to allow searching for a new block
            self.target_block = None
            self.previous_distance = float('inf')


    def random_action(self):

        self.motorSpeed = dict(
            speedLeft=random.uniform(-1.0, 1.0),
            speedRight=random.uniform(-1.0, 1.0)
        )
        self.try_collect_block()

    def fixed_action(self,simulationTime):

        cycle_time = simulationTime % 22000

        if cycle_time < 6000:
            self.motorSpeed = dict(speedLeft=2, speedRight=2)
        elif cycle_time < 7000:
            self.motorSpeed = dict(speedLeft=0.5, speedRight=-0.5)
        elif cycle_time < 9000:
            self.motorSpeed = dict(speedLeft=2, speedRight =2)
        elif cycle_time < 14000:
            self.motorSpeed = dict(speedLeft=0.5, speedRight=-0.5)
        elif cycle_time < 16000:
            self.motorSpeed = dict(speedLeft=2, speedRight=2)

        self.try_collect_block()

    def reflex_action(self):
        left_sensor = World.getSensorReading("ultraSonicSensorLeft")
        right_sensor = World.getSensorReading("ultraSonicSensorRight")

        if left_sensor != float('inf') or right_sensor != float('inf'):
            self.motorSpeed = random.choice(            # 50/50 chance of turning left or right to prevent same loop
                [
                    dict(speedLeft=1, speedRight=-1),  # Turn right
                    dict(speedLeft=-1, speedRight=1)  # Turn left
                ]
            )
        else:
            self.motorSpeed = dict(speedLeft=2.0, speedRight=2.0)

        self.try_collect_block()

    def memory_action(self,simulationTime):

        if not self.target_block:
            blocks = World.findEnergyBlocks()
            if blocks:
                self.target_block = blocks[0]
                self.previous_distance = self.target_block[2]
            else:
                print("No blocks found.") #no blocks left
                return

        # Check the current distance to the target block
        blocks = World.findEnergyBlocks()
        current_distance = blocks[0][2] if blocks else float('inf')

        if simulationTime - self.last_check_time > 200:  # Check every 200 ms in simulation time
            
            if current_distance < self.previous_distance:
                print("Moving closer to the target. Continuing forward.")
                self.motorSpeed = dict(speedLeft=1.5, speedRight=1.5)
            else:
                print("Getting farther from the target. Changing direction.")
                self.motorSpeed = random.choice(
                   
                    [
                    dict(speedLeft=0.5, speedRight=-0.5),  # Turn right
                    dict(speedLeft=-0.5, speedRight=0.5),  # Turn left
                    ]

                )
                
            # Check for obstacles
            left_sensor = World.getSensorReading("ultraSonicSensorLeft")
            right_sensor = World.getSensorReading("ultraSonicSensorRight")

            if left_sensor != float('inf') or right_sensor != float('inf'):
                if left_sensor < 0.5 or right_sensor < 0.5:
                    print("Obstacle detected. Changing direction.")
                    self.motorSpeed = dict(speedLeft=-5, speedRight=-5)  # Move backwards
                    if left_sensor < right_sensor:
                        self.motorSpeed = dict(speedLeft=5, speedRight=-5)  # turn right

                    elif right_sensor < left_sensor:
                        self.motorSpeed = dict(speedLeft=-5, speedRight=5)  # turn left

                    else:
                        self.motorSpeed = random.choice(
                   
                        [
                        dict(speedLeft=5, speedRight=-5),  # Turn right
                        dict(speedLeft=-5, speedRight=5),  # Turn left
                        ]

                        )
                    

            self.previous_distance = current_distance
            self.last_check_time = simulationTime


        self.try_collect_block()




