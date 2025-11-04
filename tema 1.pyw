print(”Cel puțin 33 de oameni uciși de trăsnete în India. Majoritatea victimelor au fost lovite în timp ce lucrau pe câmp ”)
stire=”Cel puțin 33 de oameni uciși de trăsnete în India. Majoritatea victimelor au fost lovite în timp ce lucrau pe câmp”
import string 
parte= len(stire)//2
prima_parte=stire{[:parte].strip().upper()
a_doua_parte=stire[parte:].capitalize()[::-1]
a_doua_parte:”Cel puțin 33 de oameni uciși de trăsnete în India. Majorita”
fara_punctuatie=``.join(ch for ch in a_doua_parte if ch not in string.punctuation)

a_doua_parte=fara_punctuatie

print(a_doua_parte)

print(”Prima parte:”,prima_parte)
print(A doua parte:”,a_doua_parte)
rezultat=prima_parte+a_doua_parte 
print(rezultat)








