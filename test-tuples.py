"""
Programa que permeti gestionar un registre d'estudiants amb les seves notes mitjançant tuples. L'objectiu és implementar les funcionalitats següents:

    Afegir estudiants al sistema: Cada estudiant ha de tenir:
        Nom
        Edat
        Tres notes
    Calcular la nota mitjana de cada estudiant.
    Mostrar la llista d'estudiants amb les seves dades en format llegible.

    Controlar que no es puguin ficar més o menys arguments (try / catch)
"""

def menu_afegir(llista_alumnat):
    continuar = 1
    while(continuar):
        valors = input ("Introdueix nom alumnat, edat, 3 notes separats per espais: ").split()
        afegir (llista_alumnat, valors)
        continuar = print_alumnat(llista_alumnat)

def afegir(alumnat, dades_alumnat):
    alumnat.append((dades_alumnat[0], dades_alumnat[1], 
                    (dades_alumnat[2], dades_alumnat[3], dades_alumnat[4])))

def print_alumnat(alumnat):
    mitjana_ = 0
    for nom, edat, notes in alumnat:
        # mitjana = mitjana(notes)
        mitjana_ = mitjana(notes)
        print(f"Nom - {nom}, edat - {edat}, notes - {notes}, mitjana - {mitjana_:.2f}")
    continuar = int(input("Vols afegir més? [1] - Sí; [0] - No "))
    return continuar

def mitjana(notes):
    mitjana_ = 0
    for nota in notes:
        nota_ = int(nota)
        mitjana_ += nota_
    
    return mitjana_/len(notes)

# Aquesta línea és útil per a senyalar que el codi de sota s'executi si el programa 
# es crida com el programa principal només
#
if __name__ == "__main__":
    llista_alumnat = []
    menu_afegir(llista_alumnat)