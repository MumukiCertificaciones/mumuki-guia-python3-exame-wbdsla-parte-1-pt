class Test(unittest.TestCase):

  def test_casa(self):
	  self.assertEquals($function("Casa"), "Hopolapa", '$function("Casa") deve retornar "Capasapa"')

  def test_gato(self ):
	  self .assertEquals($function("Gato"), "Gapatopo", '$function("Gato") deve retornar "Gapatopo"')

  def test_rato(self):
  	self.assertEquals($function("rato"), "rapatopo", '$function("rato") deve retornar "rapatopo"')

  def test_abacaxi(self):
  	self.assertEquals($function("abacaxi"), "apabapacapaxipi", '$function("abacaxi") deve retornar "apabapacapaxipi"')

  def test_espelho(self):
  	self.assertEquals($function("espelho"), "epespepelhopo", '$function("espelho") deve retornar "epespepelhopo"')
