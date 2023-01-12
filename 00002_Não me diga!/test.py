class Test(unittest.TestCase):

  def test_exemplo_1(self):
    self.assertFalse(
      perde_tabu("esta frase gana", ["blanco", "negro"]),
      'perde_tabu("esta frase gana", ["blanco", "negro"]) debería retornar False')

  def test_exemplo_2(self):
    self.assertTrue(
      perde_tabu("esta frase no pierde", ["si", "no"]),
      'perde_tabu("esta frase no pierde", ["si", "no"]) debería retornar True')

  def test_exemplo_3(self):
    self.assertFalse(
      perde_tabu("bajo el nogal", ["arriba", "árbol", "sombra", "nuez"]),
      'perde_tabu("bajo el nogal", ["arriba", "árbol", "sombra", "nuez"]) debería retornar False')

  def test_variante_1(self):
    self.assertFalse(
      perde_tabu("esta frase gana", ["si", "no", "blanco", "negro"]),
      'perde_tabu("esta frase gana", ["si", "no", "blanco", "negro"]) debería retornar False')
  
  def test_variante_2(self):
    self.assertTrue(
      perde_tabu("esta frase no pierde", ["si", "no", "blanco", "negro"]),
      'perde_tabu("esta frase no pierde", ["si", "no", "blanco", "negro"]) debería retornar True')
  
  def test_variante_3(self):
    self.assertFalse(
      perde_tabu("bajo el nogal", ["si", "no", "blanco", "negro"]),
      'perde_tabu("bajo el nogal", ["si", "no", "blanco", "negro"]) debería retornar False')


