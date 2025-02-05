"""
Author: Viktor Grygoriev
Assignment: #1
"""

gym_member = "Alex Alliton"  # string
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# Dictionary: Keys are friends' names (string), values are tuples of workout minutes for three activities (integer)
workout_stats = {
    "Alex": (30, 45, 20),  # yoga, running, weightlifting
    "Jamie": (25, 35, 30),
    "Taylor": (40, 50, 25)
}

for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

workout_list = [] # list of lists (2D list)
for friend in workout_stats:
    if not friend.endswith("_Total"):
        workout_list.append(list(workout_stats[friend]))

yoga_running_minutes = []
for row in workout_list:
    yoga_running_minutes.append(row[:2])

print("Yoga and Running minutes:", yoga_running_minutes)

weightlifting_minutes = []
for row in workout_list[-2:]:
    weightlifting_minutes.append(row[2])

print("Weightlifting minutes for the last two friends:", weightlifting_minutes)

for friend in workout_stats:
    if friend.endswith("_Total") and workout_stats[friend] >= 120:
        print(f"Great job staying active, {friend.replace('_Total', '')}!")

friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    minutes = workout_stats[friend_name]
    total_minutes = workout_stats.get(f"{friend_name}_Total", 0)
    print(f"{friend_name}'s workout minutes: {minutes}")
    print(f"{friend_name}'s total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

    total_friends = [friend for friend in workout_stats if friend.endswith("_Total")]
    highest_friend = total_friends[0]
    lowest_friend = total_friends[0]

    for friend in total_friends:
        if workout_stats[friend] > workout_stats[highest_friend]:
            highest_friend = friend
        if workout_stats[friend] < workout_stats[lowest_friend]:
            lowest_friend = friend

print(f"Friend with the highest total workout minutes: {highest_friend.replace('_Total', '')}")
print(f"Friend with the lowest total workout minutes: {lowest_friend.replace('_Total', '')}")
