# python-apunts
Apunts Python

## Tuples
Python, a més de treballar amb llistes i diccionaris, pot treballar amb tuples de variables. Per treballar amb tuples, pots representar una tupla amb valors o variables separats per comes o poden anar també entre parèntesis.

## Gestió d'errors (Errors and exceptions)
[Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

### Exceptions

Són errors que es detecten en l'execució del programa.

#### Variables associades a excepcions

Podem associar una variable a una excepció, la qual després es pot imprimir mostrant els possibles arguments de l'excepció associada:

```python
>>>try:

    raise Exception('spam', 'eggs')

except Exception as inst:

    print(type(inst))    # the exception type

    print(inst.args)     # arguments stored in .args

    print(inst)          # __str__ allows args to be printed directly,

                         # but may be overridden in exception subclasses

    x, y = inst.args     # unpack args

    print('x =', x)

    print('y =', y)
```

Sortida:

```python
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

#### BaseException i Exception classes

La classe base de totes les excepcions és **BaseException**, la qual controla tant les excepcions que es poden manegar com les que no.

La classe **Excepcion** és la classe base per totes les excepcions manegables.

A l'hora de manegar una excepció, podem fer servir directament la classe **Exception**. Aquesta classe ens serveix com a comodí de qualsevol altre tipus d'excepció manegable. Tot i així és preferible especificar al màxim amb el tipus d'excepció. 

El més comú a l'hora de fer ús de la classe **Exception** és fer-la servir per llençar l'excepció que no és esperada:

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

A tenir en compte que la clàusula `except`, quan s'executa, ignora després els `except` restants. O sigui, no s'executen en cascada ni fa falta afegir una clàusula `break` ni similar.

**Important. Bona pràctica**: Amb les clàusules `try`...`except` hi podem afegir una tercera clàusula `else`, que ha de seguir la resta de clàusules. És bastant útil per afegir codi que ha de ser executat si la clàusula `try` va bé i no llença una excepció. 

#### Llençar excepcions manualmant amb `raise`

La instrucció `raise` en Python serveix per generar (llançar) una excepció manualment. Això ens permet controlar errors i interrompre l'execució quan es detecta una situació incorrecta:

```python
raise ValueError("Aquest és un error personalitzat!")
```

Sortida:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Aquest és un error personalitzat!
```

Un altre exemple. Fem missatge personalitzat d'una excepció:

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No es pot dividir per zero!")
    return a / b

print(dividir(10, 2))  # Funciona
print(dividir(5, 0))   # Genera ZeroDivisionError
```

Sortida: 

```python
5.0
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
ZeroDivisionError: No es pot dividir per zero!
```
Capturem una excepció i la tornem a llençar:

```python
try:
    raise ValueError("Error detectat!")
except ValueError as e:
    print(f"Excepció atrapada: {e}")
    raise  # Torna a llençar l'error
```

Sortida:

```python
Excepció atrapada: Error detectat!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: Error detectat!
```

Crear excepcions personalitzades:

```python
class ErrorPersonalitzat(Exception):
    pass

def validar(edat):
    if edat < 18:
        raise ErrorPersonalitzat("Edat no permesa!")

try:
    validar(16)
except ErrorPersonalitzat as e:
    print(f"Error: {e}")
```

Sortida:

```python
Error: Edat no permesa!
```

#### Excepcions encadenades

**Clàusula from** - Si volem indicar que una excepció prové d'una altra:

```python
def func():

    raise ConnectionError


try:

    func()

except ConnectionError as exc:

    raise RuntimeError('Failed to open database') from exc


Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
```

**Clàusula None** - Per deshabilitar les excepcions en cadena:

```python
try:

    open('database.sqlite')

except OSError:

    raise RuntimeError from None


Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError from None
RuntimeError
```

#### Clàusula `finally`

Per executar codi al final del bloc `try`... `except` que s'ha d'executar sí o sí.

## Iterables i iteradors

**Un iterable** és qualsevol objecte en Python que pot ser recurregut i que retorna elements un a un. Exemple: una llista, una tupla, un string, un diccionari, etc.

**Un iterator** és un objecte especial a Python que permet recòrrer un **iterable** amb `next()`

## Python List Comprehension
[Tutorial amb exemples](https://python.land/deep-dives/list-comprehension)

## Funcions amb nombre de valors indeterminats

Fem servir `*args` o `*kwargs` i es poden combinar.

### Arguments posicionals il·limitats:

Hem de fer servir `*args`. Exemple:

```python
def suma(*args):
    return sum(args)

print(suma(1, 2, 3))      # 6
print(suma(10, 20, 30, 40))  # 100
```

### Arguments per nom il·limitats

Hem de fer servir `**kwargs`. Exemple:

```python
def mostrar_info(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_info(nom="Anna", edat=25, ciutat="Barcelona")
```

## Asyncio - Entrada i sortida assíncrona
[Asyncio a Pyhon3](https://docs.python.org/3/library/asyncio.html)

Es fa servir la sintaxi **async / await**

## Tasks and coroutines
[Tasks and coroutines in Python3](https://docs.python.org/3/library/asyncio-task.html#coroutine)

API d'alta nivell del mòdul asyncio.

## varis

### Paraula clau `pass`

En Python, pass és una instrucció buida que no fa res. S’utilitza quan la sintaxi requereix una línia de codi però no volem executar res en aquell moment.

```python
def funcio_pendent():
    pass  # Evitem error de sintaxi

print("El programa continua...")
```
