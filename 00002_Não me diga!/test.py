class Test(unittest.TestCase):

  def test_exemplo_1(self):
  	self.assertFalse(
    	perde_tabu("essa frase vence", ["branco", "preto"]),
  	    'perde_tabu("essa frase vence", ["branco", "preto"]) deve retornar False')

  def test_exemplo_2(self):
  	self.assertTrue(
    	perde_tabu("essa frase não vence", ["sim", "não"]),
  	    'perde_tabu("essa frase não vence", ["sim", "não"]) deve retornar True')

  def test_exemplo_3(self):
  	self.assertFalse(
    	perde_tabu("embaixo a nogueira", ["acima", "arvore", "sombra", "noz"]),
  	    'perde_tabu("embaixo a nogueira", ["acima", "arvore", "sombra", "noz"]) deve retornar False')

  def test_variante_1(self):
  	self.assertFalse(
    	perde_tabu("essa frase vence", ["sim", "não", "branco", "preto"]),
  	    'perde_tabu("essa frase vence", ["sim", "não", "branco", "preto"]) deve retornar False')
 
  def test_variante_2(self):
  	self.assertTrue(
    	perde_tabu("essa frase não vence", ["sim", "não", "branco", "preto"]),
  	    'perde_tabu("essa frase não vence", ["sim", "não", "branco", "preto"]) deve retornar True')
 
  def test_variante_3(self):
  	self.assertFalse(
    	perde_tabu("embaixo a nogueira", ["sim", "não", "branco", "preto", "em"]),
  	    'perde_tabu("embaixo a nogueira", ["sim", "não", "branco", "preto", "em"]) deve retornar False')

  def test_variante_(self):
  	self.assertTrue(
    	perde_tabu("quem perde", ["vence", "perde"]),
  	    'perde_tabu("quem perde", ["vence", "perde"]) deve retornar True')        