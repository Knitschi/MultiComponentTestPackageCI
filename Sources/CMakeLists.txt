include("CPFCMake/cpfInitCIProject.cmake")

cmake_minimum_required (VERSION ${CPF_MINIMUM_CMAKE_VERSION}) 

project(MultiComponentTestPackageCI)

cpfAddPackages(GLOBAL_FILES "${CPF_ROOT_DIR}/conanfile.py")

