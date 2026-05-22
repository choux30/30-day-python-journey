user_name = input("Enter your name: ").strip()
print()
print(f"Hello {user_name}, welcome to the pomodoro timer.")
print()
study_time = input("How many minutes would you like to study for? ").strip()
times = int(study_time)
print()
print(f"Study duration: {study_time} minutes")

print()
timer_start = input("Press Enter to start timer ").strip()
print()
print("Your timer has started.")

import time



while times > 0:
    print(times)
    time.sleep(60)
    times -= 1

print("Break Time!")

