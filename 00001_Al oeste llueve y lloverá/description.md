Antes de dormir, Ale olha a previsão do dia seguinte para se vestir de acordo :closed_umbrella:. Para fazer isso, precisa de uma função que, com base na probabilidade de chuva e um booleano que diz se vai ter vento ou não, dá um resumo:

```python
ム $forecast(20, Verdadeiro)
"Amanhã há poucas chances de chuva com vento"

ム $forecast(40, Verdadeiro)
"Amanhã há chances médias de chuva com vento"

ム $forecast(80, Falso)
"Amanhã há grandes chances de chuva sem vento"
```

Eu tinha em mente que:

* se houver menos de 30% de chance de chuva, consideramos baixa;
* se houver mais de $corteAlta%, vamos considerá-los altos
caso contrário, consideraremos que são médias.

> Eu defini a função `$forecast`.