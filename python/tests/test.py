import os, sys
import unittest

root_path = os.path.abspath(sys.path[0]).split("tests")[0]
src_path = os.path.join(root_path, "src")
sys.path.append(src_path)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
