import subprocess
import sys

def test(student_sol):
    inputs = [
        ["12345", "1000", "Barış Bilen", "3.5", "500", "300", "exit"],
        ["54321", "2000", "Uğur Önal", "2.5", "600", "400", "exit"],
        ["98072", "234009", "Erhan Biçer", "1.27", "500", "1026.59", "exit"],

        ["Account123", "1000", "Yaren Yılmaz", "12.5", "100", "0", "exit"],
        ["56781", "250", "Yaren Yılmaz", "0.33", "300", "5", "exit"],
        ["456311", "98712.4567", "Yaren Yılmaz", "23.34", "-9888", "1000", "exit"]
    ]
    expected_outputs = [
        f"Account Number: 12345\nAccount Holder: Barış Bilen\nBalance: ${'{:.2f}'.format(1000)}\nInterest Rate: 3.5%\nWithdrew ${'{:.2f}'.format(500)} from account 12345.\nAfter withdraw: {'{:.2f}'.format(500)}\nDeposited ${'{:.2f}'.format(300)} into account 12345.\nAfter deposit: {'{:.2f}'.format(800)}\nInterest of ${'{:.2f}'.format(28)} added to account 12345.\nAfter interest rate: {'{:.2f}'.format(828)}",
        f"Account Number: 54321\nAccount Holder: Uğur Önal\nBalance: ${'{:.2f}'.format(2000)}\nInterest Rate: 2.5%\nWithdrew ${'{:.2f}'.format(600)} from account 54321.\nAfter withdraw: {'{:.2f}'.format(1400)}\nDeposited ${'{:.2f}'.format(400)} into account 54321.\nAfter deposit: {'{:.2f}'.format(1800)}\nInterest of ${'{:.2f}'.format(45)} added to account 54321.\nAfter interest rate: {'{:.2f}'.format(1845)}",
        f"Account Number: 98072\nAccount Holder: Erhan Biçer\nBalance: ${'{:.2f}'.format(234009)}\nInterest Rate: 1.27%\nWithdrew ${'{:.2f}'.format(500)} from account 98072.\nAfter withdraw: {'{:.2f}'.format(233509)}\nDeposited ${'{:.2f}'.format(1026.59)} into account 98072.\nAfter deposit: {'{:.2f}'.format(234535.59)}\nInterest of ${'{:.2f}'.format(2978.60)} added to account 98072.\nAfter interest rate: {'{:.2f}'.format(237514.19)}",

        f"Account Number: Account123\nAccount Holder: Yaren Yılmaz\nBalance: ${'{:.2f}'.format(1000)}\nInterest Rate: 12.5%\nWithdrew ${'{:.2f}'.format(100)} from account Account123.\nAfter withdraw: {'{:.2f}'.format(900)}\nInvalid deposit amount.\nAfter deposit: {'{:.2f}'.format(900)}\nInterest of ${'{:.2f}'.format(112.50)} added to account Account123.\nAfter interest rate: {'{:.2f}'.format(1012.50)}",
        f"Account Number: 56781\nAccount Holder: Yaren Yılmaz\nBalance: ${'{:.2f}'.format(250)}\nInterest Rate: 0.33%\nInsufficient funds.\nAfter withdraw: {'{:.2f}'.format(250)}\nDeposited ${'{:.2f}'.format(5)} into account 56781.\nAfter deposit: {'{:.2f}'.format(255)}\nInterest of ${'{:.2f}'.format(0.84)} added to account 56781.\nAfter interest rate: {'{:.2f}'.format(255.84)}",
        f"Account Number: 456311\nAccount Holder: Yaren Yılmaz\nBalance: ${'{:.2f}'.format(98712.46)}\nInterest Rate: 23.34%\nInvalid withdrawal amount.\nAfter withdraw: {'{:.2f}'.format(98712.46)}\nDeposited ${'{:.2f}'.format(1000)} into account 456311.\nAfter deposit: {'{:.2f}'.format(99712.46)}\nInterest of ${'{:.2f}'.format(23272.89)} added to account 456311.\nAfter interest rate: {'{:.2f}'.format(122985.34)}"
    ]
    expected_points = [30, 30, 25, 5, 5, 5]
    total_points = 0

    for i in range(len(inputs)):
        process = subprocess.Popen(['python', student_sol], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        input_bytes = '\n'.join(inputs[i]).encode()  # Encode the input string to bytes
        stdout, stderr = process.communicate(input_bytes)

        actual_output = stdout.decode().strip()  # Decode the output bytes to string
        expected_output = expected_outputs[i]
        try:
            assert actual_output == expected_output
        except AssertionError:
            print(f"[0/{expected_points[i]}] Expected: {expected_output}, but got: {actual_output}")
        else:
            print(f"[{expected_points[i]}/{expected_points[i]}] Expected: {expected_output}, got: {actual_output}")
            total_points += expected_points[i]

    print(f"Total: {total_points}")

if __name__ == "__main__":
    student_sol = sys.argv[1]

    if (student_sol.split('.')[-1] == "py"):
        test(student_sol)
    else:
        raise ValueError(f"{student_sol} is not a python file")
