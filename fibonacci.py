number = int(raw_input("How may numbers in Fibonacci to print? "))
a = 0
b = 1
count = 0
while count < number:
    old_a = a
    old_b = b
    a = old_b
    b = old_a + old_b
    print(old_a),
    count = count + 1
