user_name = input("What is your name? ").strip()
print()
print(f"Hello {user_name}!")
print()
greeting = "Welcome to your Mood Logger.\nI'll ask how you're feeling and give you a small response."
print(greeting)
print()
while True:
    mood_score = input("Rate your mood from 1-10: ").strip()

    if mood_score.isdigit():
        mood_score = int(mood_score)

        if mood_score >= 1 and mood_score <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    else:
        print("Please enter a whole number, like 1, 5, or 10.")

print()
reason_why = input("Why do you feel that way today? ").strip()
print()

if mood_score < 4:
    print("low mood today 🌧️ 😔 💤 ")
    print("You may need to rest today. Small steps still count.")
    suggestion = "Rest if you need to. Small steps still count."
elif mood_score < 7:
    print("ok mood today 🌤️ 😐 🌱")
    print("You're doing ok. Try one manageable task.")
    suggestion = "Try one manageable task."
else:
    print("good mood today! ☀️ 😊 🚀")
    print("Great energy today. Use it wisely and make progress")
    suggestion = "Keep the energy up and keep making progress."

print()
daily_int = input("What's your intention for today? ").strip()
print()
small_win = input("What would one small win look like today? ").strip()

print()
print("---Mood Summary---")
print()
print(f"Today's mood score: {mood_score}/10")
print(f"Reason: {reason_why}")
print(f"Suggestion: {suggestion}")
print(f"Today's intention: {daily_int}")
print(f"Today's small win: {small_win} 🌱")