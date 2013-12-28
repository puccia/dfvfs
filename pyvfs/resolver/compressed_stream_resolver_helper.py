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
"""The compressed stream path specification resolver helper implementation."""

# This is necessary to prevent a circular import.
import pyvfs.file_io.compressed_stream_io

from pyvfs.path import compressed_stream_path_spec
from pyvfs.resolver import resolver
from pyvfs.resolver import resolver_helper


class CompressedStreamResolverHelper(resolver_helper.ResolverHelper):
  """Class that implements the compressed stream resolver helper."""

  def __init__(self):
    """Initializes the resolver helper object."""
    super(CompressedStreamResolverHelper, self).__init__(
        compressed_stream_path_spec.CompressedStreamPathSpec.TYPE_INDICATOR)

  def OpenFileObject(self, path_spec):
    """Opens a file-like object defined by path specification.

    Args:
      path_spec: the VFS path specification (instance of path.PathSpec).

    Returns:
      The file-like object (instance of file_io.FileIO) or None if the path
      specification could not be resolved.
    """
    file_object = pyvfs.file_io.compressed_stream_io.CompressedStream()
    file_object.open(path_spec)
    return file_object

# Register the resolver helpers with the resolver.
resolver.Resolver.RegisterHelper(CompressedStreamResolverHelper())