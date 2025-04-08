# Un generator és una funció que va retornant valors a mesura 
# que es va executant amb la clàusula yield. En realitat, retorna 
# un iterator amb aquests valors.
#

"""
def comptador(límit):
    actual = 0
    while actual < límit:
        yield actual
        actual += 1

for x in comptador(3):
    print(x)
"""

# Generador
def generador():
	for i in range(10):
		yield i

# creem un iterator generator
gen = generador()
print (gen)

# step the generator
result = next(gen)
print(result)

# recorro iterator
results = [print(item) for item in generador()]