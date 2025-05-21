import subprocess
import sys

def test(student_sol):
    inputs = [""]
    expected_output = "Sender: GB29-NWBK-6016-1331-9268-19 Receiver: TR21-0006-1005-1978-6457-8413-26\nSender: SW49-NWBK-6016-1331-9268-19 Receiver: TR21-0006-1005-1978-6457-8413-26\nSender: TR50-0006-7010-0000-0000-07AB-C9 Receiver: GB55-LOYD-3012-3456-7890-12\nSender: TR65-0006-7010-0000-0000-07AB-C9 Receiver: TR55-LOYD-3012-3456-7890-12\nSender: TR72-6372-7372-0828-1728-1782-11 Receiver: US18-7272-9710-8619-1826-6384-82"
    expected_points = [20,20,20,20,20]
    
    total_points = 0

    process = subprocess.Popen(['python3', 
                                student_sol, 
                                "TR72-6372-7372-0828-1728-1782-11:US18-7272-9710-8619-1826-6384-82,GB29-NWBK-6016-1331-9268-19:TR21-0006-1005-1978-6457-8413-26,TR50-0006-7010-0000-0000-07AB-C9:GB55-LOYD-3012-3456-7890-12,SW49-NWBK-6016-1331-9268-19:TR21-0006-1005-1978-6457-8413-26,NL-0006-7010-0000-0000-07AB-C9:GB55-LOYD-3012-3456-7890-12,TR65-0006-7010-0000-0000-07AB-C9:TR55-LOYD-3012-3456-7890-12"], 
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
    input_bytes = '\n'.join(inputs).encode()  # Encode the input string to bytes
    stdout, stderr = process.communicate(input_bytes)

    actual_output = stdout.decode().strip()  # Decode the output bytes to string
    print("Actual output:", actual_output)
    # split actual output using new lines
    actual_output = actual_output.split("\n")
    expected_outputs = expected_output.split("\n")
    for i in range(len(expected_outputs)):
        try:
            assert actual_output[i] == expected_outputs[i]
        except AssertionError:
            print("*********************************")
            print(f"[0/{expected_points[i]}]\n**EXPECTED**\n{expected_outputs[i]}\n**RECEIVED**\n{actual_output[i]}")
            print("*********************************")
        except IndexError:
            print("*********************************")
            print(f"[0/{expected_points[i]}]\n**EXPECTED**\n{expected_outputs[i]}\n**RECEIVED**\n")
            print("*********************************")
        else:
            print("*********************************")
            print(f"[{expected_points[i]}/{expected_points[i]}]\n**EXPECTED**\n{expected_outputs[i]},\n**RECEIVED**\n{actual_output[i]}")
            print("*********************************")
            total_points += expected_points[i]

    print(f"Total: {total_points}")

if __name__ == "__main__":
    student_sol = sys.argv[1]

    if (student_sol.split('.')[-1] == "py"):
        test(student_sol)
    else:
        raise ValueError(f"{student_sol} is not a python file")
