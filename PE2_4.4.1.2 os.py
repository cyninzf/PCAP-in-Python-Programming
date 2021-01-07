# PE2
# 4.4.1.2 The os module
# The os module lets you interact with the operating system using Python.
# In addition to file and directory operations, the os module enables you to:
#             get information about the operating system;
#             manage processes;
#             operate on I/O streams using file descriptors.

import os
print(os.uname())


#             systemname — stores the name of the operating system;
#             nodename — stores the machine name on the network;
#             release — stores the operating system release;
#             version — stores the operating system version;
#             machine — stores the hardware identifier, e.g., x86_64.
