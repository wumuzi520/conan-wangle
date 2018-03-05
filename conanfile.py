#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os
import shutil

class FollyConan(ConanFile):
    name = "wangle"
    version = "2018.02.26.00"
    release = "2018.02.26.00" # check contained cmakelists for version number
    description = "An open-source C++ library developed and used at Facebook"
    url = "https://github.com/wumuzi520/conan-wangle"
    homepage = "https://github.com/wumuzi520/wangle"
    license = "Apache 2.0"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "FindWangle.cmake"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False]
    }
    default_options = (
        "shared=False",
    )
    requires = (
        "gtest/1.8.0@ant/stable",
        "folly/2018.02.26.00@ant/stable"
    )
    

    def source(self):
        source_url = "https://github.com/wumuzi520/wangle"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.release))
        extracted_dir = self.name + "-" + self.release
        shutil.move(extracted_dir+"/"+self.name, self.name)
        shutil.rmtree(extracted_dir)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTS"] = False
        cmake.definitions["BUILD_EXAMPLES"] = False
        cmake.configure()
        return cmake
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("FindWangle.cmake", ".", ".")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if self.settings.os == "Linux":
            self.cpp_info.libs.extend(["pthread", "dl"])

        if not self.options.shared:
            if self.settings.compiler == "Visual Studio":
                self.cpp_info.libs.extend(["ws2_32", "Iphlpapi", "Crypt32"])
