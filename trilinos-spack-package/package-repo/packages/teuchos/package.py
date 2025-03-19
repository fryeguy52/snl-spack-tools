# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import pathlib
import re
import sys

from spack.build_environment import dso_suffix
from spack.operating_systems.mac_os import macos_version
from spack.package import *
from spack.pkg.builtin.kokkos import Kokkos

class Teuchos(CMakePackage, CudaPackage, ROCmPackage):
    """The Trilinos Project is an effort to develop algorithms and enabling
    technologies within an object-oriented software framework for the solution
    of large-scale, complex multi-physics engineering and scientific problems.
    A unique design feature of Trilinos is its focus on packages.
    """

    homepage = "https://trilinos.org/"
    url = "https://github.com/trilinos/Trilinos/archive/refs/tags/trilinos-release-12-12-1.tar.gz"
    git = "https://github.com/trilinos/Trilinos.git"

    maintainers("keitat", "kuberry", "jfrye", "jwillenbring", "psakievich")

    # ###################### Versions ##########################

    version("master", branch="master")
    version("develop", branch="develop")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    # ###################### Variants ##########################
    variant("tests", default=False, description="Enable testing")
    variant("fortran", default=False, description="Enable fortran")
    variant("mpi", default=False, description="Enable mpi")
    variant("wrapper", default=False, description="use kokkos-nvcc-wrapper")
    
    # ######################### TPLs #############################
    depends_on("blas")
    depends_on("lapack")
    depends_on("kokkos")
    depends_on("kokkos-nvcc-wrapper", when="+wrapper")
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        args = [
            "-DTrilinos_ENABLE_Teuchos=ON",
            self.define_from_variant("Trilinos_ENABLE_TESTS", "tests"),
        ]

        return args

    
