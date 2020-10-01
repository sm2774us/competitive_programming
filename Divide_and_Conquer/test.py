#!/usr/bin/env python

import unittest

if __name__ == "__main__":
    suite = unittest.TestLoader().discover(".", pattern="Solution*.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
