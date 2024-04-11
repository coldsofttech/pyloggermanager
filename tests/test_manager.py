import inspect
import os
import unittest

from pyloggermanager import Logger, RootLogger, Manager, CallerFrame, Record
from pyloggermanager.handlers import FileHandler


class TestManager(unittest.TestCase):
    """Unit test cases for Manager class"""

    def setUp(self) -> None:
        self.logger = Logger(name='logger')
        self.root_logger = RootLogger(level=20)
        self.manager = Manager(self.logger)
        self.caller_frame = CallerFrame.get_caller_details(inspect.currentframe())
        self.record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=20,
            caller_frame=self.caller_frame,
            exec_info=(ValueError, ValueError('Test error'), None)
        )

    def tearDown(self) -> None:
        try:
            for handler in self.manager.logger_class.handlers:
                if isinstance(type(handler), FileHandler):
                    try:
                        file_name = str(handler.filename)
                        os.remove(file_name)
                    except (PermissionError, FileNotFoundError, IsADirectoryError):
                        pass

                handler.flush()
                handler.close()
        except AttributeError:
            pass
        finally:
            self.manager.clear_cache()

    def test_init_valid(self):
        """Test if init method initializes properly"""
        self.assertEqual(self.logger, self.manager.root)
        self.assertEqual(0, self.manager.disable)
        self.assertEqual(None, self.manager.logger_class)
        self.assertEqual(None, self.manager.record_factory)

    def test_init_valid_root_logger(self):
        """Test if init method initializes properly"""
        self.manager = Manager(self.root_logger)
        self.assertEqual(self.root_logger, self.manager.root)
        self.assertEqual(0, self.manager.disable)
        self.assertEqual(None, self.manager.logger_class)
        self.assertEqual(None, self.manager.record_factory)

    def test_init_invalid(self):
        """Test if init raises TypeError"""
        with self.assertRaises(TypeError):
            Manager('logger')

    def test_disable_property_valid(self):
        """Test disable property"""
        self.manager.disable = 20
        self.assertEqual(20, self.manager.disable)

    def test_disable_property_invalid(self):
        """Test if disable property raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.disable = 'INFO'

    def test_lock_name_property_valid(self):
        """Test lock name property"""
        self.manager.lock_name = 'test_lock'
        self.assertEqual('test_lock', self.manager.lock_name)

    def test_lock_name_property_invalid(self):
        """Test if lock name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.lock_name = 100

    def test_logger_class_property_valid(self):
        """Test logger class property"""
        logger = Logger(name='testlogger')
        self.manager.logger_class = logger
        self.assertEqual(logger, self.manager.logger_class)

    def test_logger_class_property_valid_root_logger(self):
        """Test logger class property"""
        self.manager.logger_class = self.root_logger
        self.assertEqual(self.root_logger, self.manager.logger_class)

    def test_logger_class_property_invalid(self):
        """Test if logger class raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.logger_class = 100

    def test_logger_dict_property_valid(self):
        """Test logger dict property"""
        self.manager.logger_dict = {'RootLogger': self.root_logger}
        self.assertDictEqual({'RootLogger': self.root_logger}, self.manager.logger_dict)

    def test_logger_dict_property_invalid(self):
        """Test if logger dict raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.logger_dict = 100

    def test_record_factory_property_valid(self):
        """Test record factory property"""
        self.manager.record_factory = self.record
        self.assertEqual(self.record, self.manager.record_factory)

    def test_record_factory_property_invalid(self):
        """Test if record factory raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.record_factory = 100

    def test_root_property_valid(self):
        """Test root property"""
        logger = Logger(name='rootlogger')
        self.manager.root = logger
        self.assertEqual(logger, self.manager.root)

    def test_root_property_valid_root_logger(self):
        """Test root property"""
        self.manager.root = self.root_logger
        self.assertEqual(self.root_logger, self.manager.root)

    def test_root_property_invalid(self):
        """Test if root property raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.root = 100

    def test_clear_cache(self):
        """Test if clear cache works as expected"""
        self.manager.clear_cache()

    def test_get_logger_valid(self):
        """Test if the get logger works as expected"""
        root_logger = Logger(name='rootlogger')
        child_logger = root_logger.get_child(suffix='childlogger')
        self.assertIn('rootlogger.childlogger', child_logger.manager.logger_dict.keys())
        self.assertIn('rootlogger', child_logger.manager.logger_dict.keys())

        self.manager.logger_class = child_logger
        self.assertEqual(child_logger, self.manager.get_logger('childlogger'))

    def test_get_logger_valid_root_logger(self):
        """Test if the get logger works as expected"""
        root_logger = RootLogger(20)
        self.manager.logger_class = root_logger
        self.assertEqual(root_logger, self.manager.get_logger('root'))

    def test_get_logger_invalid(self):
        """Test if the get logger raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.get_logger(100)

    def test_set_logger_valid(self):
        """Test if set logger works as expected"""
        logger = Logger(name='newlogger')
        self.manager.set_logger(logger)
        self.assertEqual(logger, self.manager.logger_class)

    def test_set_logger_valid_root_logger(self):
        """Test if set logger works as expected"""
        self.manager.set_logger(self.root_logger)
        self.assertEqual(self.root_logger, self.manager.logger_class)

    def test_set_logger_invalid(self):
        """Test if set logger raises TypeError"""
        with self.assertRaises(TypeError):
            self.manager.set_logger(100)


if __name__ == "__main__":
    unittest.main()
