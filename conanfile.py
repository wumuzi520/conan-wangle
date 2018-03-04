#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class FollyConan(ConanFile):
    name = "folly"
    version = "0.58.0"
    release = "2018.02.26.00" # check contained cmakelists for version number
    description = "An open-source C++ library developed and used at Facebook"
    url = "https://github.com/bincrafters/conan-folly"
    homepage = "https://github.com/facebook/folly"
    license = "Apache 2.0"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    source_subfolder = "folly"
    build_subfolder = "build_subfolder"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False]
    }
    default_options = (
        "shared=False",
    )
    requires = (
        "gflags/2.2.1@ant/stable",
        "glog/0.3.5@ant/stable",
        "lzma/5.2.3@ant/stable",
        "double-conversion/3.0.0@ant/stable",
        "OpenSSL/1.0.2n@ant/stable",
        "zlib/1.2.11@ant/stable",
        "lz4/1.7.5@ant/stable",
        "Boost/1.65.0@ant/stable",
        "libevent/2.1.8@ant/stable"
    )
    

    def source(self):
        source_url = "https://github.com/facebook/folly"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.release))
        extracted_dir = self.name + "-" + self.release
        os.rename(extracted_dir, self.source_subfolder)
        to_be_replace = "\"\/build\/\""
        pattern = "\"\/%s\/build\/\"" % self.source_subfolder
        self.run("sed -i \"\" 's/%s/%s/' %s/CMakeLists.txt" % (to_be_replace, pattern, self.source_subfolder))

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.definitions["FOLLY_USE_LIBCPP"] = True
        cmake.definitions["FOLLY_HAVE_PTHREAD_ATFORK"] = True
        cmake.configure()
        return cmake
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if self.settings.os == "Linux":
            self.cpp_info.libs.extend(["pthread", "dl"])

        if not self.options.shared:
            if self.settings.compiler == "Visual Studio":
                self.cpp_info.libs.extend(["ws2_32", "Iphlpapi", "Crypt32"])
