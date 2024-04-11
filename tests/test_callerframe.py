import inspect
import unittest

from pyloggermanager import CallerFrame


class TestCallerFrame(unittest.TestCase):
    """Unit test cases for CallerFrame class."""

    def test_init(self):
        """Test if init method is initialized."""
        caller_frame = CallerFrame()
        expected_class_name = 'Unknown Class'
        expected_file_name = 'Unknown File'
        expected_function_name = 'Unknown Function'
        expected_module_name = 'Unknown Module'
        expected_path_name = 'Unknown Path'
        self.assertEqual(caller_frame.class_name, expected_class_name)
        self.assertEqual(caller_frame.file_name, expected_file_name)
        self.assertEqual(caller_frame.function_name, expected_function_name)
        self.assertEqual(caller_frame.module_name, expected_module_name)
        self.assertEqual(caller_frame.path_name, expected_path_name)

    def test_get_caller_details_valid(self):
        """Test if the get caller details method works as expected with valid inputs."""
        caller_frame = CallerFrame.get_caller_details(inspect.currentframe())
        expected_class_name = 'TestCallerFrame'
        expected_file_name = 'test_callerframe'
        expected_function_name = 'test_get_caller_details_valid'
        expected_module_name = 'test_callerframe'
        expected_path_name = 'test_callerframe.py'
        self.assertEqual(caller_frame.class_name, expected_class_name)
        self.assertEqual(caller_frame.file_name, expected_file_name)
        self.assertEqual(caller_frame.function_name, expected_function_name)
        self.assertEqual(caller_frame.module_name, expected_module_name)
        assert caller_frame.path_name.endswith(expected_path_name)


if __name__ == "__main__":
    unittest.main()
