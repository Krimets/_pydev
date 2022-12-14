import unittest
from utils import send_mail, concat_name, set_user_meta
from models import User


class UtilsTestCase(unittest.TestCase):

    def test_concat_name(self):
        """
        Тестируємо функцію `concat_name`.
        """
        value1, value2 = 'test1', 'test2'
        result = concat_name(value1, value2)
        expected_result = '{} {}'.format(value1, value2)
        self.assertEqual(result, expected_result)

    def test_set_user_meta(self):
        """
        Тестуємо функцію `set_user_meta`, чи виконує вона присвоєння meta та чи коретно вона працює.
        """
        instance = User('test@example.com', '1', '2')
        test_meta = {'test_key': 'test_value'}
        set_user_meta(instance, test_meta)
        self.assertDictEqual(instance.meta, test_meta)
