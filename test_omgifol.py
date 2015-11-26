print('Omgifol Unit Tests')

import unittest, omg.colormap, omg


class TestColormap(unittest.TestCase):
    def setUp(self):
        self.col = omg.colormap.Colormap()

    def test_to_lump(self):
        lump = self.col.to_lump()
        self.assertTrue(lump is omg.Lump)


class TestLump(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")


class TestMapedit(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")


class TestPalette(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")


class TestPlaypal(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")


class TestTxdef(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")


class TestUtil(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")


class TestWad(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")


class TestWadio(unittest.TestCase):
    def setUp(self):
        print("farts")

    def test_farts(self):
        print("farts")

if __name__=="__main__":
    unittest.main(verbosity=2)