"""
Expression    	Returns	                         When executed

wrapper	       the function object itself	     Not yet executed
wrapper()	   the result of running wrapper() 	 Executed immediately

So in decorators, always return wrapper (no parentheses) to defer execution until
someone calls the decorated function.

"""
import time


def time_decor(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("total time taken by function is ", end_time - start_time)

    return wrapper()


def print_logs(func):
    def wrapper():
        print("Start Logs")
        func()
        print("End Logs")

    return wrapper()


# # Apply decorators (bottom → top order)
# test_ui_1 = time_decor(print_logs(test_ui_1))

@time_decor
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function_1")
    time.sleep(2)


"""
Step A: print_logs(test_ui_1)

func inside print_logs is the original test_ui_1.

wrapper() inside print_logs runs immediately because of return wrapper().

Prints "Start Logs".

Calls func() → runs the original test_ui_1:

Add a function, time taken by this function_1


(sleeps for ~2 seconds).

Prints "End Logs".

wrapper() returns None.

So print_logs(test_ui_1) itself returns None.

Result: after this step, we are effectively calling
time_decor(None).

Step B: time_decor(None)

Now func inside time_decor is None.

wrapper() inside time_decor is defined and immediately executed.

Inside wrapper():

start_time = time.time() → prints a timestamp.

func() is attempted… but func is None.

This causes a runtime error:

TypeError: 'NoneType' object is not callable


That happens while Python is still defining test_ui_1, i.e., during import/initial execution.

5️⃣ What never happens

The name test_ui_1 is never successfully assigned.

You never get a callable function you can run later.

The script stops with a TypeError before finishing.

🟢 Key Takeaways

Decorators normally return a function, not the result of calling that function.

Correct pattern: return wrapper

Writing return wrapper() calls the wrapper right away and usually returns None.

With stacked decorators, evaluation order is bottom to top:

print_logs runs first, immediately executes the function.

Its return (None) is passed to time_decor.

time_decor then tries to run func(), but func is None, causing an error.


"""
