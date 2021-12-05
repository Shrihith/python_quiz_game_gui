import tkinter
from tkinter import *
from tkinter import font
import random

questions = [
    "Total keywords in python ?",
    "which of the following function takes A console in python ?",
    "Output of 2**3  ?",
    "Which of the following is must to execute a python code ?",
    "Output of np.arrange(1,5) ?",
    "The append Method adds value to the list at the ?",
    "Keyword use to declare function ?",
    "Output of 2*21  ?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
]

answer_choice = [
    ['33','31','30','32'],
    ['get()','input()','gets()','scan()'],
    ['6','8','9','12'],
    ['TURBO c','Py Interpreter','Notepad','IDE'],
    ['[1,2,3,4]','[0,1,2,3,4', '[1,2,3,4,5]', '[2,4,5,1,3'],
    ['custom location','end','center','begining'],
    ['definr','dif','def','null'],
    ['28','24','42','32'],
    ['function','void','fun','def'],
    ['all','var','let','global'],
 ]

answers = [0,1,1,1,0,3,3,2,3,3]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ('Console', 20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are Excellent!!")
    elif(score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You can be better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Better luck next time !!")

def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)



ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text = questions[indexes[ques]])
        r1['text'] = answer_choice[indexes[ques]][0]
        r2['text'] = answer_choice[indexes[ques]][1]
        r3['text'] = answer_choice[indexes[ques]][2]
        r4['text'] = answer_choice[indexes[ques]][3]
        ques += 1 
    else:
        print(indexes)
        print(user_answer)
        calc()
        


def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ('Consolos', 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = '#ffffff',
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    


    r1  = Radiobutton(
        root,
        text = answer_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = '#ffffff',
    )
    r1.pack(pady=5)

    r2  = Radiobutton(
        root,
        text = answer_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = '#ffffff',
    )
    r2.pack(pady=5)

    r3  = Radiobutton(
        root,
        text = answer_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = '#ffffff',
    )
    r3.pack(pady=5)

    r4  = Radiobutton(
        root,
        text = answer_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = '#ffffff',
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title('Pyquiz')
root.geometry("900x800")
root.config(background="#ffffff")
root.resizable(0,0)

img1 = PhotoImage(file="icon.png")


labelimage = Label(
    root,
    image = img1,
    background = '#ffffff',
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = 'Pyquiz',
    font = ("Comic sans MS",42,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="start.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    background = "#ffffff",
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick start once you ready",
    font = ("Consolas",16,"bold"),
    background="#ffffff",
    justify= "center",
)
lblInstruction.pack(pady=(10,40))

lblRules = Label(
    root,
    text = "This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background= "#000000",
    foreground= "#FACA2F",
)
lblRules.pack()




root.mainloop()