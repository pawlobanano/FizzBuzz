def i_divisible_by(i, num):
    if (i % num == 0):
        return True
    return False


def output_printer(str):
    output = ""
    return output + str


choices = {
    3: output_printer("Fizz"),
    5: output_printer("Buzz")
}

for i in range(1, 101):
    output = ""
    if (i_divisible_by(i, 3)):
        output += choices.get(3)
    if (i_divisible_by(i, 5)):
        output += choices.get(5)
    if (output == ""):
        output = output_printer(str(i))
    print(output)
