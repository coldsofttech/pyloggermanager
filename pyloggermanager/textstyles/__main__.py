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

class TextBackgroundColor:
    """
    Represents text background color for styling console text.
    Provides methods to add custom colors, retrieve color mappings, get color codes,
    and check if a color is valid.
    """

    # Standard color constants
    BLACK: str = "\033[40m"
    RED: str = "\033[41m"
    GREEN: str = "\033[42m"
    YELLOW: str = "\033[43m"
    BLUE: str = "\033[44m"
    MAGENTA: str = "\033[45m"
    CYAN: str = "\033[46m"
    WHITE: str = "\033[47m"

    # Dictionary mapping color codes to their corresponding names
    _color_to_name = {
        BLACK: 'BLACK',
        RED: 'RED',
        GREEN: 'GREEN',
        YELLOW: 'YELLOW',
        BLUE: 'BLUE',
        MAGENTA: 'MAGENTA',
        CYAN: 'CYAN',
        WHITE: 'WHITE'
    }

    # Dictionary mapping color names to their corresponding codes
    _name_to_color = {v: k for k, v in _color_to_name.items()}

    @classmethod
    def add_color(cls, name: str, code: str) -> None:
        """
        Adds a custom color with the provided name and code.

        :param name: Name of the color.
        :type name: str
        :param code: Color code.
        :type code: str
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('name should be a string.')
        elif not isinstance(code, str):
            raise TypeError('code should be a string.')

        cls._color_to_name[code] = name.upper()
        cls._name_to_color[name.upper()] = code

    @classmethod
    def get_colors(cls) -> dict:
        """
        Returns a dictionary mapping color names to their corresponding codes, sorted alphabetically.

        :return: Color mappings.
        :rtype: dict
        """
        return dict(sorted(cls._name_to_color.items()))

    @classmethod
    def get_color(cls, color_str: str) -> str:
        """
        Returns the color code for the provided color name or code string.

        :param color_str: Color name or code.
        :type color_str: str
        :return: Color code.
        :rtype: str
        """
        if not isinstance(color_str, str):
            raise TypeError('color_str should be a string.')

        color_str = repr(color_str) if color_str.startswith('\\') else color_str
        combined_colors = {**cls._color_to_name, **cls._name_to_color}
        result = combined_colors.get(color_str)
        if result is None:
            raise ValueError(f'TextBackgroundColor "{color_str}" is not a valid value.')
        return result

    @classmethod
    def is_valid_color(cls, color: str) -> bool:
        """
        Checks if the provided color name or code is valid.

        :param color: Color name or code.
        :type color: str
        :return: True if valid, False otherwise.
        :rtype: bool
        """
        if not isinstance(color, str):
            raise TypeError('color should be a string.')

        try:
            value = cls.get_color(color)
            if value is not None:
                return True
            else:
                return False
        except ValueError:
            return False

    @classmethod
    def remove_color(cls, name: str) -> None:
        """
        Removes the color mapping for the specified color name.

        :param name: The name of the color to remove.
        :type name: str
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('name should be a string.')

        color_code = cls._name_to_color.get(name.upper())
        if color_code is not None:
            del cls._color_to_name[color_code]
            del cls._name_to_color[name.upper()]
        else:
            raise ValueError(f'No mapping found for color name "{name}".')


class TextColor:
    """
    Represents text color for styling console text.
    Provides methods to add custom colors, retrieve color mappings, get color codes,
    and check if a color is valid.
    """

    # Standard color constants
    BLACK: str = "\033[30m"
    RED: str = "\033[31m"
    GREEN: str = "\033[32m"
    YELLOW: str = "\033[33m"
    BLUE: str = "\033[34m"
    MAGENTA: str = "\033[35m"
    CYAN: str = "\033[36m"
    WHITE: str = "\033[37m"

    # Dictionary mapping color codes to their corresponding names
    _color_to_name = {
        BLACK: 'BLACK',
        RED: 'RED',
        GREEN: 'GREEN',
        YELLOW: 'YELLOW',
        BLUE: 'BLUE',
        MAGENTA: 'MAGENTA',
        CYAN: 'CYAN',
        WHITE: 'WHITE'
    }

    # Dictionary mapping color names to their corresponding codes
    _name_to_color = {v: k for k, v in _color_to_name.items()}

    @classmethod
    def add_color(cls, name: str, code: str) -> None:
        """
        Adds a custom color with the provided name and code.

        :param name: Name of the color.
        :type name: str
        :param code: Color code.
        :type code: str
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('name should be a string.')
        elif not isinstance(code, str):
            raise TypeError('code should be a string.')

        cls._color_to_name[code] = name.upper()
        cls._name_to_color[name.upper()] = code

    @classmethod
    def get_colors(cls) -> dict:
        """
        Returns a dictionary mapping color names to their corresponding codes, sorted alphabetically.

        :return: Color mappings.
        :rtype: dict
        """
        return dict(sorted(cls._name_to_color.items()))

    @classmethod
    def get_color(cls, color_str: str) -> str:
        """
        Returns the color code for the provided color name or code string.

        :param color_str: Color name or code.
        :type color_str: str
        :return: Color code.
        :rtype: str
        """
        if not isinstance(color_str, str):
            raise TypeError('color_str should be a string.')

        color_str = repr(color_str) if color_str.startswith('\\') else color_str
        combined_colors = {**cls._color_to_name, **cls._name_to_color}
        result = combined_colors.get(color_str)
        if result is None:
            raise ValueError(f'TextColor "{color_str}" is not a valid value.')
        return result

    @classmethod
    def is_valid_color(cls, color: str) -> bool:
        """
        Checks if the provided color name or code is valid.

        :param color: Color name or code.
        :type color: str
        :return: True if valid, False otherwise.
        :rtype: bool
        """
        if not isinstance(color, str):
            raise TypeError('color should be a string.')

        try:
            value = cls.get_color(color)
            if value is not None:
                return True
            else:
                return False
        except ValueError:
            return False

    @classmethod
    def remove_color(cls, name: str) -> None:
        """
        Removes the color mapping for the specified color name.

        :param name: The name of the color to remove.
        :type name: str
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('name should be a string.')

        color_code = cls._name_to_color.get(name.upper())
        if color_code is not None:
            del cls._color_to_name[color_code]
            del cls._name_to_color[name.upper()]
        else:
            raise ValueError(f'No mapping found for color name "{name}".')


class TextEffect:
    """
    Represents different text effects used in text formatting, such as bold, underline, and italics.
    Provides methods to add custom text effects, get text effect mappings, check if a text effect
    is valid, and retrieve the corresponding text effect for a given string representation.
    """

    # Standard text effect constants
    BOLD: str = "\033[1m"
    UNDERLINE: str = "\033[4m"
    ITALIC: str = "\033[3m"

    # Dictionary mapping text effect codes to their corresponding names
    _effect_to_name = {
        BOLD: 'BOLD',
        UNDERLINE: 'UNDERLINE',
        ITALIC: 'ITALIC'
    }

    # Dictionary mapping text effect names to their corresponding codes
    _name_to_effect = {v: k for k, v in _effect_to_name.items()}

    @classmethod
    def add_effect(cls, name: str, code: str) -> None:
        """
        Adds a custom text effect with the provided name and code.

        :param name: Name of the text effect.
        :type name: str
        :param code: Code representing the text effect.
        :type code: str
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('name should be a string.')
        elif not isinstance(code, str):
            raise TypeError('code should be a string.')

        cls._effect_to_name[code] = name.upper()
        cls._name_to_effect[name.upper()] = code

    @classmethod
    def get_effects(cls) -> dict:
        """
        Returns a dictionary mapping text effect names to their corresponding codes, sorted alphabetically.

        :return: Text effect mappings.
        :rtype: dict
        """
        return dict(sorted(cls._name_to_effect.items()))

    @classmethod
    def get_effect(cls, effect_str: str) -> str:
        """
        Returns the text effect name corresponding to the given text effect code or name.

        :param effect_str: Text effect code or name.
        :type effect_str: str
        :return: Text effect name.
        :rtype: str
        """
        if not isinstance(effect_str, str):
            raise TypeError('effect_str should be a string.')

        effect_str = repr(effect_str) if effect_str.startswith('\\') else effect_str
        combined_effects = {**cls._effect_to_name, **cls._name_to_effect}
        result = combined_effects.get(effect_str)
        if result is None:
            raise ValueError(f'TextEffect "{effect_str}" is not a valid value.')
        return result

    @classmethod
    def is_valid_effect(cls, effect: str) -> bool:
        """
        Checks if the provided text effect is valid.

        :param effect: Text effect code or name.
        :type effect: str
        :return: True if valid, False otherwise.
        :rtype: bool
        """
        if not isinstance(effect, str):
            raise TypeError('effect should be a string.')

        try:
            value = cls.get_effect(effect)
            if value is not None:
                return True
            else:
                return False
        except ValueError:
            return False

    @classmethod
    def remove_effect(cls, name: str) -> None:
        """
        Removes the text effect mapping for the specified effect name.

        :param name: The name of the text effect to remove.
        :type name: str
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('name should be a string.')

        effect_code = cls._name_to_effect.get(name.upper())
        if effect_code is not None:
            del cls._effect_to_name[effect_code]
            del cls._name_to_effect[name.upper()]
        else:
            raise ValueError(f'No mapping found for text effect name "{name}".')
