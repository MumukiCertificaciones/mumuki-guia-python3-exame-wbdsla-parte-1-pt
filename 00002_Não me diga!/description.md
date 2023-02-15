:see_no_evil: _Tabu_ é um jogo onde você não pode dizer certas palavras.

É por isso que vamos precisar de uma função `e_tabu` que nos diga se a frase contém alguma das palavras proibidas:

```python
ムe_tabu("essa frase vence", ["branco", "preto"])
False
ムe_tabu("essa frase não vence", ["sim", "não"])
True
ムe_tabu("debaixo da nogueira", ["acima", "árvore", "sombra", "noz"])
False
```

:warning: Para resolver este problema, você achará útil a função `str.split`, que, entre outras coisas, permite dividir uma string em palavras:
 
```python
ムstr.split("oi tudo bem")
['oi', 'tudo', 'bem']
```

> Escreva a função `e_tabu`.
>
