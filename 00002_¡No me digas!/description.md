:see_no_evil: El _tabú_ es un juego donde no podés decir ciertas palabras.

Por eso vamos a necesitar una función `pierde_tabu` que nos diga si la frase contiene alguna de las palabras prohibidas:

```python
ム pierde_tabu("esta frase gana", ["blanco", "negro"])
False
ム pierde_tabu("esta frase no pierde", ["si", "no"])
True
ム pierde_tabu("bajo el nogal", ["arriba", "árbol", "sombra", "nuez"])
False
```

:warning: Para resolver este problema te resultará útil la función `str.split`, que, entre otras cosas, permite dividir un string en palabras: 
 
```python
ム str.split("hola que tal")
['hola', 'que', 'tal']
```

> Escribí la función `pierde_tabu`. 
> 


