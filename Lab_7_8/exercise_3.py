import math

addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x*y
division = lambda x, y: x/y
factorial = lambda x: 0 if x==0 else x * factorial(x-1)
power = lambda x, y: 1 if y==0 else x*power(x,y-1)
log = lambda x, y: math.log(x,y)


while True:
    try:
        params = input("Enter the operation and the numbers: ")
        if params == -1:
            break
        params = params.split()
        
        operation_chars = "asmdfpl"
        
        assert params[0].lower() in operation_chars, f"Not a valid option select from {operation_chars}"
        
        if params[0] == "a":
            assert len(params) == 3, "Number of params not correct."
            result = addition(int(params[1]),int(params[2]))
            print(str(result))
        elif params[0] == "s":
            assert len(params) == 3, "Number of params not correct."
            result = subtraction(int(params[1]),int(params[2]))
            print(str(result))
        elif params[0] == "m":
            assert len(params) == 3, "Number of params not correct."
            result = multiplication(int(params[1]),int(params[2]))
            print(str(result))
        elif params[0] == "d":
            assert len(params) == 3, "Number of params not correct."
            assert params[2] != 0, ValueError("Zero division.")
            result = division(int(params[1]),int(params[2]))
            print(str(result))
        elif params[0] == "f":
            assert len(params) == 2, "Number of params not correct."
            assert int(params[1] >= 0), ValueError("Out of factorial range.")
            result = factorial(int(params[1]))
            print(str(result))
        elif params[0] == "p":
            assert len(params) == 3, "Number of params not correct."
            assert int(params[2]) >= 0, ValueError("Out of scope")
            assert int(params[1]) !=0 and int(params[2]) != 0, ValueError("Out of scope") 
            result = power(int(params[1]),int(params[2]))
            print(str(result))
        elif params[0] == "l":
            assert len(params) == 3, "Number of params not correct."
            assert len(params[1]) >= 0, ValueError("Out of scope")
            assert len(params[2]) > 0, ValueError("Out of scope")
            result = log(int(params[1]),int(params[2]))
            print(str(result))
    except AssertionError as error:
        print("Oops something happened with the assertion! The error is:", error)
    except ValueError as error:
        print(f"There is an error with at least one value written and the error is {error}")
    except Exception as error:
        print("Oops something happened! The error is:", error)
    except KeyboardInterrupt:
        print("Keyboard interrupt is detected, terminating...")
        break
