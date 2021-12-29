include("CPFCMake/cpfInitCIProject.cmake")

cmake_minimum_required (VERSION ${CPF_MINIMUM_CMAKE_VERSION}) 

set( CPF_ENABLE_ABI_API_COMPATIBILITY_REPORT_TARGETS "OFF" CACHE BOOL "Enables targets that create ABI/API compatibility reports and checking." FORCE )

project(MultiComponentTestPackageCI)

cpfAddPackages(GLOBAL_FILES "${CPF_ROOT_DIR}/conanfile.py")

