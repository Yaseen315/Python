print "Hello"

name = raw_input("What is your name?:")
name = name.upper()

animal = raw_input("what is your favourite animal?:")
animal= animal.upper()

superhero = raw_input("who is your favourite superhero:")
superhero = superhero.upper()

villian = raw_input("who is your favourite villian:")
villian = villian.upper()


def answers(name,villian,animal,superhero):
    print "%s was walking one day and saw a %s stuck in a tree. %s was so confused and didnt know what to do."%(name, animal, name) 
    print "Suddenly %s came out of nowhere! %s was so exited to see %s. Oh no, %s's life long villian, %s appeared."%(superhero, name, superhero, superhero, villian)
    print "%s was conflicted because %s also loved %s. But the %s needs saving."%(name, name, villian, animal)
answers(name,villian,animal,superhero)
asking = True 
def final():
    while asking:   
        lifeordeath = raw_input("life or death?:")
        if lifeordeath == "life":
            print "%s killed %s with %s's help and saved the %s."%(superhero, villian, name, animal)
            break
        elif lifeordeath == "death": 
            print "%s couldn't help but assist %s killing %s. %s died, and so did %s"%(name, villian, superhero, superhero, animal)
            break
        elif lifeordeath != "life" or lifeordeath != "death":
            print "life or death ONLY"
            final
final()
        



