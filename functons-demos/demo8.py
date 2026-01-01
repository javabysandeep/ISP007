def process(number, string='default string value'):
    print(string * number)


# def process1(string='default string value', number):
#     print(string * number)


process(string="abc", number=10)
process(number=2)  # default string valuede fault string value
process(2)  # default string value default string value

