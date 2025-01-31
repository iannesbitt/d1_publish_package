# d1_publish_package
Add public read to all objects referenced by a metadata document

## Description

This tool is designed to facilitate the publishing of DataONE objects. It provides a command-line interface for users to easily add public read to the access policy of specified objects in repository.

## Requirements

- Python >3.9 <4.0 environment
- `dataone.common`
- `dataone.libclient`

## Installation

Clone the package from github, then use pip to install:

```bash
git clone https://github.com/iannesbitt/d1_publish_package
cd d1_publish_package
pip install .
```

## Configuration

You will need to set some configuration values so that this script will know where within DataONE to get and modify objects.
There are two main configuration files. Both will be located at `~/.config/d1_publish_package` within your home directory:

`.d1_token` - the DataONE token, which you will need to retrieve from your profile page once you're logged into the repository. For example, a Smithsonian user would get it from https://smithsonian.dataone.org/my-profile/s=settings/s=token, and a Test KNB user would get it from https://dev.nceas.ucsb.edu/my-profile/s=settings/s=token. The token should be pasted on the first line of this file with no other content.

`config.json` - The config file. Example config values are shown below.

Again for Smithsonian:
```json
{
    "rightsholder_orcid": "http://orcid.org/0000-0001-5828-6070",
    "write_groups": ["CN=smithsonian-curators,DC=dataone,DC=org"],
    "changePermission_groups": ["CN=smithsonian-admins,DC=dataone,DC=org"],
    "nodeid": "urn:node:SI",
    "mnurl": "https://smithsonian.dataone.org/metacat/d1/mn/",
    "cnurl": "https://cn.dataone.org/cn"
}
```

for CIB:
```json
{
    "rightsholder_orcid": "http://orcid.org/0000-0001-5828-6070",
    "write_groups": ["CN=cib-curators,DC=dataone,DC=org"],
    "changePermission_groups": ["CN=cib-admins,DC=dataone,DC=org"],
    "nodeid": "urn:node:CIB",
    "mnurl": "https://cib.dataone.org/metacat/d1/mn/",
    "cnurl": "https://cn.dataone.org/cn"
}
```

for the Test KNB:
```json
{
    "rightsholder_orcid": "http://orcid.org/0000-0001-5828-6070",
    "write_groups": [],
    "changePermission_groups": [],
    "nodeid": "urn:node:mnTestKNB",
    "mnurl": "https://dev.nceas.ucsb.edu/knb/d1/mn/",
    "cnurl": "https://cn-stage.test.dataone.org/cn"
}
```

## Operation

After [installing](#installation) using pip, you can use the `d1_publish_package` tool to set a PID or list of PIDs public. Use `d1_publish_package --help` to display help text.

```bash
d1_publish_package urn:uuid:f49edb4d-4b20-429b-9118-8b9b0d377ccc urn:uuid:1a5550b6-0319-4be2-892a-58ecfb29d7a0 urn:uuid:5580e89e-d0f3-4588-8b85-ed16b52c4fa9 resource_map_urn:uuid:75a07438-0523-4898-a67b-2c260cd5efff
```

**Note: if your dataset is initially private, don't forget to make your resource map public as well!**

_Todo: automate finding of package objects and making them all public with just one PID._

