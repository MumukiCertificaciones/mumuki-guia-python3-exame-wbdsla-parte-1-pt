class Test(unittest.TestCase):

  def test_hola(self):
    self.assertEquals(jeringozo("Hola"), "Hopolapa", 'jeringozo("Hola") debe retornar "Hopolapa"')

  def test_casa(self):
    self.assertEquals(jeringozo("Casa"), "Capasapa", 'jeringozo("Casa") debe retornar "Capasapa"')

  def test_perro(self):
    self.assertEquals(jeringozo("Perro"), "Peperropo", 'jeringozo("Perro") debe retornar "Peperropo"')

  def test_carpincho(self):
    self.assertEquals(jeringozo("Carpincho"), "Caparpipinchopo", 'jeringozo("Carpincho") debe retornar "Caparpipinchopo"')

  def test_universo(self):
    self.assertEquals(jeringozo("universo"), "upunipivepersopo", 'jeringozo("universo") debe retornar "upunipivepersopo"')  
