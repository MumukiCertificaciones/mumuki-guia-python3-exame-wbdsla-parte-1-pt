class Test(unittest.TestCase):

  def test_exemplo_1(self):
    self.assertFalse(
      perde_tabu("essa frase vence", ["blanco", "negro"]),
      'perde_tabu("essa frase vence", ["blanco", "negro"]) debería retornar False')

  def test_exemplo_2(self):
    self.assertTrue(
      perde_tabu("essa frase não perde", ["si", "no"]),
      'perde_tabu("essa frase não perde", ["si", "no"]) debería retornar True')

  def test_exemplo_3(self):
    self.assertFalse(
      perde_tabu("embaixo a nogueira", ["arriba", "árbol", "sombra", "nuez"]),
      'perde_tabu("embaixo a nogueira", ["arriba", "árbol", "sombra", "nuez"]) debería retornar False')

  def test_variante_1(self):
    self.assertFalse(
      perde_tabu("essa frase vence", ["si", "no", "blanco", "negro"]),
      'perde_tabu("essa frase vence", ["si", "no", "blanco", "negro"]) debería retornar False')
  
  def test_variante_2(self):
    self.assertTrue(
      perde_tabu("essa frase não perde", ["si", "no", "blanco", "negro"]),
      'perde_tabu("essa frase não perde", ["si", "no", "blanco", "negro"]) debería retornar True')
  
  def test_variante_3(self):
    self.assertFalse(
      perde_tabu("embaixo a nogueira", ["si", "no", "blanco", "negro"]),
      'perde_tabu("embaixo a nogueira", ["si", "no", "blanco", "negro"]) debería retornar False')


