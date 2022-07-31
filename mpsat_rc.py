# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.3.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00=\
#\
 mPSAT\x0d\x0aA (micro\
)plastic spectro\
scopy analyze to\
ol - mPSAT\x0d\x0a\
"

qt_resource_name = b"\
\x00\x08\
\x08\x91\xb8\xbe\
\x00m\
\x00a\x00r\x00k\x00d\x00o\x00w\x00n\
\x00\x09\
\x05\x91\xe8\x14\
\x00R\
\x00E\x00A\x00D\x00M\x00E\x00.\x00m\x00d\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x82L\xbd|{\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
