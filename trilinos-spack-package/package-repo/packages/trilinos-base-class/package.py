import os

from datetime import datetime

from spack.package import *

import llnl.util.filesystem as fs
import spack.store

class TrilinosBaseClass(CMakePackage, CudaPackage, ROCmPackage):
    """The Trilinos Project is an effort to develop algorithms and enabling
    technologies within an object-oriented software framework for the solution
    of large-scale, complex multi-physics engineering and scientific problems.
    A unique design feature of Trilinos is its focus on packages."""

    homepage = "https://trilinos.org/"
    url = "https://github.com/trilinos/Trilinos/archive/refs/tags/trilinos-release-12-12-1.tar.gz"
    git = "https://github.com/trilinos/Trilinos.git"

    maintainers("keitat", "kuberry", "jwillenbring", "psakievich", "jfrye")

    # ###################### Versions ##########################

    version("master", branch="master")
    version("develop", branch="develop")
    version("16.0.0", sha256="46bfc40419ed2aa2db38c144fb8e61d4aa8170eaa654a88d833ba6b92903f309")
    # ###################### Variants ##########################
    variant(
        "tests", default=False, description="Enable build of package's test executables"
    )

    variant(
        "cxxstd",
        values=("17", "20"),
        default="17",
        multi=False,
        description="C++ standard to use when building",
    )
    variant("tests", default=False, description="Enable testing")
    variant("fortran", default=False, description="Enable fortran")
    variant("mpi", default=False, description="Enable mpi")
    variant("wrapper", default=False, description="use kokkos-nvcc-wrapper")

    # ###################### Dependencies ##########################
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")
    depends_on("mpi", when="+mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("kokkos@4.3.01")
    depends_on("kokkos-nvcc-wrapper", when="+wrapper")

    
    git_sparse_paths = []

    def trilinos_base_cmake_args(self):
        args = []
        args.append("-DTPL_ENABLE_Kokkos=ON")
        args.append(self.define_from_variant("Trilinos_ENABLE_TESTS", "tests")),
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd")),
        
        if "^openblas" in self.spec:
            args.append(f"-DBLAS_LIBRARY_NAMES=openblas")
            args.append(f"-DLAPACK_LIBRARY_NAMES=openblas")

        return args
    
    def cmake_args(self):
        return []

#    def trilinos_dependency(package_name, self):

