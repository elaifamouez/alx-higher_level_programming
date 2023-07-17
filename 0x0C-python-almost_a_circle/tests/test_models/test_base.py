#!/usr/bin/python3
"""
Module for the uniitest of the class Base
"""
import models.base as b
import models.rectangle as r
import models.square as s
import unittest
import os


class TestBase(unittest.TestCase):
    """
    class TestBase
    """

    def test_module_doc(self):
        """
        Tests for the module doc
        """
        self.assertIsNotNone(b.__doc__)
        self.assertGreater(len(b.__doc__), 0)

    def test_class_doc(self):
        """
        Tests for the class doc
        """
        self.assertIsNotNone(b.Base.__doc__)
        self.assertGreater(len(b.Base.__doc__), 0)

    def test_method_doc(self):
        """
        Tests for the __init__ doc
        """
        self.assertIsNotNone(b.Base.__init__.__doc__)
        self.assertGreater(len(b.Base.__init__.__doc__), 0)

    def test_to_json_string_doc(self):
        """
        Tests for the to json string doc
        """
        self.assertIsNotNone(b.Base.to_json_string.__doc__)
        self.assertGreater(len(b.Base.to_json_string.__doc__), 0)

    def setUp(self):
        """
        Resets counter and create a temporary directory for test files
        """
        b.Base._Base__nb_objects = 0

    def test_base_id_incr(self):
        """
        Tests for for base id inctrementation
        """
        b1 = b.Base()
        b2 = b.Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_None(self):
        """
        Tests for None id
        """
        b1 = b.Base(None)
        b2 = b.Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_private_attribute(self):
        """
        Tests for private attributes
        """
        with self.assertRaises(AttributeError):
            b.Base(5).__nb_objects

    def test_id_True(self):
        """
        Tests id boolean
        """
        self.assertEqual(b.Base(True).id, True)

    def test_base_id_input(self):
        """
        Tests for id input
        """
        self.assertEqual(b.Base(89).id, 89)
        self.assertEqual(b.Base(-89).id, -89)
        self.assertEqual(b.Base(0).id, 0)

    def test_id_str(self):
        """
        Tests with str id
        """
        self.assertEqual(b.Base('Hola!').id, 'Hola!')

    def test_more_args(self):
        """
        Tests for too many args
        """
        with self.assertRaises(TypeError):
            b.Base(5, 10)

    def test_base_id_mix(self):
        """
        Tests for both
        """
        self.assertEqual(b.Base(89).id, 89)
        self.assertEqual(b.Base().id, 1)
        self.assertEqual(b.Base(0).id, 0)
        self.assertEqual(b.Base().id, 2)
        self.assertEqual(b.Base().id, 3)
        self.assertEqual(b.Base(-1).id, -1)
        self.assertEqual(b.Base(4).id, 4)

    def test_to_json_string_empty(self):
        """
        Tests for empty input
        """
        result = b.Base.to_json_string([])
        self.assertIsInstance(result, str)
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """
        Tests with none input
        """
        result = b.Base.to_json_string(None)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "[]")

    def test_to_json_string(self):
        """
        Test with 1 dictionary
        """
        dictionaries = r.Rectangle(10, 7, 2, 8).to_dictionary()
        expected = str(dictionaries)
        result = b.Base.to_json_string(dictionaries)
        self.assertIsInstance(result, str)
        self.assertEqual(eval(result), eval(expected))

    def test_to_json_strings(self):
        """
        Test with multiple dictionaries
        """
        d_list = []
        d_list.append(r.Rectangle(10, 7, 2, 8).to_dictionary())
        d_list.append(r.Rectangle(8, 4).to_dictionary())
        d_list.append(r.Rectangle(8, 4).to_dictionary())
        expected = str(d_list)
        result = b.Base.to_json_string(d_list)
        self.assertIsInstance(result, str)
        self.assertEqual(eval(result), eval(expected))

    def test_save_to_file_none(self):
        """
        Tests save to file with none with rectangle
        """
        r.Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_none_2(self):
        """
        Tests save to file with none with sqaure
        """
        s.Square.save_to_file(None)
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_empty_list(self):
        """
        Tests save to file with empty list with rectangle
        """
        r.Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_empty_list_2(self):
        """
        Tests save to file with none with sqaure
        """
        s.Square.save_to_file([])
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_1_inst_rec(self):
        """
        Tests save to file with 1 intsance of rectangle
        """
        obj = r.Rectangle(5, 3, 1, 6, 9)
        r.Rectangle.save_to_file([obj])
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        dictionary = obj.to_dictionary()
        self.assertEqual(file_contents, b.Base.to_json_string([dictionary]))

    def test_save_to_file_1_inst_squ(self):
        """
        Tests save to file with 1 intsance of square
        """
        obj = s.Square(3, 1, 6, 9)
        s.Square.save_to_file([obj])
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        dictionary = obj.to_dictionary()
        self.assertEqual(file_contents, b.Base.to_json_string([dictionary]))

    def test_save_to_file_multiple_rec(self):
        """
        Tests save to file with multiple instances of rectangle
        """
        d_list = []
        d_list.append(r.Rectangle(2, 1))
        d_list.append(r.Rectangle(55, 1, 0, 12, 98))
        d_list.append(r.Rectangle(2, 5, 13, 4))
        r.Rectangle.save_to_file(d_list)
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.setUp()
        r_list = []
        r_list.append(r.Rectangle(2, 1).to_dictionary())
        r_list.append(r.Rectangle(55, 1, 0, 12, 98).to_dictionary())
        r_list.append(r.Rectangle(2, 5, 13, 4).to_dictionary())
        self.assertEqual(file_contents, b.Base.to_json_string(r_list))

    def test_save_to_file_multiple_squ(self):
        """
        Tests save to file with multiple instances of square
        """
        d_list = []
        d_list.append(s.Square(2, 1))
        d_list.append(s.Square(1, 0, 12, 98))
        d_list.append(s.Square(2, 5, 13, 4))
        s.Square.save_to_file(d_list)
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.setUp()
        r_list = []
        r_list.append(s.Square(2, 1).to_dictionary())
        r_list.append(s.Square(1, 0, 12, 98).to_dictionary())
        r_list.append(s.Square(2, 5, 13, 4).to_dictionary())
        self.assertEqual(file_contents, b.Base.to_json_string(r_list))


if __name__ == "__main__":
    unittest.main()
