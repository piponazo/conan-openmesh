from conans import ConanFile, CMake
import os

username = os.getenv("CONAN_USERNAME", "piponazo")
channel = os.getenv("CONAN_CHANNEL", "testing")

class GmpReuseConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "OpenMesh/4.1.1@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        if self.settings.os == "Windows":
            self.run(os.sep.join([".", "bin", "Release", "test"]))
        else:
            self.run(os.sep.join([".", "bin", "test"]))
