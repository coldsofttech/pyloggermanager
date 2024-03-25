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

import inspect
import io
import os
import sys
import unittest

from pyloggermanager import Logger, Manager, CallerFrame, Record
from pyloggermanager.formatters import DefaultFormatter
from pyloggermanager.handlers import FileHandler


class TestLogger(unittest.TestCase):
    """Unit test cases for Logger class."""
    maxDiff = None

    def setUp(self) -> None:
        self.logger = Logger(name='TestLogger')
        self.exec_info = (ValueError, ValueError('Test error'), None)
        self.caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        self.record = Record(
            message='Test error message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=self.caller_frame
        )

    def tearDown(self) -> None:
        for handler in self.logger.handlers:
            if issubclass(type(handler), FileHandler):
                try:
                    file_name = str(handler.filename)
                    os.remove(file_name)
                except (PermissionError, FileNotFoundError, IsADirectoryError):
                    pass
            else:
                handler.flush()
                handler.close()
        self.logger = Logger(name='TestLogger')

    def test_init_valid(self):
        """Test if init method is initialized properly."""
        logger = Logger(name='TestLogger')
        expected_name = 'TestLogger'
        expected_level = 20
        self.assertEqual(expected_name, logger.name)
        self.assertEqual(expected_level, logger.level)

    def test_init_invalid_name(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Logger(name=100)

    def test_init_invalid_level(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Logger(name='TestLogger', level='level')

    def test_cache_property_valid(self):
        """Test cache property"""
        self.logger.cache = {'level': 10}
        self.assertDictEqual({'level': 10}, self.logger.cache)

    def test_cache_property_invalid(self):
        """Test if cache property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.cache = 100

    def test_disabled_property_valid(self):
        """Test disabled property"""
        self.logger.disabled = False
        self.assertFalse(self.logger.disabled)

    def test_disabled_property_invalid(self):
        """Test if disabled property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.disabled = 100

    def test_handlers_property_valid(self):
        """Test handlers property"""
        self.logger.handlers = [FileHandler()]
        assert len(self.logger.handlers) > 0

    def test_handlers_property_invalid(self):
        """Test if handlers property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.handlers = 'handlers'

    def test_level_property_valid(self):
        """Test level property"""
        self.logger.level = 10
        self.assertEqual(10, self.logger.level)

    def test_level_property_invalid(self):
        """Test if level property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.level = 'level'

    def test_lock_name_property_valid(self):
        """Test lock name property"""
        self.logger.lock_name = 'lock'
        self.assertEqual('lock', self.logger.lock_name)

    def test_lock_name_property_invalid(self):
        """Test if lock name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.lock_name = 100

    def test_manager_property_valid(self):
        """Test manager property"""
        self.logger.manager = Manager(Logger(name='RootLogger'))
        assert isinstance(self.logger.manager, Manager)

    def test_manager_property_invalid(self):
        """Test if manager property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.manager = 'manager'

    def test_name_property_valid(self):
        """Test name property"""
        self.logger.name = 'TestLogger1'
        self.assertEqual('TestLogger1', self.logger.name)

    def test_name_property_invalid(self):
        """Test if name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.name = 100

    def test_parent_property_valid(self):
        """Test parent property"""
        self.logger.parent = Logger(name='ParentLogger')
        assert isinstance(self.logger.parent, Logger)

    def test_parent_property_invalid(self):
        """Test if parent property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.parent = 'manager'

    def test_root_property_valid(self):
        """Test root property"""
        self.logger.root = Logger(name='RootLogger')
        assert issubclass(type(self.logger.root), Logger)

    def test_root_property_invalid(self):
        """Test if root property raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.root = 'root'

    def test__is_internal_frame_valid(self):
        """Test is internal frame works as expected"""
        self.assertFalse(self.logger._is_internal_frame(inspect.currentframe()))

    def test__is_internal_frame_invalid(self):
        """Test if is internal frame raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger._is_internal_frame(100)

    def test__log_valid(self):
        """Test _log works as expected"""
        formatter = DefaultFormatter()
        handler = FileHandler(name='FileHandler')
        handler.formatter = formatter
        self.logger.add_handler(handler)
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        self.logger._log(20, 'Test message', False)
        sys.stdout = sys.__stdout__
        expected_output = ' :: INFO :: Test message'
        self.assertIn(expected_output, output_buffer.getvalue())

        with open(handler.filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output, file_content)

    def test__log_invalid_level(self):
        """Test if _log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger._log('level', 'Test message')

    def test__log_invalid_message(self):
        """Test if _log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger._log(20, 200)

    def test__log_invalid_ignore_display(self):
        """Test if _log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger._log(20, 'Test message', 200)

    def test__log_invalid_exec_info(self):
        """Test if _log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger._log(20, 'Test message', False, {'dict'})

    def test__log_invalid_stack_info(self):
        """Test if _log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger._log(
                20, 'Test message', False, self.exec_info, 200
            )

    def test__log_invalid_stack_level(self):
        """Test if _log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger._log(
                20, 'Test message', False, self.exec_info, True, 'level1'
            )

    def test_add_handler_valid(self):
        """Test if add handler works as expected"""
        handler = FileHandler(name='FileHandler')
        self.logger.add_handler(handler)
        assert len(self.logger.handlers) > 0

    def test_add_handler_invalid(self):
        """Test if add handler raises TypeError"""
        handler = 200
        with self.assertRaises(TypeError):
            self.logger.add_handler(handler)

    def test_call_handlers_valid(self):
        """Test if call handlers works as expected"""
        handler = FileHandler(name='FileHandler')
        self.logger.add_handler(handler)
        self.logger.call_handlers(self.record, False)

    def test_call_handlers_invalid(self):
        """Test if call handlers raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.call_handlers(200, False)

    def test_critical_valid(self):
        """Test if critical works as expected"""
        formatter = DefaultFormatter()
        handler = FileHandler()
        handler.formatter = formatter
        self.logger.add_handler(handler)
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        self.logger.critical('Test critical message', False)
        sys.stdout = sys.__stdout__
        expected_output = ' :: CRITICAL :: Test critical message'
        self.assertIn(expected_output, output_buffer.getvalue())

        with open(handler.filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output, file_content)

    def test_critical_invalid_message(self):
        """Test if critical raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.critical(200)

    def test_critical_invalid_ignore_display(self):
        """Test if critical raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.critical('Test message', ignore_display=200)

    def test_critical_invalid_exec_info(self):
        """Test if critical raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.critical('Test message', False, {'dict'})

    def test_critical_invalid_stack_info(self):
        """Test if critical raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.critical(
                'Test message', False, self.exec_info, 'dict'
            )

    def test_critical_invalid_stack_level(self):
        """Test if critical raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.critical(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )

    def test_debug_valid(self):
        """Test if debug works as expected"""
        formatter = DefaultFormatter()
        handler = FileHandler(level=10)
        handler.formatter = formatter
        self.logger.level = 10
        self.logger.add_handler(handler)
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        self.logger.debug('Test debug message', False)
        sys.stdout = sys.__stdout__
        expected_output_console = ''
        expected_output_file = ' :: DEBUG :: Test debug message'
        self.assertIn(expected_output_console, output_buffer.getvalue())

        with open(handler.filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output_file, file_content)

    def test_debug_invalid_message(self):
        """Test if debug raises TypeError"""
        self.logger.level = 10
        with self.assertRaises(TypeError):
            self.logger.debug(200)

    def test_debug_invalid_ignore_display(self):
        """Test if debug raises TypeError"""
        self.logger.level = 10
        with self.assertRaises(TypeError):
            self.logger.debug('Test message', ignore_display=200)

    def test_debug_invalid_exec_info(self):
        """Test if debug raises TypeError"""
        self.logger.level = 10
        with self.assertRaises(TypeError):
            self.logger.debug('Test message', False, {'dict'})

    def test_debug_invalid_stack_info(self):
        """Test if debug raises TypeError"""
        self.logger.level = 10
        with self.assertRaises(TypeError):
            self.logger.debug(
                'Test message', False, self.exec_info, 'dict'
            )

    def test_debug_invalid_stack_level(self):
        """Test if debug raises TypeError"""
        self.logger.level = 10
        with self.assertRaises(TypeError):
            self.logger.debug(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )

    def test_info_valid(self):
        """Test if info works as expected"""
        formatter = DefaultFormatter()
        handler = FileHandler()
        handler.formatter = formatter
        self.logger.add_handler(handler)
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        self.logger.info('Test info message', False)
        sys.stdout = sys.__stdout__
        expected_output = ' :: INFO :: Test info message'
        self.assertIn(expected_output, output_buffer.getvalue())

        with open(handler.filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output, file_content)

    def test_info_invalid_message(self):
        """Test if info raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.info(200)

    def test_info_invalid_ignore_display(self):
        """Test if info raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.info('Test message', ignore_display=200)

    def test_info_invalid_exec_info(self):
        """Test if info raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.info('Test message', False, {'dict'})

    def test_info_invalid_stack_info(self):
        """Test if info raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.info(
                'Test message', False, self.exec_info, 'dict'
            )

    def test_info_invalid_stack_level(self):
        """Test if info raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.info(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )

    def test_warning_valid(self):
        """Test if warning works as expected"""
        formatter = DefaultFormatter()
        handler = FileHandler()
        handler.formatter = formatter
        self.logger.add_handler(handler)
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        self.logger.warning('Test warning message', False)
        sys.stdout = sys.__stdout__
        expected_output = ' :: WARNING :: Test warning message'
        self.assertIn(expected_output, output_buffer.getvalue())

        with open(handler.filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output, file_content)

    def test_warning_invalid_message(self):
        """Test if warning raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.warning(200)

    def test_warning_invalid_ignore_display(self):
        """Test if warning raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.warning('Test message', ignore_display=200)

    def test_warning_invalid_exec_info(self):
        """Test if warning raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.warning('Test message', False, {'dict'})

    def test_warning_invalid_stack_info(self):
        """Test if warning raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.warning(
                'Test message', False, self.exec_info, 'dict'
            )

    def test_warning_invalid_stack_level(self):
        """Test if warning raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.warning(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )

    def test_error_valid(self):
        """Test if error works as expected"""
        formatter = DefaultFormatter()
        handler = FileHandler()
        handler.formatter = formatter
        self.logger.add_handler(handler)
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        self.logger.error('Test error message', False)
        sys.stdout = sys.__stdout__
        expected_output = ' :: ERROR :: Test error message'
        self.assertIn(expected_output, output_buffer.getvalue())

        with open(handler.filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output, file_content)

    def test_error_invalid_message(self):
        """Test if error raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.error(200)

    def test_error_invalid_ignore_display(self):
        """Test if error raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.error('Test message', ignore_display=200)

    def test_error_invalid_exec_info(self):
        """Test if error raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.error('Test message', False, {'dict'})

    def test_error_invalid_stack_info(self):
        """Test if error raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.error(
                'Test message', False, self.exec_info, 'dict'
            )

    def test_error_invalid_stack_level(self):
        """Test if error raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.error(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )

    def test_log_valid(self):
        """Test if log works as expected"""
        formatter = DefaultFormatter()
        handler = FileHandler()
        handler.formatter = formatter
        self.logger.add_handler(handler)
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        self.logger.log(20, 'Test info message', False)
        sys.stdout = sys.__stdout__
        expected_output = ' :: INFO :: Test info message'
        self.assertIn(expected_output, output_buffer.getvalue())

        with open(handler.filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output, file_content)

    def test_log_invalid_level(self):
        """Test if log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.log('level', 'Test message')

    def test_log_invalid_message(self):
        """Test if log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.log(20, ['Test message'])

    def test_log_invalid_ignore_display(self):
        """Test if log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.log(20, 'Test message', ignore_display=200)

    def test_log_invalid_exec_info(self):
        """Test if log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.log(20, 'Test message', False, {'dict'})

    def test_log_invalid_stack_info(self):
        """Test if log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.log(
                20, 'Test message', False, self.exec_info, 'dict'
            )

    def test_log_invalid_stack_level(self):
        """Test if log raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.log(
                20, 'Test message', False, self.exec_info,
                'StackInfo', 'level'
            )

    def test_find_caller_valid(self):
        """Test if the find caller works as expected"""
        caller_frame, stack_info = self.logger.find_caller(True)
        self.assertEqual('test_logger', caller_frame.file_name)
        self.assertEqual('TestLogger', caller_frame.class_name)
        self.assertEqual('test_find_caller_valid', caller_frame.function_name)
        self.assertEqual('test_logger', caller_frame.module_name)
        assert caller_frame.path_name.endswith('test_logger.py')
        self.assertIn('Stack (most recent call last):', stack_info)

    def test_find_caller_invalid_stack_info(self):
        """Test if the find caller raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.find_caller('stack info')

    def test_find_caller_invalid_stack_level(self):
        """Test if the find caller raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.find_caller(False, 'level')

    def test_get_child_valid(self):
        """Test if the get child works as expected"""
        root_logger = Logger(name='root')
        self.logger.name = 'child1'
        self.logger.root = root_logger
        child = self.logger.get_child('child2')
        self.assertEqual('child1.child2', child.name)

    def test_get_child_invalid(self):
        """Test if the get child raises TypeError"""
        root_logger = Logger(name='root')
        self.logger.name = 'child1'
        self.logger.root = root_logger
        with self.assertRaises(TypeError):
            self.logger.get_child(100)

    def test_get_effective_level(self):
        """Test if the get effective level works as expected"""
        self.assertEqual(20, self.logger.get_effective_level())

    def test_handle_valid(self):
        """Test if handle works as expected"""
        handler = FileHandler()
        formatter = DefaultFormatter()
        handler.formatter = formatter
        self.logger.add_handler(handler)
        self.logger.handle(self.record, False)

    def test_handle_invalid_record(self):
        """Test if handle raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.handle({'record'}, False)

    def test_handle_invalid_ignore_display(self):
        """Test if handle raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.handle(self.record, 100)

    def test_has_handlers_empty(self):
        """Test if the has handlers works as expected"""
        self.assertFalse(self.logger.has_handlers())

    def test_has_handlers_valid(self):
        """Test if the has handlers works as expected"""
        handler = FileHandler()
        formatter = DefaultFormatter()
        handler.formatter = formatter
        self.logger.add_handler(handler)
        self.assertTrue(self.logger.has_handlers())

    def test_is_enabled_for_disabled(self):
        """Test if is enabled for works as expected"""
        self.assertTrue(self.logger.is_enabled_for(20))
        self.assertFalse(self.logger.is_enabled_for(10))

    def test_is_enabled_for_enabled(self):
        """Test if is enabled for works as expected"""
        self.logger.disabled = True
        self.assertFalse(self.logger.is_enabled_for(20))

    def test_is_enabled_for_invalid(self):
        """Test if is enabled for raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.is_enabled_for('level')

    def test_make_record(self):
        """Test if the make record works as expected"""
        actual_record = self.logger.make_record(
            name=self.record.logger_name,
            level=self.record.level_number,
            message=self.record.message,
            caller_frame=self.caller_frame,
            exec_info=self.record.exec_info,
            stack_info=self.record.stack_info
        )
        actual_record_dict = actual_record.to_dict()
        expected_record_dict = self.record.to_dict()
        keys_to_ignore = ['time']
        actual_record_dict_filtered = {k: v for k, v in actual_record_dict.items() if k not in keys_to_ignore}
        expected_record_dict_filtered = {k: v for k, v in expected_record_dict.items() if k not in keys_to_ignore}
        self.assertDictEqual(expected_record_dict_filtered, actual_record_dict_filtered)

    def test_remove_handler_valid(self):
        """Test if remove handler works as expected"""
        handler = FileHandler(name='FileHandler')
        self.logger.add_handler(handler)
        self.logger.remove_handler(handler)
        assert len(self.logger.handlers) == 0

    def test_remove_handler_empty(self):
        """Test if remove handler works as expected"""
        self.logger.remove_handler(FileHandler())
        assert len(self.logger.handlers) == 0

    def test_remove_handler_invalid(self):
        """Test if remove handler raises TypeError"""
        with self.assertRaises(TypeError):
            self.logger.remove_handler({'handler'})


if __name__ == "__main__":
    unittest.main()
