# UNIT testing with the pytest module

import sys
import pytest

class TestDoubleIt(object):

    def test_doubleit(self):
        assert myprogram.doubleit(10)==20

    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            myprogram.doubleit('hello')
