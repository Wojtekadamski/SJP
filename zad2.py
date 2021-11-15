
def duration():
    hour = int(input("Starting time (hours): "))
    mins = int(input("Starting time (minutes): "))
    dura = int(input("Event duration (minutes): "))
    return print(int(((hour+dura/60+mins/60))%24),":",(mins+dura)%60)

print(duration())
# Write your code here.
