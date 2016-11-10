# - Try to find the Exiv2 library
#
# Once done this will define
#
#  OPENMESH_FOUND - system has libexiv2
#  OPENMESH_INCLUDE_DIR - the libexiv2 include directory
#  OPENMESH_LIBRARIES - Link these to use libexiv2
#  OPENMESH_DEFINITIONS - Compiler switches required for using libexiv2
#

find_path(OPENMESH_INCLUDE_DIR NAMES OpenMesh/Core/System/config.h PATHS ${CONAN_INCLUDE_DIRS_OPENMESH})
find_library(OPENMESH_CORE_LIB NAMES OpenMeshCore PATHS ${CONAN_LIB_DIRS_OPENMESH})
find_library(OPENMESH_TOOLS_LIB NAMES OpenMeshTools PATHS ${CONAN_LIB_DIRS_OPENMESH})

set(OPENMESH_FOUND TRUE)
set(OPENMESH_INCLUDE_DIRS ${OPENMESH_INCLUDE_DIR})
set(OPENMESH_LIBRARIES ${OPENMESH_CORE_LIB} ${OPENMESH_TOOLS_LIB})
mark_as_advanced(OPENMESH_LIBRARY OPENMESH_INCLUDE_DIR)
