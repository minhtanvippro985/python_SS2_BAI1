print("-----EMERGENCY TIRAGE SYSTEM ----")
heart_rate = int(input("Enter patient's heart rate (bpm) :"))

if heart_rate > 120:
    print("RED - Critical condition")
elif heart_rate > 100:
    print("Yellow - Abormal")
elif heart_rate < 60:
    print("Blue - bradycardia")
else:
    print("Green - stable")

print("Triage process completed")


# do >100 để lên trước nên sẽ kiểm tra điều kiện >100 trước , nếu ta nhập 130 
# điều kiện >120 sẽ bị bỏ qua