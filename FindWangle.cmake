#
# Find WANGLE
#
#  WANGLE_INCLUDE_DIR - where to find wangle/service/Service.h, etc.
#  WANGLE_LIBRARY     - List of libraries when using libwangle.
#  WANGLE_FOUND       - True if libwangle found.

FIND_PATH(WANGLE_INCLUDE_DIR wangle/service/Service.h)

FIND_LIBRARY(WANGLE_LIBRARY NAMES wangle)

# handle the QUIETLY and REQUIRED arguments and set WANGLE_FOUND to TRUE if
# all listed variables are TRUE
INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WANGLE DEFAULT_MSG WANGLE_LIBRARY WANGLE_INCLUDE_DIR)

MARK_AS_ADVANCED(WANGLE_LIBRARY WANGLE_INCLUDE_DIR)

