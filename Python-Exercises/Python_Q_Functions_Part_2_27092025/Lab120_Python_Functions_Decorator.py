import time

def time_decor(func):

    def wrapper():
        start_time = time.time()
        print("Start Time", start_time)
        func()
        end_time = time.time()
        print("End Time", end_time)
        print("total time taken by function is ", end_time-start_time)
    return wrapper

def print_logs(func):
    def wrapper():
        print("Start Logs")
        func()
        print("End Logs")
    return wrapper

@time_decor
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function_1")
    time.sleep(2)

test_ui_1()

@time_decor
def test_ui_2():
    print("Add a function, time taken by this function_2")
    time.sleep(5)

#test_ui_2()


"""
What happens when you call test_ui_1()

Call sequence (with numbering to show nesting):

1. test_ui_1() → enters time_decor.wrapper (outer)

        start_time = time.time() (printed)

        time_decor.wrapper calls func() — this func is print_logs.wrapper

2. Enter print_logs.wrapper (inner)

        prints "Start Logs"

        calls its func() — this func is the original test_ui_1 function body

3. Enter original test_ui_1

        prints "Add a function, time taken by this function_1"

        time.sleep(2) runs

        original returns

4. Back in print_logs.wrapper

        prints "End Logs"

        returns to caller

5. Back in time_decor.wrapper

        end_time = time.time() (printed)

        prints "total time taken by function is ", end_time - start_time

        returns

Console output order you will see for test_ui_1():

<start timestamp printed by time_decor>
Start Logs
Add a function, time taken by this function_1
End Logs
<end timestamp printed by time_decor>
total time taken by function is  2.0...


(Note: <start timestamp> and <end timestamp> are epoch floats from time.time().)
"""