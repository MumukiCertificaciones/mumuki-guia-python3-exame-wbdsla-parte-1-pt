:see_no_evil: _Tabu_ é um jogo onde você não pode dizer certas palavras.

É por isso que vamos precisar de uma função `pierde_tabu` que nos diga se a frase contém alguma das palavras proibidas:

```python
ム e_tabu("essa frase vence", ["branco", "preto"])
False
ム e_tabu("essa frase não vence", ["sim", "não"])
True
ム perdera_tabu("debaixo da nogueira", ["acima", "árvore", "sombra", "noz"])
False
```

:warning: Para resolver este problema, você achará útil a função `str.split`, que, entre outras coisas, permite dividir uma string em palavras:
 
```python
ム str.split("oi tudo bem")
['oi', 'tudo', 'bem']
```

> Escreva a função `e_tabu`.
>
