#
# Find WANGLE
#
#  WANGLE_INCLUDE_DIRS - where to find wangle/service/Service.h, etc.
#  WANGLE_LIBRARIES     - List of libraries when using libwangle.
#  WANGLE_FOUND       - True if libwangle found.

FIND_PATH(WANGLE_INCLUDE_DIRS wangle/service/Service.h)

FIND_LIBRARY(WANGLE_LIBRARIES NAMES wangle)

# handle the QUIETLY and REQUIRED arguments and set WANGLE_FOUND to TRUE if
# all listed variables are TRUE
INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WANGLE DEFAULT_MSG WANGLE_LIBRARIES WANGLE_INCLUDE_DIRS)

MARK_AS_ADVANCED(WANGLE_LIBRARIES WANGLE_INCLUDE_DIRS)

