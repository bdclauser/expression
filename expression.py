import random as rnd
from tkinter import Tk
from tkinter.ttk import Button, Label

exps = ["We were meant to be!", "Nothing can separate the two of us.", "You make live worth living.",
        "Love is never for the weak.", "You make the butterflies in my stomach flutter.",
        "They say you only fall in love one, but that can't be true...\nEvery time I look at you, I fall in love all over again.",
        "I love yo to the moon and back.",
        "With you,\nforever\nwon't be\ntoo long.", "I never know how joyous life could be,\nuntil I saw your face.",
        "Loving you is like everything I've ever lost come back to me.", "When I see you, I think \"Good Job, GOD!",
        ]

root = Tk()
root.title("Because of You")

lb = Label(root, text="HEY")
lb.pack(pady=30)


def express():
    lb["text"] = rnd.choice(exps)

    Button(root, text="Express Lobe", command=express().pack(pady=20))
    root.geometry("250x150+300+300")

    root.mainloop()
