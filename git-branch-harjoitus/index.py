# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

print("welcome!")
logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"lukujen {x} ja {y} summa on {summa(x, y)}") #muutos bugikorjauksessa
print(f"lukujen {x} ja {y} erotus on {erotus(x, y)}") #muutos bugikorjauksessa
print(f"lukujen {x} ja {y} tulo on {tulo(x, y)}") #muutos bugikorjauksessa

logger("lopetetaan")
print("goodbye!")
