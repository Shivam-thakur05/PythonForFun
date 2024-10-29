"""
    A drone navigation system needs to determine if it can safely travel to a given destination based on its current battery level. The drone's battery %age should be at least 30% to start the journey. Now, the drone needs to visit multiple waypoints. Each waypoint requires 10% of the battery. You need to check if the drone can visit all the waypoints with the available battery.
 
 Task 1: Write a Python program that takes the current battery %age and the number of waypoints as input. Use the loop to check if the drone can visit all the waypoints. Print "Drone can visit all waypoints" or "Drone cannot visit all waypoints".
    
"""


current_battery = int(input("enter the age of the battery in percentage : "))

if current_battery < 30:
    print("No battery power for travel!");


else:
    print("ready for travel")
    waypoint = int(input("enter the waypoints : "))

    while waypoint > 0:
        if current_battery >= 30:
            current_battery = current_battery - 10;
            waypoint = waypoint-1;
        else:
            break

    if waypoint == 0:
        print("Drone can visit all waypoints")
    else:
        print("Drone cannot visit all waypoints")

        

        
        
        