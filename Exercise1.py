#define the initial no.
no = 1
# to print all no's divisible by 3
while no <= 1000:
    if no % 3 == 0:
        print(str(no) + "is divisible by 3")
    no = no+1
else: print(str(no) + "No. is out of limit")



