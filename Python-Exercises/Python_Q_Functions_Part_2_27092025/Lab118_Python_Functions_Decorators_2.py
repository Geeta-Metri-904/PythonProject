def add_before_UI_after_UI(func):

    def wrapper():
        print("Before running the UI TC")
        print("Start the Browser")
        func()
        print("After running the UI TC")
        print("Quit the Browser")
    return wrapper()


@add_before_UI_after_UI
def test_UI():
    print(">>>> I will test the UI")