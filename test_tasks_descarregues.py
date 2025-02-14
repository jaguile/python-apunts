import asyncio
import random
import time

# programa en Python que simuli un sistema de descàrrega de fitxers utilitzant asyncio, coroutines i asyncio.gather().

"""
1 Simular la descàrrega de fitxers amb una funció asíncrona.
2️ Fer que cada descàrrega trigui un temps aleatori (usant asyncio.sleep()).
3️ Gestionar múltiples descàrregues en paral·lel amb asyncio.gather().
4️ Mostrar missatges d'inici i finalització de cada descàrrega.
5️ Mostrar el temps total de descàrrega al final.
"""

MIN_SECONDS=1
MAX_SECONDS=8

async def descarrega(nom_fitxer, temps):
    print(f"Iniciant descarrega de {nom_fitxer} -- {time.strftime("%H:%M:%S", time.localtime())}")
    await asyncio.sleep(temps)
    print(f"Descàrrega finalitzada {nom_fitxer} -- {time.strftime("%H:%M:%S", time.localtime())}")
    return f"{nom_fitxer} descarregat"
    

async def main():
    fitxers = ["Arxiu1.jpeg", "Arxiu2.pdf", "Arxiu3.gift", "Arxiu4.zip"]

    # _ és una variable que s'acostuma a fer servir en loops quan no interessa el seu valor, és simplement per iterar.
    #
    temps_descarrega = [random.randrange(MIN_SECONDS, MAX_SECONDS) for _ in fitxers]

    # zip és per agrupar objectes iterables
    #
    tasques = [descarrega(nom, temps) for nom, temps in zip(fitxers, temps_descarrega)]

    temps_ini = time.time()

    # *tasques desempaqueta la llista tasques, ja que la funció gather espera paràmetres per separat.
    #
    resultats = await asyncio.gather(*tasques)

    temps_final = time.time()

    print (f"Temps total de descàrrega: {round(temps_final - temps_ini, 2)}")

    print(resultats)

# asyncio.run s'ha de fer servir per executat l'entrada principal del l'aplicació:
# The asyncio.run() function to run the top-level entry point “main()” function (see the above example.)
#
asyncio.run(main())
