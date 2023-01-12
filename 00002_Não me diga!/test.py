class Test(unittest.TestCase):

  def test_ejemplo_1(self):
    self.assertFalse(
      pierde_tabu("esta frase gana", ["blanco", "negro"]),
      'pierde_tabu("esta frase gana", ["blanco", "negro"]) debería retornar False')

  def test_ejemplo_2(self):
    self.assertTrue(
      pierde_tabu("esta frase no pierde", ["si", "no"]),
      'pierde_tabu("esta frase no pierde", ["si", "no"]) debería retornar True')

  def test_ejemplo_3(self):
    self.assertFalse(
      pierde_tabu("bajo el nogal", ["arriba", "árbol", "sombra", "nuez"]),
      'pierde_tabu("bajo el nogal", ["arriba", "árbol", "sombra", "nuez"]) debería retornar False')

  def test_variante_1(self):
    self.assertFalse(
      pierde_tabu("esta frase gana", ["si", "no", "blanco", "negro"]),
      'pierde_tabu("esta frase gana", ["si", "no", "blanco", "negro"]) debería retornar False')
  
  def test_variante_2(self):
    self.assertTrue(
      pierde_tabu("esta frase no pierde", ["si", "no", "blanco", "negro"]),
      'pierde_tabu("esta frase no pierde", ["si", "no", "blanco", "negro"]) debería retornar True')
  
  def test_variante_3(self):
    self.assertFalse(
      pierde_tabu("bajo el nogal", ["si", "no", "blanco", "negro"]),
      'pierde_tabu("bajo el nogal", ["si", "no", "blanco", "negro"]) debería retornar False')


