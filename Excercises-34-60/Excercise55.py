frequency = float(input("Enter the frequency of radiation: "))

if frequency < 3e9:
    print("That frequency enters the range of Radio waves!")
elif frequency >= 3e9 and frequency < 3e12:
    print("That frequency enters the range of Microwaves!")
elif frequency >= 3e12 and frequency < 4.3e14:
    print("That frequency enters the range of Infrared light!")
elif frequency >= 4.3e14 and frequency < 7.5e14:
    print("That frequency enters the range of Visible light!")
elif frequency >= 7.5e14 and frequency < 3e17:
    print("That frequency enters the range of Ultraviolet light!")
elif frequency >= 3e17 and frequency < 3e19:
    print("That frequency enters the range of X-rays!")
elif frequency >= 3e19:
    print("That frequency enters the range of Gamma rays!")
else:
    print("Your input is invalid!")