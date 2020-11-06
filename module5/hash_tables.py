voted = {}


def check_vote(name):
    if voted.get(name):
        return "Kick them out!"
    else:
        voted[name] = True
        return "Len them vote!"


print(check_vote("Ivan"))
print(check_vote("Ivan"))

d = {}
print(True if d.get("lo") else False)