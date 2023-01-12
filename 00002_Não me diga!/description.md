:see_no_evil: _Tabu_ é um jogo onde você não pode dizer certas palavras.

É por isso que vamos precisar de uma função `pierde_tabu` que nos diga se a frase contém alguma das palavras proibidas:

```python
ム perde_tabu("essa frase vence", ["branco", "preto"])
falso
ム perde_tabu("essa frase não perde", ["sim", "não"])
Verdadeiro
ム perdera_tabu("debaixo a nogueira", ["acima", "árvore", "sombra", "noz"])
falso
```

:warning: Para resolver este problema, você achará útil a função `str.split`, que, entre outras coisas, permite dividir uma string em palavras:
 
```python
ム str.split("oi tudo bem")
['Oi', 'tudo', 'bem']
```

> Eu escrevi a função `perde_tabu`.
>