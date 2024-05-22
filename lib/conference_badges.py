def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
    return ["Hello, my name is " + name + "." for name in names]

def assign_rooms(names):
    return ["Hello, " + name + "! You'll be assigned to room " + str(index+1) + "!" for index, name in enumerate(names)]

def printer(names):
    for message in batch_badge_creator(names):
        print(message)
    for message in assign_rooms(names):
        print(message)
