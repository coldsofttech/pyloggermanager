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

def pytest_collection_modifyitems(config, items):
    """
    Custom pytest hook to modify the collection of test items.
    This function sorts test items to execute specific tests first.
    """

    def test_order(test_name):
        # Define the desired order of execution for specific test names
        order_mapping = {
            'test_debug_valid': 1,
            'test_debug_invalid_message': 2,
            'test_debug_invalid_ignore_display': 3,
            'test_debug_invalid_exec_info': 4,
            'test_debug_invalid_stack_info': 5,
            'test_debug_invalid_stack_level': 6,
            'test_critical_valid': 7,
            'test_critical_invalid_message': 8,
            'test_critical_invalid_ignore_display': 9,
            'test_critical_invalid_exec_info': 10,
            'test_critical_invalid_stack_info': 11,
            'test_critical_invalid_stack_level': 12,
            'test_info_valid': 13,
            'test_info_invalid_message': 14,
            'test_info_invalid_ignore_display': 15,
            'test_info_invalid_exec_info': 16,
            'test_info_invalid_stack_info': 17,
            'test_info_invalid_stack_level': 18,
            'test_error_valid': 19,
            'test_error_invalid_message': 20,
            'test_error_invalid_ignore_display': 21,
            'test_error_invalid_exec_info': 22,
            'test_error_invalid_stack_info': 23,
            'test_error_invalid_stack_level': 24,
            'test_warning_valid': 25,
            'test_warning_invalid_message': 26,
            'test_warning_invalid_ignore_display': 27,
            'test_warning_invalid_exec_info': 28,
            'test_warning_invalid_stack_info': 29,
            'test_warning_invalid_stack_level': 30,
            'test_log_valid': 31,
            'test_log_invalid_level': 32,
            'test_log_invalid_message': 33,
            'test_log_invalid_ignore_display': 34,
            'test_log_invalid_exec_info': 35,
            'test_log_invalid_stack_info': 36,
            'test_log_invalid_stack_level': 37,
            'test_load_config_invalid_file_name': 38,
            'test_load_config_invalid_file_mode': 39,
            'test_load_config_invalid_level': 40,
            'test_load_config_invalid_format_str': 41,
            'test_load_config_invalid_date_format': 42,
            'test_load_config_invalid_stream': 43,
            'test_load_config_invalid_handlers': 44,
            'test_load_config_invalid_colorization': 45,
            'test_load_config_invalid_encoding': 46,
            'test_load_config_valid_file_name': 47,
            'test_load_config_valid_no_params': 48
        }
        return order_mapping.get(test_name, float('inf'))  # Default to infinity for tests not in the mapping

    items.sort(key=lambda item: (test_order(item.nodeid.split("::")[-1]), item.fspath, item.originalname))
