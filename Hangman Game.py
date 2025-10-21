import random
words=["stone","camel","eagle","rabbit","lion"]
word=random.choice(words);
guessed=""
attempts=6
while (attempts>0):
    display=""
    for c in word:
        if c in guessed:
            display+=c
        else:
            display+="_"
    print(display)
    if(display==word):
        print("you won!")
        break
    guess=input("guess letter:")
    if guess in word:
        guessed+=guess
    else:
        attempts-=1
        print("wrong-attempts left:",attempts)
else:
    print("you lost word was:",word)