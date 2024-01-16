#!/usr/bin/python3

"""This is Console Test Module."""

import json
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class TestConsole(unittest.TestCase):
    """Implement Unittest for the console."""

    def test_help(self):
        """Test the help method."""
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, f.getvalue())

    def test_empty_line(self):
        """Test empty line method."""
        expected = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(expected, f.getvalue())

    def test_quit(self):
        """Test quit method."""
        expected = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(expected, f.getvalue())

    def test_eof(self):
        """Test quit method."""
        expected = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(expected, f.getvalue())

    def test_create_without_model_fail(self):
        """Test if create without model fails."""
        expected = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(expected, f.getvalue())
