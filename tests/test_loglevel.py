import unittest

from pyloggermanager import LogLevel


class TestLogLevel(unittest.TestCase):
    """Unit test cases for LogLevel class."""

    def tearDown(self) -> None:
        try:
            LogLevel.remove_level(15)
            LogLevel.set_default_level(20)
        except (KeyError, ValueError, TypeError):
            pass

    def test_debug_property(self):
        """Test if debug property value is as expected."""
        self.assertEqual(LogLevel.DEBUG, 10)

    def test_check_level_valid(self):
        """Test if check level works as expected when valid inputs are provided."""
        self.assertEqual(LogLevel.check_level(10), 10)

    def test_check_level_invalid(self):
        """Test if check level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.check_level('str')

    def test_check_level_do_not_exist(self):
        """Test if check level raises ValueError when invalid inputs are provided."""
        with self.assertRaises(ValueError):
            LogLevel.check_level(100)

    def test_get_default_mode(self):
        """Test if get default mode returns expected value."""
        self.assertEqual(LogLevel.get_default_level(), 'INFO')

    def test_get_level_valid_name(self):
        """Test if the get level returns expected value."""
        self.assertEqual(LogLevel.get_level('INFO'), 20)

    def test_get_level_valid_level(self):
        """Test if the get level returns expected value."""
        self.assertEqual(LogLevel.get_level(10), 'DEBUG')

    def test_get_level_invalid(self):
        """Test if the get level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.get_level({'dict'})

    def test_get_level_name_do_not_exist(self):
        """Test if the get level returns expected value."""
        self.assertEqual(LogLevel.get_level('RED'), '')

    def test_get_level_level_do_not_exist(self):
        """Test if the get level returns expected value."""
        self.assertEqual(LogLevel.get_level(15), 'Level 15')

    def test_get_levels(self):
        """Test if the get levels returns as expected."""
        levels = LogLevel.get_levels()
        assert len(levels) > 0

    def test_get_next_level_valid(self):
        """Test if the get next level returns as expected."""
        self.assertEqual(LogLevel.get_next_level(10), 20)

    def test_get_next_level_invalid(self):
        """Test if the get next level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.get_next_level('INFO')

    def test_get_next_level_do_not_exist(self):
        """Test if the get next level returns None when invalid inputs are provided."""
        self.assertEqual(LogLevel.get_next_level(90), None)

    def test_get_previous_level_valid(self):
        """Test if the get previous level returns as expected."""
        self.assertEqual(LogLevel.get_previous_level(20), 10)

    def test_get_previous_level_invalid(self):
        """Test if the get previous level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.get_previous_level('INFO')

    def test_get_previous_do_not_exist(self):
        """Test if the get previous level returns None when invalid inputs are provided."""
        self.assertEqual(LogLevel.get_previous_level(0), None)

    def test_is_valid_level_valid_name(self):
        """Test if is valid level returns as expected."""
        self.assertTrue(LogLevel.is_valid_level('INFO'))

    def test_is_valid_level_valid_level(self):
        """Test if is valid level returns as expected."""
        self.assertTrue(LogLevel.is_valid_level(10))

    def test_is_valid_level_invalid(self):
        """Test if is valid level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.is_valid_level({'dict'})

    def test_is_valid_level_do_not_exist(self):
        """Test if is valid level returns as expected."""
        self.assertFalse(LogLevel.is_valid_level(100))
        self.assertFalse(LogLevel.is_valid_level('DEBUG1'))

    def test_remove_level_valid_name(self):
        """Test if remove level works as expected."""
        LogLevel.set_level(15, 'CUSTOM 15')
        LogLevel.remove_level(15)
        self.assertFalse(LogLevel.is_valid_level(15))

    def test_remove_level_valid_level(self):
        """Test if remove level works as expected."""
        LogLevel.set_level(15, 'CUSTOM 15')
        LogLevel.remove_level('CUSTOM 15')
        self.assertFalse(LogLevel.is_valid_level('CUSTOM 15'))

    def test_remove_level_invalid(self):
        """Test if remove level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.remove_level({'dict'})

    def test_remove_level_do_not_exist(self):
        """Test if remove level raises ValueError when invalid inputs are provided."""
        with self.assertRaises(ValueError):
            LogLevel.remove_level(90)

        with self.assertRaises(ValueError):
            LogLevel.remove_level('CUSTOM 90')

    def test_set_default_level_valid_name(self):
        """Test if set default level works as expected."""
        LogLevel.set_default_level('DEBUG')
        self.assertEqual(LogLevel.get_default_level(), 'DEBUG')

    def test_set_default_level_valid_level(self):
        """Test if set default level works as expected."""
        LogLevel.set_default_level(30)
        self.assertEqual(LogLevel.get_default_level(), 'WARNING')

    def test_set_default_level_invalid(self):
        """Test if set default level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.set_default_level({'dict'})

    def test_set_default_level_do_not_exist(self):
        """Test if set default level raises ValueError when invalid inputs are provided."""
        with self.assertRaises(ValueError):
            LogLevel.set_default_level(90)

        with self.assertRaises(ValueError):
            LogLevel.set_default_level('CUSTOM 90')

    def test_set_level_valid(self):
        """Test if set level works as expected."""
        LogLevel.set_level(15, 'CUSTOM 15')
        self.assertEqual(LogLevel.get_level(15), 'CUSTOM 15')
        self.assertEqual(LogLevel.get_level('CUSTOM 15'), 15)

    def test_set_level_invalid(self):
        """Test if set level raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            LogLevel.set_level('CUSTOM 15', 15)


if __name__ == "__main__":
    unittest.main()
