print("🤖 Level 119 AI Job Skill Planner")

name = input("Enter your name: ")
job_goal = input("What job goal do you have? ")
skill = input("What skill do you want to practice today? ")
minutes = int(input("How many minutes will you practice today? "))

print()
print("AI Job Skill Plan for", name)
print("Job goal:", job_goal)
print("Today skill:", skill)
print("Practice time:", minutes, "minutes")

if minutes >= 30:
    print("Great practice time ✅")
elif minutes >= 10:
    print("Good short practice ✅")
else:
    print("Small start is still good ✅")

print()
print("AI Prompt:")
print("Please teach me", skill)
print("I am a beginner.")
print("My job goal is", job_goal)
print("Use short steps and give me one small example.")