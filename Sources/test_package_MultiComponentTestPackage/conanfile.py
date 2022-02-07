
from conans import ConanFile, tools, CMake

class TestPackage(object):

    python_requires = "CPFPackageTestConanfile/0.0.1@knitschi/development",
    python_requires_extend = "CPFPackageTestConanfile.CPFPackageTestConanfile",
    
    def init(self):

        self.cpf_conanfile_module = self.python_requires["CPFPackageTestConanfile"].module

        self.cpf_conanfile_module.init_impl(["MultiComponentTestPackage"])



