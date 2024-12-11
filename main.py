import bevezetes
import sorozat
from autom import Auto

"""bevezetes.automarka()
sorozat.kiir()
lista = sorozat.lotto()
sorozat.file_kiir(sorozat.egyjegyuek_szama(lista))"""

Auto.beolvas("auto.txt") 
print(f"III/Flotta:")
print(f"         Autók száma: {Auto.flotta()}.")