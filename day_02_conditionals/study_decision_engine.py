user_name = input("What is your name? ").strip()
print()
print(f"Hi {user_name}!")

print()
print("Welcome to the Study Decision Engine.")
print("I'll help you decide what kind of study session makes sense today.")

print()
while True:
    energy_level = input("Please rate your energy level from 1 to 10. ").strip()

    if energy_level.isdigit():
        energy_level = int(energy_level)

        if energy_level >=1 and energy_level <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    else:
        print("Please enter a whole number, like 1, 5, or 10.")

print()
while True:
    stress_level = input("Please rate your stress level from 1 to 10. ").strip()

    if stress_level.isdigit():
        stress_level = int(stress_level)

        if stress_level >= 1 and stress_level <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    else:
        print("Please enter a whole number, like 1, 5, or 10.")

print()
while True:
    study_time = input("Please enter the number of minutes you have available to study. ").strip()

    if study_time.isdigit():
        study_time = int(study_time)

        if study_time >= 1:
            break
        else:
            print("Please enter a number of minutes greater or equal to 1.")
    else:
        print("Please enter minutes as a whole number, like 1, 25, or 60.")

print()
study_topic = input("What topic or subject are you studying today? ").strip()

print()
study_goal = input("What is one thing you want to accomplish today? ").strip()

print()
if energy_level <= 3 or stress_level >= 8:
    study_mode = "Rest / Reset 😴"
    reason = "Your energy is low or your stress is high, so recovery may help more than forcing a study session."
    next_action = "Take a 10-minute reset, drink water, breath, and then choose one tiny task."

elif study_time < 15:
    study_mode = "Quick Review ⚡"
    reason = "You do not have much time, so a short review will be more realistic than deep work."
    next_action = f"Review one small part of {study_topic}, such as notes, flashcards, or one previous mistake."

elif energy_level >= 8 and stress_level <= 5 and study_time >= 45:
    study_mode = "Deep Study 🧠"
    reason = "Your energy, stress, and available time are lined up well for focused learning."
    next_action = f"Pick one difficult part of {study_topic} and focus on it for a strong study block."

elif energy_level >= 6 and stress_level <= 6 and study_time >= 30:
    study_mode = "Coding Practice 💻"
    reason = "You have enough energy and time for active practice."
    next_action = f"Work on one small project, feature, or practice problem related to {study_topic}."

else:
    study_mode = "Light Review 🌱"
    reason = "You have enough capacity to make progress, but a lighter task may be better today."
    next_action = f"Review your notes or redo an easier exercise related to {study_topic}."

print()
print("---Study Plan Summary---")
print(f"Name: {user_name}")
print(f"Energy Level: {energy_level}/10")
print(f"Stress Level: {stress_level}/10")
print(f"Study Time: {study_time} minutes")
print(f"Study Topic: {study_topic}")
print(f"Gooal: {study_goal}")
print()
print(f"Recommended Study Mode: {study_mode}")
print(f"Reason: {reason}")
print(f"Next action: {next_action}")