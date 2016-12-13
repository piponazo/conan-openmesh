from conans import ConanFile, tools, CMake
import os, sys

class OpenMeshConan(ConanFile):
    name = "OpenMesh"
    version = "6.3.0"
    settings = "os", "compiler", "build_type", "arch"
    description="Public recipe for OpenMesh"
    url="https://github.com/piponazo/conan-openmesh"
    exports = ["FindOpenMesh.cmake"]
    license="GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007"

    def source(self):
        self.run("git clone --depth 1 --branch OpenMesh-6.3 https://www.graphics.rwth-aachen.de:9000/OpenMesh/OpenMesh.git")

    def build(self):

        os.makedirs('OpenMesh/build')
        os.makedirs('OpenMesh/installFolder')

        cmake = CMake(self.settings)
        cmake_options = []
        cmake_options.append("CMAKE_BUILD_TYPE=%s" % self.settings.build_type)
        cmake_options.append("BUILD_APPS=OFF")
        cmake_options.append("CMAKE_INSTALL_PREFIX=%s" % self.package_folder)
        options = " -D".join(cmake_options)

        config_command = 'cd OpenMesh/build && cmake .. %s -D%s' % (cmake.command_line, options)
        self.output.warn(config_command)
        self.run(config_command)

        compile_command = "cd OpenMesh/build && cmake --build . %s" % cmake.build_config
        if self.settings.os != "Windows":
            n_cores = tools.cpu_count()
            compile_command = compile_command + " -- -j%s" % (n_cores)
        else:
            compile_command = compile_command + " --config %s" % (self.settings.build_type)
        self.output.warn(compile_command)
        self.run(compile_command)

        install_command = "cd OpenMesh/build && cmake --build . --target install"
        install_command = install_command + " --config %s" % (self.settings.build_type)
        self.output.warn(install_command)
        self.run(install_command)

    def package(self):
        self.copy("FindOpenMesh.cmake", ".", ".")

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = ['OpenMeshCore', 'OpenMeshTools']  # The libs to link against
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        self.cpp_info.resdirs = ['res']  # Directories where resources, data, etc can be found
