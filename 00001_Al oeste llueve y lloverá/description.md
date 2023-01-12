Antes de ir a dormir Ale mira el pronóstico del día siguiente para vestirse de manera acorde :closed_umbrella:. Para ello necesita una función que, a partir de la probabilidad de lluvia y de un booleano que le dice si va a haber viento o no, le haga un resumen:

```python
ム $pronostico(20, True)
"Mañana hay bajas probabilidades de lluvia con viento"

ム $pronostico(40, True)
"Mañana hay medias probabilidades de lluvia con viento"

ム $pronostico(80, False)
"Mañana hay altas probabilidades de lluvia sin viento"
```

Tené en cuenta que:

* si hay menos de 30% de probabilidades de lluvia, consideramos que son bajas;
* si hay más de $corteAlta%, consideraremos que son altas
en caso contrario, consideraremos que son medias.

> Definí la función `$pronostico`.
