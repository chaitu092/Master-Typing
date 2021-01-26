from tkinter import *
import random
import ttkthemes as tt
from tkinter import ttk
import time
import threading

timelimit = 60
remainingtime = timelimit
elapsedtime = 0
elapsedtimeinminutes = 0
totalwords = 0
wrongwords = 0
wpm = 0
accurcay = 0


def start_timer():
    global elapsedtime
    textarea.config(state=NORMAL)
    textarea.focus()

    start_button.config(state=DISABLED)
    # range (1,10)
    for t in range(1, timelimit + 1):
        elapsedtime = t
        elapsed_timer_label.config(text=elapsedtime)

        updateRemainingTime = remainingtime - elapsedtime

        remaning_timer_label.config(text=updateRemainingTime)

        time.sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    reset_button.config(state=NORMAL)


def count():
    global elapsedtime, wrongwords, elapsedtimeinminutes
    para_words = label_paragraph['text'].split()

    while elapsedtime != timelimit:
        entered_paragraph = textarea.get(1.0, END).split()
        totalwords = len(entered_paragraph)

    for pair in list(zip(para_words, entered_paragraph)):
        if pair[0] != pair[1]:
            wrongwords += 1

    elapsedtimeinminutes = elapsedtime / 60  # 1.0 min

    wpm = (totalwords - wrongwords) / elapsedtimeinminutes
    wpm_timer_label.config(text=wpm)

    gross_wpm = totalwords / elapsedtimeinminutes

    accurcay = wpm / gross_wpm * 100

    accurcay = round(accurcay)

    accuracypercent_label.config(text=str(accurcay) + '%')

    totalwords_count_label.config(text=totalwords)

    wrongwords_count_label.config(text=wrongwords)


def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


def reset():
    global remainingtime, elapsedtime
    reset_button.config(state=DISABLED)
    start_button.config(state=NORMAL)

    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

    remainingtime = timelimit
    elapsedtime = 0
    elapsedtimeinminutes = 0

    elapsed_timer_label.config(text='0')
    remaning_timer_label.config(text='0')
    wpm_timer_label.config(text='0')
    accuracypercent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')


root = tt.ThemedTk()

root.get_themes()

root.set_theme('radiance')
# to remove titlebar
root.overrideredirect(True)

root.geometry('940x735+350+0')
# root.title('Master Typing created by Sai Chaitanya')
# root.resizable(0,0)

mainframe = Frame(root, bg='snow', bd=4)
mainframe.grid()

titleFrame = Frame(mainframe, bg='red3')
titleFrame.grid(row=0, column=0)

titleLabel = Label(titleFrame, text='Master Typing', font=('algerian', '28', 'bold'), bg='goldenrod3', fg='white',
                   width=38, bd=10, relief=FLAT)
titleLabel.grid(row=0, column=0, pady=5)

frame_test = Frame(mainframe, bg='snow', relief='flat')
frame_test.grid(row=1, column=0)

selected_paragraph = [
    'The Ramayana is a story of Lord Rama written by the SageValmiki. Lord Rama, the prince of Ayodhya, in order to help his father Dasharatha went to exile for fourteen years. His wife, Sita and his younger brother Lakshmana also went with him. He went through many difficulties in the forest. One day Ravana, the king of Lanka carried away Sita with him. Then, Lord Rama, with the help of Hanumana, defeated and killed Ravana; Sita, Rama and Lakshmana returned to Ayod hya after their exile.',
    'The Mahabharata is a story about a great battle between the Kauravas and the Pandavas. The battle was fought in Kurukshetra near Delhi. Many kings and princes took part in the battle. The Pandavas defeated the Kauravas. The Bhagvad Gita is a holy book of the Hindus. It is a part of the Mahabharata. Then, Lord Rama, with the help of It is a book of collection of teachings of Lord Krishna to Arjuna in the battlefield. It is the longest epic in the world.',
    'India is an agricultural country. Most of the people live in villages and are farmers. They grow cereals, pulses, vegetables and fruits. The farmers lead a tough life. They get up early in the morning and go to the fields. They stay and work on the farm late till evening. The farmers usually live in kuchcha houses. Though, they work hard they remain poor. Farmers eat simple food; wear simple clothes and rear animals like cows, buffaloes and oxen. Without them there would be no cereals for us to eat. They play an important role in the growth and economy of a country.',
    'The doctor is a person who looks after the sick people and prescribes medicines so that the patient recovers fast. In order to become a doctor, a person has to study medicine. Doctors lead a hard life. Their life is very busy. They get up early in the morning and go to the hospital. They work without taking a break. They always remain polite so that patients feel comfortable with them. Since doctors work so hard we must realise their value.',
    'The sun is a huge ball of gases. It has a diameter of 1,392,000 km. It is so huge that it can hold millions of planets inside it. The Sun is mainly made up of hydrogen and helium gas. The surface of the Sun is known as the photosphere. The photosphere is surrounded by a thin layer of gas known as the chromospheres. Without the Sun, there would be no life on Earth. There would be no plants, no animals and no human beings. As, all the living things on Earth get their energy from the Sun for their survival.',
    'The Moon is a barren, rocky world without air and water. It has dark lava plain on its surface. The Moon is filled wit craters. It has no light of its own. It gets its light from the Sun. The Moo keeps changing its shape as it moves round the Earth. It spins on its axis in 27.3 days stars were named after the Edwin Aldrin were the first ones to set their foot on the Moon on 21 July 1969 They reached the Moon in their space craft named Apollo II.',
    'The Solar System consists of the Sun Moon and Planets. It also consists of comets, meteoroids and asteroids. The Sun is the largest member of the Solar System. In order of distance from the Sun, the planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto; the dwarf planet. The Sun is at the centre of the Solar System and the planets, asteroids, comets and meteoroids revolve around it.',
    'An elephant is the biggest living animal on land. It is quite huge in size. It is usually black or grey in colour. Elephants have four legs, a long trunk and two white tusks near their trunk. Apart from this, they have two big ears and a short tail. Elephants are vegetarian. They eat all kinds of plants especially bananas. They are quite social, intelligent and useful animals. They are used to carry logs of wood from one place to another. They are good swimmers.'
    ]

random.shuffle(selected_paragraph)

label_paragraph = Label(frame_test, text=selected_paragraph[0], font=('arial', 14, 'bold'), wraplength=930,
                        justify=LEFT)
label_paragraph.grid(row=0, column=0, pady=5)

text_frame = Frame(mainframe, bg='snow', relief='flat')
text_frame.grid(row=2, column=0)

textarea = Text(text_frame, font=('arial', '12', 'bold'), width=100, height=7, bd=4, wrap='word', relief=GROOVE,
                state=DISABLED)
textarea.grid(row=0, column=0, padx=5, pady=5)

frame_output = Frame(mainframe)
frame_output.grid(row=3, column=0)

frame_label = Label(frame_output)
frame_label.grid()

elapsed_time_label = Label(frame_label, text='   Elapsed Time', font=('Tahoma', 12, 'bold'), fg='red', bg='snow')
elapsed_time_label.grid(row=0, column=0, padx=5, pady=5)

elapsed_timer_label = Label(frame_label, text='0', font=('Tahoma', 12, 'bold'), fg='black', bg='snow')
elapsed_timer_label.grid(row=0, column=1, padx=5, pady=5)

remaning_time_label = Label(frame_label, text='Remaning Time', font=('Tahoma', 12, 'bold'), fg='red', bg='snow')
remaning_time_label.grid(row=0, column=2, padx=5, pady=5)

remaning_timer_label = Label(frame_label, text='60', font=('Tahoma', 12, 'bold'), fg='black', bg='snow')
remaning_timer_label.grid(row=0, column=3, padx=5, pady=5)

wpm_time_label = Label(frame_label, text='WPM', font=('Tahoma', 12, 'bold'), fg='red', bg='snow')
wpm_time_label.grid(row=0, column=4, padx=5, pady=5)

wpm_timer_label = Label(frame_label, text='0', font=('Tahoma', 12, 'bold'), fg='black', bg='snow')
wpm_timer_label.grid(row=0, column=5, padx=5, pady=5)

accuracy_label = Label(frame_label, text='Accuracy', font=('Tahoma', 12, 'bold'), fg='red', bg='snow')
accuracy_label.grid(row=0, column=6, padx=5, pady=5)

accuracypercent_label = Label(frame_label, text='0', font=('Tahoma', 12, 'bold'), fg='black', bg='snow')
accuracypercent_label.grid(row=0, column=7, padx=5, pady=5)

totalwords_label = Label(frame_label, text='Total Words', font=('Tahoma', 12, 'bold'), fg='red', bg='snow')
totalwords_label.grid(row=0, column=8, padx=5, pady=5)

totalwords_count_label = Label(frame_label, text='0', font=('Tahoma', 12, 'bold'), fg='black', bg='snow')
totalwords_count_label.grid(row=0, column=9, padx=5, pady=5)

wrongwords_label = Label(frame_label, text='Wrong Words', font=('Tahoma', 12, 'bold'), fg='red', bg='snow')
wrongwords_label.grid(row=0, column=10, padx=5, pady=5)

wrongwords_count_label = Label(frame_label, text='0', font=('Tahoma', 12, 'bold'), fg='black', bg='snow')
wrongwords_count_label.grid(row=0, column=11, padx=5, pady=5)

# buttons
frame_control = Frame(frame_output, bg='snow')
frame_control.grid(row=1)

start_button = ttk.Button(frame_control, text='Start', command=start)
start_button.grid(row=0, column=0, padx=10)

reset_button = ttk.Button(frame_control, text='Reset', state=DISABLED, command=reset)
reset_button.grid(row=0, column=1, padx=10)

exit_button = ttk.Button(frame_control, text='Exit', command=root.destroy)
exit_button.grid(row=0, column=2, padx=10)

# creating keyboard
keyboard_frame = Frame(mainframe, bg='snow')
keyboard_frame.grid(row=4)

frame_1to0 = Frame(keyboard_frame, bg='snow')
frame_1to0.grid(row=0, column=0)

label1 = Label(frame_1to0, text='1', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label1.grid(row=0, column=0, padx=5, pady=3)

label2 = Label(frame_1to0, text='2', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label2.grid(row=0, column=1, padx=5, pady=3)

label3 = Label(frame_1to0, text='3', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label3.grid(row=0, column=2, padx=5, pady=3)

label4 = Label(frame_1to0, text='4', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label4.grid(row=0, column=3, padx=5, pady=3)

label5 = Label(frame_1to0, text='5', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label5.grid(row=0, column=4, padx=5, pady=3)

label6 = Label(frame_1to0, text='6', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label6.grid(row=0, column=5, padx=5, pady=3)

label7 = Label(frame_1to0, text='7', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label7.grid(row=0, column=6, padx=5, pady=3)

label8 = Label(frame_1to0, text='8', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label8.grid(row=0, column=7, padx=5, pady=3)

label9 = Label(frame_1to0, text='9', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label9.grid(row=0, column=8, padx=5, pady=3)

label0 = Label(frame_1to0, text='0', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
label0.grid(row=0, column=9, padx=5, pady=3)

frame_qtop = Frame(keyboard_frame, bg='snow')
frame_qtop.grid(row=1, column=0)

labelQ = Label(frame_qtop, text='Q', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelQ.grid(row=0, column=0, padx=5, pady=3)

labelW = Label(frame_qtop, text='W', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelW.grid(row=0, column=1, padx=5, pady=3)

labelE = Label(frame_qtop, text='E', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelE.grid(row=0, column=2, padx=5, pady=3)

labelR = Label(frame_qtop, text='R', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelR.grid(row=0, column=3, padx=5, pady=3)

labelT = Label(frame_qtop, text='T', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelT.grid(row=0, column=4, padx=5, pady=3)

labelY = Label(frame_qtop, text='Y', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelY.grid(row=0, column=5, padx=5, pady=3)

labelU = Label(frame_qtop, text='U', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelU.grid(row=0, column=6, padx=5, pady=3)

labelI = Label(frame_qtop, text='I', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelI.grid(row=0, column=7, padx=5, pady=3)

labelO = Label(frame_qtop, text='O', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelO.grid(row=0, column=8, padx=5, pady=3)

labelP = Label(frame_qtop, text='P', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelP.grid(row=0, column=9, padx=5, pady=3)

frame_atol = Frame(keyboard_frame, bg='snow')
frame_atol.grid(row=2, column=0)

labelA = Label(frame_atol, text='A', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelA.grid(row=0, column=0, padx=5, pady=3)

labelS = Label(frame_atol, text='S', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelS.grid(row=0, column=1, padx=5, pady=3)

labelD = Label(frame_atol, text='D', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelD.grid(row=0, column=2, padx=5, pady=3)

labelF = Label(frame_atol, text='F', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelF.grid(row=0, column=3, padx=5, pady=3)

labelG = Label(frame_atol, text='G', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelG.grid(row=0, column=4, padx=5, pady=3)

labelH = Label(frame_atol, text='H', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelH.grid(row=0, column=5, padx=5, pady=3)

labelJ = Label(frame_atol, text='J', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelJ.grid(row=0, column=6, padx=5, pady=3)

labelK = Label(frame_atol, text='K', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelK.grid(row=0, column=7, padx=5, pady=3)

labelL = Label(frame_atol, text='L', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelL.grid(row=0, column=8, padx=5, pady=3)

frame_ztom = Frame(keyboard_frame, bg='snow')
frame_ztom.grid(row=3, column=0)

labelZ = Label(frame_ztom, text='Z', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelZ.grid(row=0, column=0, padx=5, pady=3)

labelX = Label(frame_ztom, text='X', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelX.grid(row=0, column=1, padx=5, pady=3)

labelC = Label(frame_ztom, text='C', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelC.grid(row=0, column=2, padx=5, pady=3)

labelV = Label(frame_ztom, text='V', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelV.grid(row=0, column=3, padx=5, pady=3)

labelB = Label(frame_ztom, text='B', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelB.grid(row=0, column=4, padx=5, pady=3)

labelN = Label(frame_ztom, text='N', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelN.grid(row=0, column=5, padx=5, pady=3)

labelM = Label(frame_ztom, text='M', fg='white', bg='black', bd=10, width=5, height=2, relief=GROOVE,
               font=('arial', 10, 'bold'))
labelM.grid(row=0, column=6, padx=5, pady=3)

spaceFrame = Frame(keyboard_frame, bg='snow')
spaceFrame.grid(row=4)

label_space = Label(spaceFrame, text='SPACE', fg='white', bg='black', bd=10, width=40, height=2, relief=GROOVE,
                    font=('arial', 10, 'bold'))
label_space.grid(row=0, column=6, padx=10, pady=3)


# functionality !!!!!!!!!!!!!!!!!

def changeBG(widget):
    bg = 'black'
    widget.configure(background='blue')
    widget.after(100, lambda color=bg: widget.configure(background=color))


label_numbers = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label0]
label_alphabets = [labelA, labelB, labelC, labelD, labelE, labelF, labelG, labelH, labelI, labelJ, labelK, labelL,
                   labelM, labelN,
                   labelO, labelP, labelQ, labelR, labelS, labelT, labelU, labelV, labelW, labelX, labelY, labelZ]
space_label = [label_space]

binding_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

binding_capital_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z']
binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't',
                           'u', 'v', 'w', 'x', 'y', 'z']

for number in range(len(binding_numbers)):
    root.bind(f'{binding_numbers[number]}', lambda event, label=label_numbers[number]: changeBG(label))

for capital_alphabet in range(len(binding_capital_alphabets)):
    root.bind(f'{binding_capital_alphabets[capital_alphabet]}',
              lambda event, label=label_alphabets[capital_alphabet]: changeBG(label))

for small_alphabet in range(len(binding_small_alphabets)):
    root.bind(f'{binding_small_alphabets[small_alphabet]}',
              lambda event, label=label_alphabets[small_alphabet]: changeBG(label))

root.bind('<space>', lambda event, label=space_label[0]: changeBG(label))

root.mainloop()
