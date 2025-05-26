import requests
import unittest

class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        self.school_url = 'http://localhost:5000'
        self.reservation_url = 'http://localhost:5001'

    def test_00_reset_apis(self):
        r1 = requests.post(f'{self.school_url}/resetar')
        r2 = requests.post(f'{self.reservation_url}/salas/resetar')
        self.assertEqual(r1.status_code, 200)
        self.assertEqual(r2.status_code, 200)

    def test_01_criar_turmas(self):
        r_prof = requests.post(f'{self.school_url}/professores', json={
            'id': 1, 'nome': 'fernando', 'idade': 27, 'materia': 'matematica'
        })
        r1 = requests.post(f'{self.school_url}/turmas', json={
            'id': 1, 'descricao': 'sala mat', 'professor_id': 1, 'ativo': True
        })
        r2 = requests.post(f'{self.school_url}/turmas', json={
            'id': 2, 'descricao': 'sala dev', 'professor_id': 1, 'ativo': True
        })
        self.assertEqual(r1.status_code, 201)
        self.assertEqual(r2.status_code, 201)

    # TESTES DE SALAS

    def test_02_post_sala_completa(self):
        r = requests.post(f'{self.reservation_url}/salas', json={
            'id': 1, 'numero': '101', 'descricao': 'Laboratório'
        })
        self.assertEqual(r.status_code, 201)

    def test_03_post_sala_invalida(self):
        r = requests.post(f'{self.reservation_url}/salas', json={})
        self.assertEqual(r.status_code, 400)

    def test_04_get_salas(self):
        r = requests.get(f'{self.reservation_url}/salas')
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), list)

    def test_05_get_sala_por_id(self):
        r = requests.get(f'{self.reservation_url}/salas/1')
        self.assertIn(r.status_code, [200, 404])  # depende se foi criada ou não

    # TESTES DE RESERVAS

    def test_06_post_reserva_completa(self):
        requests.post(f'{self.reservation_url}/salas', json={
        'numero': '101',
        'descricao': 'Sala de Teste'
        }) # Cria a sala para a reserva

        r_salas = requests.get(f'{self.reservation_url}/salas')
        self.assertEqual(r_salas.status_code, 200)
        salas = r_salas.json()
        self.assertGreater(len(salas), 0)
        id_sala = salas[0]['id']

        r = requests.post(f'{self.reservation_url}/salas/reservas', json={
            'id_sala': id_sala,
            'id_turma': 1,
            'data_reserva': '2025-06-01',
            'hora_inicio': '09:00',
            'hora_fim': '10:00'
        })
        self.assertEqual(r.status_code, 201)

    def test_07_post_reserva_invalida(self):
        r = requests.post(f'{self.reservation_url}/salas/reservas', json={
            'id_sala': 1,
            'data_reserva': '2025-06-01',
            'hora_inicio': '09:00',
            'hora_fim': '10:00'
        })  # falta o id_turma
        self.assertEqual(r.status_code, 400)

    def test_08_get_reservas(self):
        r = requests.get(f'{self.reservation_url}/salas/reservas')
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), list)

    def test_09_get_reserva_por_id(self):
        r = requests.get(f'{self.reservation_url}/salas/reservas/1')
        self.assertIn(r.status_code, [200, 404])
         
def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runTests()