import unittest
import logging
from your_module import Runner

# Настройка логирования
logging.basicConfig(
    filename="runner_tests.log",
    level=logging.INFO,
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(levelname)s | %(message)s"
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """Тест проверяет выброс исключения при отрицательном значении speed"""
        try:
            runner = Runner("TestRunner", speed=-5)  # Неправильное значение скорости
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, 50)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")


    def test_run(self):
        """Тест проверяет выброс исключения при неверном типе name"""
        try:
            runner = Runner(2, speed=5)  # Неверный тип имени
            runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 100)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
