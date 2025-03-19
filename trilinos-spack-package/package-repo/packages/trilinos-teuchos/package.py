# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import pathlib
import re
import sys

from spack.package import *
from spack.pkg.builtin.kokkos import Kokkos
from spack.pkg.trilinos.trilinos_base_class import TrilinosBaseClass

class TrilinosTeuchos(TrilinosBaseClass):
    """The Trilinos Project is an effort to develop algorithms and enabling
    technologies within an object-oriented software framework for the solution
    of large-scale, complex multi-physics engineering and scientific problems.
    A unique design feature of Trilinos is its focus on packages.
    """

    maintainers("jfrye")

    # ###################### Versions ##########################
    # Handled in TrilinosBaseClass

    # ###################### Variants ##########################

    # ######################### TPLs #############################

    def trilinos_package_cmake_args(self):
        args = [
        "-DTrilinos_ENABLE_Teuchos=ON",
        ]

        return args

    def cmake_args(self):
        args = []
        args.extend(self.trilinos_base_cmake_args())
        args.extend(self.trilinos_package_cmake_args())
        return args
