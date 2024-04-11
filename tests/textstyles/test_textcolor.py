import unittest

from pyloggermanager.textstyles import TextColor


class TestTextColor(unittest.TestCase):
    """Unit test cases for TextColor class"""

    _new_color_name = 'NAVY_BLUE'
    _new_color_code = '\033[38;5;18m'

    _red_color_code = '\033[31m'
    _red_color_name = 'RED'

    def tearDown(self) -> None:
        TextColor._color_to_name.pop(self._new_color_code, None)
        TextColor._name_to_color.pop(self._new_color_name, None)

    def test_color_property(self):
        """
        Test if the standard color property is retrievable.
        """
        actual_color_code = TextColor.RED
        self.assertEqual(actual_color_code, self._red_color_code)

    def test_add_color_valid(self):
        """
        Test if the add_color method is able to add the color details to dict when valid inputs are provided.
        """
        TextColor.add_color(self._new_color_name, self._new_color_code)
        actual_color_code = TextColor.get_color(self._new_color_name)
        self.assertEqual(actual_color_code, self._new_color_code)

    def test_add_color_invalid_name(self):
        """
        Test if the add_color method raises TypeError when invalid datatype is passed for name property.
        """
        new_color_name = 100
        with self.assertRaises(TypeError):
            TextColor.add_color(new_color_name, self._new_color_code)

    def test_add_color_invalid_code(self):
        """
        Test if the add_color method raises TypeError when invalid datatype is passed for code property.
        """
        new_color_code = {'\033[48;2;139;69;19m'}
        with self.assertRaises(TypeError):
            TextColor.add_color(self._new_color_name, new_color_code)

    def test_get_colors(self):
        """
        Test if expected dict of colors is return when get_colors is called.
        """
        expected_dict = {
            'BLACK': "\033[30m",
            'RED': "\033[31m",
            'GREEN': "\033[32m",
            'YELLOW': "\033[33m",
            'BLUE': "\033[34m",
            'MAGENTA': "\033[35m",
            'CYAN': "\033[36m",
            'WHITE': "\033[37m"
        }
        actual_dict = TextColor.get_colors()
        self.assertDictEqual(actual_dict, expected_dict)

    def test_get_color_valid_name(self):
        """
        Test if the get_color returns color code when valid color name is provided.
        """
        actual_color_code = TextColor.get_color(self._red_color_name)
        self.assertEqual(actual_color_code, self._red_color_code)

    def test_get_color_valid_code(self):
        """
        Test if the get_color returns color name when valid color code is provided.
        """
        actual_color_name = TextColor.get_color(self._red_color_code)
        self.assertEqual(actual_color_name, self._red_color_name)

    def test_get_color_invalid_color_str(self):
        """
        Test if TypeError is raised when invalid name/code datatype is passed to get_color method.
        """
        with self.assertRaises(TypeError):
            TextColor.get_color(100)

    def test_get_color_invalid_color_name(self):
        """
        Test if ValueError is raised when invalid name is passed to get_color method.
        """
        with self.assertRaises(ValueError):
            TextColor.get_color(self._new_color_name)

    def test_get_color_invalid_color_code(self):
        """
        Test if ValueError is raised when invalid code is passed to get_color method.
        """
        with self.assertRaises(ValueError):
            TextColor.get_color(self._new_color_code)

    def test_is_valid_color_valid_name(self):
        """
        Test if True is returned when valid color name is provided.
        """
        return_value = TextColor.is_valid_color(self._red_color_name)
        self.assertTrue(return_value)

    def test_is_valid_color_valid_code(self):
        """
        Test if True is returned when valid color code is provided.
        """
        return_value = TextColor.is_valid_color(self._red_color_code)
        self.assertTrue(return_value)

    def test_is_valid_color_invalid(self):
        """
        Test if TypeError is raised when invalid datatype is passed to method.
        """
        with self.assertRaises(TypeError):
            TextColor.is_valid_color(100)

    def test_is_valid_color_invalid_color_name(self):
        """
        Test if False is return when invalid color name is provided.
        """
        return_value = TextColor.is_valid_color(self._new_color_name)
        self.assertFalse(return_value)

    def test_is_valid_color_invalid_color_code(self):
        """
        Test if False is return when invalid color code is provided.
        """
        return_value = TextColor.is_valid_color(self._new_color_code)
        self.assertFalse(return_value)

    def test_remove_color_valid(self):
        """
        Test remove color works as expected when valid inputs are provided.
        """
        TextColor.remove_color(self._red_color_name)
        with self.assertRaises(ValueError):
            TextColor.get_color(self._red_color_name)

    def test_remove_color_invalid_name(self):
        """
        Test remove color raises TypeError when invalid name datatype is provided.
        """
        with self.assertRaises(TypeError):
            TextColor.remove_color({'text'})

    def test_remove_color_invalid_color(self):
        """
        Test remove color raises ValueError when invalid code that do not exist is provided.
        """
        with self.assertRaises(ValueError):
            TextColor.remove_color(self._new_color_name)


if __name__ == "__main__":
    unittest.main()
