C4_freq = float(261.63)
D4_freq = float(293.66)
E4_freq = float(329.63)
F4_freq = float(349.23)
G4_freq = float(392.00)
A4_freq = float(440.00)
B4_freq = float(493.88)

name_of_note = (input("Type the name of the note!: "))

note = name_of_note[0]
octave = int(name_of_note[1])

if note == "C":
    freq = C4_freq
elif note == "D":
    freq = D4_freq
elif note == "E":
    freq = E4_freq
elif note == "F":
    freq = F4_freq
elif note == "G":
    freq = G4_freq
elif note == "A":
    freq = A4_freq
elif note == "B":
    freq = B4_freq

freq = freq / 2 ** (4 - octave)

print("The frequency of", name_of_note, "is", freq)

