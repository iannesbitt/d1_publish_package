from pathlib import Path

CONFIG = {
    "rightsholder_orcid": "http://orcid.org/0000-0001-5828-6070",
    "write_groups": ["CN=Test_Group,DC=dataone,DC=org"],
    "changePermission_groups": ["CN=Test_Group,DC=dataone,DC=org"],
    "nodeid": "urn:node:mnTestKNB",
    "mnurl": "https://dev.nceas.ucsb.edu/knb/d1/mn/",
    "cnurl": "https://cn-stage.test.dataone.org/cn"
}
"""
The configuration dictionary. These values are read from the config file.
Defaults to the values above but should be set appropriately in the config file.
"""

CONFIG_LOC = Path('~/.config/d1_publish_package/').expanduser().absolute()
"""
The location of the configuration file.
Defaults to ``~/.config/d1_publish_package/``.
"""
