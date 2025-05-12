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
from spack.pkg.trilinos.trilinos_base_class import depends_on_trilinos_package
from spack.pkg.trilinos.trilinos_base_class import trilinos_variant
from spack.pkg.trilinos.trilinos_base_class import list_of_trilinos_variants

class TrilinosThyra(TrilinosBaseClass):
    """The Trilinos Project is an effort to develop algorithms and enabling
    technologies within an object-oriented software framework for the solution
    of large-scale, complex multi-physics engineering and scientific problems.
    A unique design feature of Trilinos is its focus on packages.
    """

    maintainers("keitat", "kuberry", "jfrye", "jwillenbring", "psakievich")

    # ###################### Versions ##########################
    # Handled in TrilinosBaseClass
    
    # ###################### Variants ##########################

    
    # ######################### Conflicts #############################

    
    # ######################### TPLs #############################
    depends_on_trilinos_package("trilinos-rtop")
    depends_on_trilinos_package("trilinos-tpetra")

    def trilinos_package_cmake_args(self):
        args = [
        "-DTrilinos_ENABLE_Thyra=ON",
        "-DTPL_ENABLE_RTOp=ON",
        "-DTPL_ENABLE_Tpetra=ON",
        ]

        return args

    def cmake_args(self):
        args = []
        args.extend(self.trilinos_base_cmake_args())
        args.extend(self.trilinos_package_cmake_args())
        return args
