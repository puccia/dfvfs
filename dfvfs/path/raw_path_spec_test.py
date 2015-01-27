#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the RAW storage media image path specification implementation."""

import unittest

from dfvfs.path import raw_path_spec
from dfvfs.path import test_lib


class RawPathSpecTest(test_lib.PathSpecTestCase):
  """Tests for the RAW storage media image path specification implementation."""

  def testInitialize(self):
    """Tests the path specification initialization."""
    path_spec = raw_path_spec.RawPathSpec(parent=self._path_spec)

    self.assertNotEquals(path_spec, None)

    with self.assertRaises(ValueError):
      _ = raw_path_spec.RawPathSpec(parent=None)

    with self.assertRaises(ValueError):
      _ = raw_path_spec.RawPathSpec(parent=self._path_spec, bogus=u'BOGUS')

  def testComparable(self):
    """Tests the path specification comparable property."""
    path_spec = raw_path_spec.RawPathSpec(parent=self._path_spec)

    self.assertNotEquals(path_spec, None)

    expected_comparable = u'\n'.join([
        u'type: TEST',
        u'type: RAW',
        u''])

    self.assertEquals(path_spec.comparable, expected_comparable)


if __name__ == '__main__':
  unittest.main()
