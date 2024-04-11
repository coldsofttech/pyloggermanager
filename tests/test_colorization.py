import unittest

from pyloggermanager import Colorization
from pyloggermanager.textstyles import TextColor, TextBackgroundColor


class TestColorization(unittest.TestCase):
    """Unit test cases for Colorization class."""

    def tearDown(self) -> None:
        keywords = Colorization.get_keyword_color_mappings()
        for keyword in keywords:
            Colorization.remove_keyword_color_mapping(keyword)

    def test_reset_property(self):
        """Test if reset property returns expected value."""
        expected_value = '\033[0m'
        self.assertEqual(Colorization.RESET, expected_value)

    def test_colorize_message_valid(self):
        """Test if colorize message returns expected value when valid inputs are provided."""
        Colorization.set_keyword_color_mapping('error', ['error'], TextColor.RED)
        expected_output = (
            f'{TextColor.RED}'
            f'Test error message'
            f'{Colorization.RESET}'
        ) if Colorization.is_colorization_supported() else (
            'Test error message'
        )
        self.assertEqual(Colorization.colorize_message('Test error message'), expected_output)

    def test_colorize_message_invalid_name(self):
        """Test if colorize message raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping(100, ['error'], TextColor.RED)

    def test_colorize_message_invalid_keywords(self):
        """Test if colorize message raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping('error', 199, TextColor.RED)

    def test_colorize_message_invalid_text_color(self):
        """Test if colorize message raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping('error', ['error'], 100)

    def test_colorize_message_invalid_text_background_color(self):
        """Test if colorize message raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping(
                'error', ['error'], TextColor.RED, 100
            )

    def test_colorize_message_invalid_text_effect(self):
        """Test if colorize message raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping(
                'error', ['error'], TextColor.RED, TextBackgroundColor.WHITE, 100
            )

    def test_colorize_message_invalid_text_color_do_not_exist(self):
        """Test if colorize message raises ValueError when color / effect that do not exist is provided."""
        with self.assertRaises(ValueError):
            Colorization.set_keyword_color_mapping('error', ['error'], 'ORANGE')

    def test_colorize_message_invalid_text_background_color_do_not_exist(self):
        """Test if colorize message raises ValueError when color / effect that do not exist is provided."""
        with self.assertRaises(ValueError):
            Colorization.set_keyword_color_mapping(
                'error', ['error'], TextColor.RED, 'ORANGE'
            )

    def test_colorize_message_invalid_text_effect_do_not_exist(self):
        """Test if colorize message raises ValueError when color / effect that do not exist is provided."""
        with self.assertRaises(ValueError):
            Colorization.set_keyword_color_mapping(
                'error', ['error'], TextColor.RED, TextBackgroundColor.WHITE, 'STRIKETHROUGH'
            )

    def test_colorize_message_regex(self):
        """Test if colorize message works as expected when regex pattern is provided."""
        Colorization.set_keyword_color_mapping('error', ['warning|error'], TextColor.RED)
        expected_output = (
            f'{TextColor.RED}'
            f'Test error message'
            f'{Colorization.RESET}'
        ) if Colorization.is_colorization_supported() else (
            'Test error message'
        )
        self.assertEqual(Colorization.colorize_message('Test error message'), expected_output)

        expected_output = (
            f'{TextColor.RED}'
            f'Test warning message'
            f'{Colorization.RESET}'
        ) if Colorization.is_colorization_supported() else (
            'Test warning message'
        )
        self.assertEqual(Colorization.colorize_message('Test warning message'), expected_output)

        expected_output = 'Test success message'
        self.assertEqual(Colorization.colorize_message('Test success message'), expected_output)

    def test_colorize_message_no_keywords(self):
        """Test if colorize message works as expected when no keywords are provided."""
        expected_output = 'Test message'
        self.assertEqual(Colorization.colorize_message('Test message'), expected_output)

    def test_get_keyword_color_mapping_valid(self):
        """Test if the get keyword color mapping returns expected value when valid inputs are provided."""
        Colorization.set_keyword_color_mapping('error', ['error'], TextColor.RED)
        expected_output = {
            'keywords': ['error'],
            'colorization': {
                'text_color': TextColor.RED,
                'text_background_color': None,
                'text_effect': None
            }
        }
        self.assertDictEqual(Colorization.get_keyword_color_mapping('error'), expected_output)

    def test_get_keyword_color_mapping_invalid(self):
        """Test if the get keyword color mapping raises TypeError when invalid inputs are provided."""
        Colorization.set_keyword_color_mapping('error', ['error'], TextColor.RED)
        with self.assertRaises(TypeError):
            Colorization.get_keyword_color_mapping(100)

    def test_get_keyword_color_mapping_do_not_exist(self):
        """Test if the get keyword color mapping raises ValueError when invalid keyword is provided."""
        Colorization.set_keyword_color_mapping('error', ['error'], TextColor.RED)
        with self.assertRaises(ValueError):
            Colorization.get_keyword_color_mapping('success')

    def test_get_keyword_color_mappings_no_input(self):
        """Test if the get keyword color mappings is empty when no keywords exist."""
        keywords = Colorization.get_keyword_color_mappings()
        assert len(keywords) == 0

    def test_get_keyword_color_mappings_valid(self):
        """Test if the get keyword color mappings returns as expected."""
        Colorization.set_keyword_color_mapping('error', 'error', TextColor.RED)
        keywords = Colorization.get_keyword_color_mappings()
        assert len(keywords) > 0

    def test_is_valid_mapping_exists(self):
        """Test if is valid mapping method returns True when value exists."""
        Colorization.set_keyword_color_mapping('error', 'error', TextColor.RED)
        self.assertTrue(Colorization.is_valid_mapping('error'))

    def test_is_valid_mapping_do_not_exists(self):
        """Test if is valid mapping method returns False when value do not exist."""
        Colorization.set_keyword_color_mapping('error', 'error', TextColor.RED)
        self.assertFalse(Colorization.is_valid_mapping('success'))

    def test_is_valid_mapping_invalid(self):
        """Test if is valid mapping method raises TypeError when invalid input is provided."""
        with self.assertRaises(TypeError):
            Colorization.is_valid_mapping(100)

    def test_remove_keyword_color_mapping_valid(self):
        """Test if remove keyword color mappings works as expected when valid inputs are provided."""
        Colorization.set_keyword_color_mapping('error', 'error', TextColor.RED)
        Colorization.remove_keyword_color_mapping('error')
        self.assertFalse(Colorization.is_valid_mapping('error'))

    def test_remove_keyword_color_mapping_invalid(self):
        """Test if remove keyword color mapping raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Colorization.remove_keyword_color_mapping(100)

    def test_remove_keyword_color_mapping_do_not_exist(self):
        """Test if remove keyword color mapping raises ValueError when invalid inputs are provided."""
        with self.assertRaises(ValueError):
            Colorization.remove_keyword_color_mapping('error')

    def test_set_keyword_color_mapping_valid(self):
        """Test if set keyword color mapping works as expected with valid inputs."""
        Colorization.set_keyword_color_mapping('error', ['error'], TextColor.RED)
        self.assertTrue(Colorization.is_valid_mapping('error'))

    def test_set_keyword_color_mappings_invalid_name(self):
        """Test if set keyword color mapping raises TypeError when invalid name is provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping(100, 'error', TextColor.RED)

    def test_set_keyword_color_mappings_invalid_keywords(self):
        """Test if set keyword color mapping raises TypeError when invalid keywords are provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping('error', 100, TextColor.RED)

    def test_set_keyword_color_mappings_invalid_text_color(self):
        """Test if set keyword color mapping raises TypeError when invalid text color is provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping('error', 'error', 100)

    def test_set_keyword_color_mappings_invalid_text_background_color(self):
        """Test if set keyword color mapping raises TypeError when invalid text background color is provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping(
                'error', 'error', TextColor.RED, 100
            )

    def test_set_keyword_color_mappings_invalid_text_effect(self):
        """Test if set keyword color mapping raises TypeError when invalid text effect is provided."""
        with self.assertRaises(TypeError):
            Colorization.set_keyword_color_mapping(
                'error', 'error', TextColor.RED, TextBackgroundColor.WHITE, 100
            )


if __name__ == "__main__":
    unittest.main()
