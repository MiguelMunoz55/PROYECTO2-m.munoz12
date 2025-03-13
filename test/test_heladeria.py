import unittest
from app.controllers.funciones import esto_es_sano, las_calorias, costos, rentabilidad, el_mejor_producto

class TestHeladeria(unittest.TestCase):

    def test_esto_es_sano(self):
        self.assertTrue(esto_es_sano(80, True))
        self.assertFalse(esto_es_sano(120, False))
        self.assertTrue(esto_es_sano(90, False))

    def test_las_calorias(self):
        self.assertEqual(las_calorias([100, 200, 300]), 570)
        self.assertEqual(las_calorias([0, 0, 0]), 0)
        self.assertEqual(las_calorias([100]), 95)

    def test_costos(self):
        ing1 = {"nombre": "Fresa", "precio": 50}
        ing2 = {"nombre": "Chocolate", "precio": 70}
        ing3 = {"nombre": "Vainilla", "precio": 30}
        self.assertEqual(costos(ing1, ing2, ing3), 150)

    def test_rentabilidad(self):
        ing1 = {"precio": 50}
        ing2 = {"precio": 30}
        ing3 = {"precio": 20}
        self.assertEqual(rentabilidad(150, ing1, ing2, ing3), 50)
        self.assertEqual(rentabilidad(100, ing1, ing2, ing3), 0)

    def test_el_mejor_producto(self):
        prod1 = {"nombre": "Copa Fresa", "rentabilidad": 50}
        prod2 = {"nombre": "Malteada Choco", "rentabilidad": 70}
        prod3 = {"nombre": "Helado Vainilla", "rentabilidad": 60}
        prod4 = {"nombre": "Banana Split", "rentabilidad": 80}
        
        self.assertEqual(el_mejor_producto(prod1, prod2, prod3, prod4), "Banana Split")

if __name__ == '__main__':
    unittest.main()