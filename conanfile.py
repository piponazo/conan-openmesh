from conans import ConanFile, tools, CMake
import os, sys

class ExivConan(ConanFile):
    name = "OpenMesh"
    version = "4.1.1"
    settings = "os", "compiler", "build_type", "arch"
    url="https://github.com/piponazo/conan-openmesh"
    exports = ["FindOpenMesh.cmake"]
    FOLDER_NAME = "openmesh_%s" % version.replace(".", "_")
    license="GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007"

    def source(self):
        url='https://bitbucket.org/pix4d/openmesh/get/4.1-patch-1.tar.bz2'
        zip_name = "%s.tar.bz2" % (self.FOLDER_NAME)
        self.output.info("Downloading %s..." % url)
        tools.download(url, zip_name)
        tools.unzip(zip_name, ".")
        os.remove(zip_name)
        os.rename("pix4d-openmesh-f84bca0b26c6", "openmesh")

    def build(self):

        os.makedirs('openmesh/build')
        os.makedirs('openmesh/installFolder')

        cmake = CMake(self.settings)
        cmake_options = []
        cmake_options.append("CMAKE_BUILD_TYPE=Release")
        cmake_options.append("BUILD_APPS=OFF")
        cmake_options.append("CMAKE_INSTALL_PREFIX=../installFolder")

        n_cores = tools.cpu_count()
        options = " -D".join(cmake_options)

        conf_command = 'cd openmesh/build && cmake .. %s -D%s' % (cmake.command_line, options)
        self.output.warn(conf_command)
        self.run(conf_command)
        compile_command = "cd openmesh/build && cmake --build . %s -- -j%s" % (cmake.build_config, n_cores)
        self.output.warn(compile_command)
        self.run(compile_command)
        self.run("cd openmesh/build && cmake --build . --target install")

    def package(self):
        self.copy("FindOpenMesh.cmake", ".", ".")
        self.copy("*",   dst="include", src="openmesh/installFolder/include")
        self.copy("*",     dst="lib",     src="openmesh/installFolder/lib")

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = ['OpenMeshCore', 'OpenMeshToolds']  # The libs to link against
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        self.cpp_info.resdirs = ['res']  # Directories where resources, data, etc can be found
