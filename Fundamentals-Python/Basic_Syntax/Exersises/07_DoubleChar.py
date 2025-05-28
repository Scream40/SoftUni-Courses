string = input()

while string != 'End':

    double_string = ''
    if string != "SoftUni":
        for char in string:
            double_string += char * 2

        print(double_string)
    string = input()