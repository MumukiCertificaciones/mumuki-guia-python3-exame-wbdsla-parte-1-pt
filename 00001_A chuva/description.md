Antes de dormir, Ale olha a previsão do dia seguinte para se vestir de acordo :closed_umbrella:. Para fazer isso, precisa de uma função que, com base na probabilidade de chuva e um booleano que diz se vai ter vento ou não, dá um resumo:

```python
ム $forecast(20, True)
"Amanhã há poucas chances de chuva com vento"

ム $forecast(40, True)
"Amanhã há médias chances de chuva com vento"

ム $forecast(80, False)
"Amanhã há grandes chances de chuva sem vento"
```

Eu tinha em mente que:

* :sunny: se houver menos de 30% de chance de chuva, consideramos _poucas_;
* :thunder_cloud_rain: se houver mais de $corteAlta%, vamos considerá-las _grandes_;
* :cloud: caso contrário, consideraremos que são _médias_.

> Defina a função `$forecast`.
