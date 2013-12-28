#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2013 The PyVFS Project Authors.
# Please see the AUTHORS file for details on individual authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the text file interface for file-like objects."""

import os
import unittest

from pyvfs.file_io import os_file_io
from pyvfs.helpers import text_file
from pyvfs.path import os_path_spec


class TextFileTest(unittest.TestCase):
  """The unit test for the text file object."""

  def setUp(self):
    """Sets up the needed objects used throughout the test."""
    test_file = os.path.join('test_data', 'another_file')
    self._os_path_spec1 = os_path_spec.OSPathSpec(location=test_file)

    test_file = os.path.join('test_data', 'password.txt')
    self._os_path_spec2 = os_path_spec.OSPathSpec(location=test_file)

  def testReadline(self):
    """Test the readline() function."""
    file_object = os_file_io.OSFile()
    file_object.open(self._os_path_spec1)
    text_file_object = text_file.TextFile(file_object)

    self.assertEquals(text_file_object.readline(), 'This is another file.\n')

    self.assertEquals(text_file_object.get_offset(), 22)

    file_object.close()

  def testReadlines(self):
    """Test the readlines() function."""
    file_object = os_file_io.OSFile()
    file_object.open(self._os_path_spec2)
    text_file_object = text_file.TextFile(file_object)

    lines = text_file_object.readlines()

    self.assertEquals(len(lines), 5)
    self.assertEquals(lines[0], 'place,user,password\n')
    self.assertEquals(lines[1], 'bank,joesmith,superrich\n')
    self.assertEquals(lines[2], 'alarm system,-,1234\n')
    self.assertEquals(lines[3], 'treasure chest,-,1111\n')
    self.assertEquals(lines[4], 'uber secret laire,admin,admin\n')

    file_object.close()

  def testReadlinesWithSizeHint(self):
    """Test the readlines() function."""
    file_object = os_file_io.OSFile()
    file_object.open(self._os_path_spec2)
    text_file_object = text_file.TextFile(file_object)

    lines = text_file_object.readlines(sizehint=60)

    self.assertEquals(len(lines), 3)
    self.assertEquals(lines[0], 'place,user,password\n')
    self.assertEquals(lines[1], 'bank,joesmith,superrich\n')
    self.assertEquals(lines[2], 'alarm system,-,1234\n')

    file_object.close()

  def testIterator(self):
    """Test the iterator functionality."""
    file_object = os_file_io.OSFile()
    file_object.open(self._os_path_spec2)
    text_file_object = text_file.TextFile(file_object)

    lines = []
    for line in text_file_object:
      lines.append(line)

    self.assertEquals(len(lines), 5)
    self.assertEquals(lines[0], 'place,user,password\n')
    self.assertEquals(lines[1], 'bank,joesmith,superrich\n')
    self.assertEquals(lines[2], 'alarm system,-,1234\n')
    self.assertEquals(lines[3], 'treasure chest,-,1111\n')
    self.assertEquals(lines[4], 'uber secret laire,admin,admin\n')

    file_object.close()


if __name__ == '__main__':
  unittest.main()