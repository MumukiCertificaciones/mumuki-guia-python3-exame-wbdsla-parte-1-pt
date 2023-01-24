class Test(unittest.TestCase):

  def test_exemplo_1(self):
    self.assertEquals($forecast(20, True), "Amanhã há poucas chances de chuva com vento")

  def test_exemplo_2(self):
    self.assertEquals($forecast(40, True), "Amanhã há poucas chances de chuva com vento")

  def test_exemplo_3(self):
    self.assertEquals($forecast(80, False), "Amanhã há grandes chances de chuva sem vento")

  def test_mas_de_$corteAlta(self):
    self.assertEquals($forecast($corteAlta+1, False) , "Amanhã há grandes chances de chuva sem vento")

  def test_menos_de_$corteAlta(self):
    self.assertEquals($forecast($corteAlta-1, False), "Amanhã há médias chances de chuva sem vento")
