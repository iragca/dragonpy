# ---------------------------------------------------------------------
# Attribution
# ---------------------------------------------------------------------
# Portions of this module are derived from:
# https://github.com/fastapi/fastapi/blob/f5c6e9b4f9cadc1bf0f9a1fd672e621206b63007/fastapi/exceptions.py
# Copyright (c) 2018 Sebastián Ramírez, licensed under the MIT License.
#
# The following license text is retained as required by the upstream license:

# The MIT License (MIT)

# Copyright (c) 2018 Sebastián Ramírez

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class DragonPyError(RuntimeError):
    """
    A generic, DragonPy-specific error.
    """

    def __init__(self, message: str = ""):
        self.message = message

    def __str__(self) -> str:
        if self.message == "":
            return "DragonPy: Something unexpected happened"
        return f"DragonPy: {self.message}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(message={self.message!r})"


class DragonPyDeprecationWarning(UserWarning):
    """
    A custom deprecation warning as DeprecationWarning is ignored
    Ref: https://sethmlarson.dev/deprecations-via-warnings-dont-work-for-python-libraries
    """
