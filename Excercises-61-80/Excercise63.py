temperature = [0,10,20,30,40,50,60,70,80,90,100]
i = 0


while i < len(temperature):
   i = i + 1 
   celcius = temperature[i]
   farenheit = 1.8 * celcius + 32 
   print("Celcius: ",celcius,"| Farenheit: ",farenheit) 
