# Copyright (c) 2024 coldsofttech
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest

from pyloggermanager.textstyles import TextEffect


class TestTextEffect(unittest.TestCase):
    """Unit test cases for TextEffect class"""

    _new_effect_name = 'STRIKETHROUGH'
    _new_effect_code = '\033[9m'

    _bold_effect_code = '\033[1m'
    _bold_effect_name = 'BOLD'

    def tearDown(self) -> None:
        TextEffect._effect_to_name.pop(self._new_effect_code, None)
        TextEffect._name_to_effect.pop(self._new_effect_name, None)

    def test_effect_property(self):
        """
        Test if the standard effect property is retrievable.
        """
        actual_effect_code = TextEffect.BOLD
        self.assertEqual(actual_effect_code, self._bold_effect_code)

    def test_add_effect_valid(self):
        """
        Test if the add_effect method is able to add the effect details to dict when valid inputs are provided.
        """
        TextEffect.add_effect(self._new_effect_name, self._new_effect_code)
        actual_effect_code = TextEffect.get_effect(self._new_effect_name)
        self.assertEqual(actual_effect_code, self._new_effect_code)

    def test_add_effect_invalid_name(self):
        """
        Test if the add_effect method raises TypeError when invalid datatype is passed for name property.
        """
        new_effect_name = 100
        with self.assertRaises(TypeError):
            TextEffect.add_effect(new_effect_name, self._new_effect_code)

    def test_add_effect_invalid_code(self):
        """
        Test if the add_effect method raises TypeError when invalid datatype is passed for code property.
        """
        new_effect_code = {'text'}
        with self.assertRaises(TypeError):
            TextEffect.add_effect(self._new_effect_name, new_effect_code)

    def test_get_effects(self):
        """
        Test if expected dict of effects is return when get_effects is called.
        """
        expected_dict = {
            'BOLD': "\033[1m",
            'UNDERLINE': "\033[4m",
            'ITALIC': "\033[3m"
        }
        actual_dict = TextEffect.get_effects()
        self.assertDictEqual(actual_dict, expected_dict)

    def test_get_effect_valid_name(self):
        """
        Test if the get_effect returns effect code when valid effect name is provided.
        """
        actual_effect_code = TextEffect.get_effect(self._bold_effect_name)
        self.assertEqual(actual_effect_code, self._bold_effect_code)

    def test_get_effect_valid_code(self):
        """
        Test if the get_effect returns effect name when valid effect code is provided.
        """
        actual_effect_name = TextEffect.get_effect(self._bold_effect_code)
        self.assertEqual(actual_effect_name, self._bold_effect_name)

    def test_get_effect_invalid_effect_str(self):
        """
        Test if TypeError is raised when invalid name/code datatype is passed to get_effect method.
        """
        with self.assertRaises(TypeError):
            TextEffect.get_effect(100)

    def test_get_effect_invalid_effect_name(self):
        """
        Test if ValueError is raised when invalid name is passed to get_effect method.
        """
        with self.assertRaises(ValueError):
            TextEffect.get_effect(self._new_effect_name)

    def test_get_effect_invalid_effect_code(self):
        """
        Test if ValueError is raised when invalid code is passed to get_effect method.
        """
        with self.assertRaises(ValueError):
            TextEffect.get_effect(self._new_effect_code)

    def test_is_valid_effect_valid_name(self):
        """
        Test if True is returned when valid effect name is provided.
        """
        return_value = TextEffect.is_valid_effect(self._bold_effect_name)
        self.assertTrue(return_value)

    def test_is_valid_effect_valid_code(self):
        """
        Test if True is returned when valid effect code is provided.
        """
        return_value = TextEffect.is_valid_effect(self._bold_effect_code)
        self.assertTrue(return_value)

    def test_is_valid_effect_invalid(self):
        """
        Test if TypeError is raised when invalid datatype is passed to method.
        """
        with self.assertRaises(TypeError):
            TextEffect.is_valid_effect(100)

    def test_is_valid_effect_invalid_effect_name(self):
        """
        Test if False is return when invalid effect name is provided.
        """
        return_value = TextEffect.is_valid_effect(self._new_effect_name)
        self.assertFalse(return_value)

    def test_is_valid_effect_invalid_effect_code(self):
        """
        Test if False is return when invalid effect code is provided.
        """
        return_value = TextEffect.is_valid_effect(self._new_effect_code)
        self.assertFalse(return_value)

    def test_remove_effect_valid(self):
        """
        Test remove effect works as expected when valid inputs are provided.
        """
        TextEffect.remove_effect(self._bold_effect_name)
        with self.assertRaises(ValueError):
            TextEffect.get_effect(self._bold_effect_name)

    def test_remove_effect_invalid_name(self):
        """
        Test remove effect raises TypeError when invalid name datatype is provided.
        """
        with self.assertRaises(TypeError):
            TextEffect.remove_effect({'text'})

    def test_remove_effect_invalid_effect(self):
        """
        Test remove effect raises ValueError when invalid code that do not exist is provided.
        """
        with self.assertRaises(ValueError):
            TextEffect.remove_effect(self._new_effect_name)


if __name__ == "__main__":
    unittest.main()
