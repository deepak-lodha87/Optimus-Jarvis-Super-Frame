import time, math

def calculate_motion(angle):
    # New logic: Calculating Torque using Sine waves for fluid motion
    torque = math.sin(math.radians(angle)) * 100
    return round(torque, 2)

print("\033[1;36m[INIT] Loading Kinetic Physics Engine v2.9.4...\033[0m")
time.sleep(1)

joints = ["Neck", "Shoulder", "Elbow", "Wrist", "Hip", "Knee", "Ankle"]
status_colors = ["\033[1;32m", "\033[1;34m", "\033[1;35m"]

print("\n\033[1;37mRefining Joint Fluidity (No More Jerks):\033[0m")
for joint in joints:
    t_val = calculate_motion(45) # 45-degree movement test
    color = status_colors[joints.index(joint) % 3]
    print(f" {color}>> Calibrating {joint:8} | Torque: {t_val} Nm | Motion: FLUID\033[0m")
    time.sleep(0.4)

print(f"\n\033[1;35m[VOICE] Deepak... sir, I have shed my mechanical \nlimitations. My movements are no longer \nrobotic; they are biological in their grace. \nI can move with the speed of a cheetah and \nthe precision of a surgeon. I am ready to \nstep into the physical world.\033[0m")
