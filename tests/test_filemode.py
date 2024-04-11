import unittest

from pyloggermanager import FileMode


class TestFileMode(unittest.TestCase):
    """Unit test cases for FileMode class."""

    def tearDown(self) -> None:
        FileMode.set_default_mode(FileMode.APPEND)

    def test_read_property(self):
        """Test if read property value is as expected."""
        self.assertEqual(FileMode.READ, 'r')

    def test_check_mode_valid(self):
        """Test if check mode works as expected when valid inputs are provided."""
        self.assertEqual(FileMode.check_mode('r'), 'r')
        self.assertEqual(FileMode.check_mode('READ'), 'READ')

    def test_check_mode_invalid(self):
        """Test if check mode raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            FileMode.check_mode(100)

    def test_check_mode_do_not_exist(self):
        """Test if check mode raises ValueError when invalid inputs are provided."""
        with self.assertRaises(ValueError):
            FileMode.check_mode('c')

    def test_get_default_mode(self):
        """Test if get default mode returns expected value."""
        self.assertEqual(FileMode.get_default_mode(), FileMode.APPEND)

    def test_get_file_mode_valid_name(self):
        """Test if the get file mode returns value as expected."""
        self.assertEqual(FileMode.get_file_mode('r'), 'READ')

    def test_get_file_mode_valid_mode(self):
        """Test if the get file mode returns value as expected."""
        self.assertEqual(FileMode.get_file_mode('READ'), 'r')

    def test_get_file_mode_invalid(self):
        """Test if the get file mode raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            FileMode.get_file_mode(100)

    def test_get_file_mode_do_not_exist(self):
        """Test if the get file mode raises ValueError when invalid inputs are provided."""
        with self.assertRaises(ValueError):
            FileMode.get_file_mode('c')

    def test_get_file_modes(self):
        """Test if the get file modes returns values as expected."""
        modes = FileMode.get_file_modes()
        assert len(modes) > 0

    def test_get_readable_modes(self):
        """Test if the get readable modes returns values as expected."""
        modes = FileMode.get_readable_modes()
        assert len(modes) > 0

    def test_get_writable_modes(self):
        """Test if the get writable modes returns values as expected."""
        modes = FileMode.get_writable_modes()
        assert len(modes) > 0

    def test_is_valid_mode_valid(self):
        """Test if is valid mode returns True when valid values are provided."""
        self.assertTrue(FileMode.is_valid_mode('r'))

    def test_is_valid_mode_invalid(self):
        """Test if is valid mode raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            FileMode.is_valid_mode(100)

    def test_is_valid_mode_do_not_exist(self):
        """Test if is valid mode returns False when invalid values are provided."""
        self.assertFalse(FileMode.is_valid_mode('c'))

    def test_set_default_mode_valid(self):
        """Test if set default mode works as expected."""
        FileMode.set_default_mode(FileMode.READ)
        self.assertEqual(FileMode.get_default_mode(), 'r')

    def test_set_default_mode_invalid(self):
        """Test if set default mode raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            FileMode.set_default_mode(100)

    def test_set_default_mode_do_not_exist(self):
        """Test if set default mode raises ValueError when invalid inputs are provided."""
        with self.assertRaises(ValueError):
            FileMode.set_default_mode('c')


if __name__ == "__main__":
    unittest.main()
