#
# Find WANGLE
#
#  LIBWANGLE_INCLUDE_DIR - where to find wangle/service/Service.h, etc.
#  LIBWANGLE_LIBRARY     - List of libraries when using libwangle.
#  LIBWANGLE_FOUND       - True if libwangle found.

FIND_PATH(LIBWANGLE_INCLUDE_DIR wangle/service/Service.h)

FIND_LIBRARY(LIBWANGLE_LIBRARY NAMES wangle)

# handle the QUIETLY and REQUIRED arguments and set LIBWANGLE_FOUND to TRUE if
# all listed variables are TRUE
INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WANGLE DEFAULT_MSG LIBWANGLE_LIBRARY LIBWANGLE_INCLUDE_DIR)

MARK_AS_ADVANCED(LIBWANGLE_LIBRARY LIBWANGLE_INCLUDE_DIR)

