
db = [
    ['aaaa', '1111'],
    ['bbbb', '2222'],
    ['cccc', '3333'],
    ['dddd', '4444'],
    ['eeee', '5555'],
    ['ffff', '6666'],
]

user = raw_input("Name: ")
pin = raw_input("Pind: ")

if [user, pin] in db:
    print "Access granted!"
else:
    print "ERROR!"
