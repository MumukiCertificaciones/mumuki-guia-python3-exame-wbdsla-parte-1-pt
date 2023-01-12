class Test(unittest.TestCase):

  def test_ejemplo_1(self):
    self.assertEquals($pronostico(20, True), "Mañana hay bajas probabilidades de lluvia con viento")

  def test_ejemplo_2(self):
    self.assertEquals($pronostico(40, True), "Mañana hay medias probabilidades de lluvia con viento")

  def test_ejemplo_3(self):
    self.assertEquals($pronostico(80, False), "Mañana hay altas probabilidades de lluvia sin viento")

  def test_mas_de_$corteAlta(self):
    self.assertEquals($pronostico($corteAlta+1, False), "Mañana hay altas probabilidades de lluvia sin viento")

  def test_menos_de_$corteAlta(self):
    self.assertEquals($pronostico($corteAlta-1, False), "Mañana hay medias probabilidades de lluvia sin viento")
