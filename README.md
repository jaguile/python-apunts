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

Amb la funció `isinstance()` podem saber si un element és iterable o no.

**Un iterator** és un objecte especial a Python que permet recòrrer un **iterable** amb `next()`. Els iteradors fan referència a un element i tenen aquest mètode `next()` que permet fer referència al següent element.

La funció `iter()` cridada sobre un objecte iterable ens retorna un objecte oterador. Aquest objecte o variable fa referència a l'objecte iterable i ens permet accedir als seus elements amb la funció `next()`.

## Python List Comprehension
[Tutorial amb exemples](https://python.land/deep-dives/list-comprehension)

## Funcions amb nombre de valors indeterminats

Fem servir `*args` o `*kwargs` i es poden combinar.

## Generadors (generators)

Un generador és una funció que va retornant valors de mica en mica. Aquests valors són accessibles mitjançant un iterator. Una funció generadora no fa servir la paraula `return`, sinó `yield`.

La diferència principal entre una funció generadora i una funció normal és que quan es retorna un valor amb `yield` a la funció generadora, la funció retorna el control a qui la va cridar (fins aquí igual) però aquesta funció no termina, sino que s'atura i el seu estat es guarda, permetent que la seva execució pugui continuar més endavant.

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

## Asyncio - Entrada i sortida assíncrona i tasques concurrents
[Asyncio a Pyhon3](https://docs.python.org/3/library/asyncio.html)

Es fa servir la sintaxi **async / await**.

**Assincronia**: Permet no bloquejar processos a l'espera del final d'alguna operació externa (establiment d'alguna connexió, operació d'entrada o sortida, ...).

**Concurrència**: Execució de tasques en paral·lel.

## Tasks and coroutines
[Tasks and coroutines in Python3](https://docs.python.org/3/library/asyncio-task.html#coroutine)

API d'alt nivell del mòdul asyncio.

### Conceptes i definicions del mòdul asyncio

**Co-routines**: Funcions que poden pausar o reprendre la seva execució. Són funcions que es defineixen amb `async def` al davant i serveixen per incloure codi assíncron dins d'elles. S'executen amb la paraula `await` al davant (la funció que la crida espera a que finalitzi l'execució) o amb la funció `asyncio.run()`, **no es poden executar directament sense fer servir await ni run()**.

**Tasques**: Són *co-routeines* que s'executen en paral·lel un cop creades. Comparteixen entre elles la CPU. Les tasques es generen amb `asyncio.create_task()`.

### Funcions del mòdul asyncio

* `asyncio.sleep()`
* `asyncio.run()` - Executa l'*event loop* del programa.
* `create_task()` - crea i executa una tasca.
* `asyncio.taskGroup()` - permet agrupar tasques i executar-les en paral·lel. La funció o el codi que crida `taskGroup` fa un `await` implícit i espera a que s'acabin d'executar les tasques del grup abans de finalitzar.
* `asyncio.gather()` - Similar a `taskGroup()` però anterior. Executa grup de tasques en paral·lel que passem com a arguments a la funció.

### Proves

**Prova 1 - No concurrència**

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():

    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

En aquest exemple, no hi ha concurrència, per lo que la sortida és:

```bash
(.venv) joan@super-ThinkBook-14-G4-IAP:~/src/python-apunts$ python3 test_tasks.py 
started at 14:37:31
hello 
world 
finished at 14:37:34
```

**Prova 2 - Concurrència però el codi que les crida no s'espera a que les tasques finalitzin**

Modifiquem el `main`:

```python
async def main():

    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    print(f"finished at {time.strftime('%X')}")
```

Sortida:

```bash
$ python3 test_tasks.py 
started at 14:42:31
finished at 14:42:31
```

**Prova 3 - Concurrència i codi principal espera a les dues tasques**

```python
async def main():

    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```

```bash
$ python3 test_tasks.py 
started at 14:43:35
hello
world
finished at 14:43:37
```

Que seria equivalent, en aquest exemple, a posar només la línea `await task2`.

**Prova 4 - equivalent a 3 però agrupant les tasques**

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")
```

## Async generators

[Asynchronous Generators in Python](https://superfastpython.com/asynchronous-generators-in-python/)

## varis

### Paraula clau `pass`

En Python, pass és una instrucció buida que no fa res. S’utilitza quan la sintaxi requereix una línia de codi però no volem executar res en aquell moment.

```python
def funcio_pendent():
    pass  # Evitem error de sintaxi

print("El programa continua...")
```
