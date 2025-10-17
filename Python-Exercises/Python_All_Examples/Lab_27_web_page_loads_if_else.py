# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time = float(input("Enter web page load time in seconds : "))

if load_time <= 3:
    print("Page load is fast", load_time, "seconds")
else:
    print("⚠️ Page load too slow", load_time, "seconds" )