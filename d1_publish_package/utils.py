from d1_common.types import dataoneTypes
from d1_common import const
import json
from pathlib import Path
from .defs import CONFIG_LOC


def get_token():
    """
    Get the DataONE token from the token file.
    Paste your auth token into ``{CONFIG_LOC}/.d1_token``.

    :return: The DataONE token.
    :rtype: str
    """
    # Set the D1 token
    with open(Path(CONFIG_LOC / '.d1_token'), 'r') as tf:
        return tf.read().split('\n')[0]


def get_config():
    """
    Config values not including the DataONE token are stored in
    ``{CONFIG_LOC}/config.json``.

    :return: The ORCID, node identifier, Member Node URL, and metadata JSON file.
    :rtype: tuple
    """
    global CN_URL
    global CONFIG
    # Set your ORCID
    CONFIG_F = CONFIG_LOC.joinpath('config.json')
    with open(CONFIG_F, 'r') as lc:
        config = json.load(lc)
    CONFIG = config
    # set the data root and CN URL
    CN_URL = config['cnurl'] if config.get('cnurl') else CN_URL
    return config


def generate_access_policy():
    """
    Creates the access policy for the object. Note that the permission is set to 'read'.
    
    :return: The access policy.
    :rtype: dataoneTypes.accessPolicy
    """
    accessPolicy = dataoneTypes.accessPolicy()
    accessRule = dataoneTypes.AccessRule()
    accessRule.subject.append(const.SUBJECT_PUBLIC)
    permission = dataoneTypes.Permission('read')
    accessRule.permission.append(permission)
    accessPolicy.append(accessRule)
    accessRule = dataoneTypes.AccessRule()
    config = get_config()
    if config.get('write_groups'):
        for group in config.get('write_groups'):
            writeGroup = dataoneTypes.Subject(group)
            accessRule.subject.append(writeGroup)
            permission = dataoneTypes.Permission('write')
            accessRule.permission.append(permission)
            accessPolicy.append(accessRule)
    if config.get('changePermission_groups'):
        for group in config.get('changePermission_groups'):
            changePermissionGroup = dataoneTypes.Subject(group)
            accessRule.subject.append(changePermissionGroup)
            permission = dataoneTypes.Permission('changePermission')
            accessRule.permission.append(permission)
            accessPolicy.append(accessRule)
    return accessPolicy


def add_public_access(sysmeta):
    """
    Adds public access to the access policy.
    
    :param sysmeta: The system metadata.
    :type sysmeta: dataoneTypes.systemMetadata
    :return: The access policy with public access.
    :rtype: dataoneTypes.accessPolicy
    """
    accessPolicy = sysmeta.accessPolicy
    accessRule = dataoneTypes.AccessRule()
    accessRule.subject.append(const.SUBJECT_PUBLIC)
    permission = dataoneTypes.Permission('read')
    accessRule.permission.append(permission)
    accessPolicy.append(accessRule)
    return accessPolicy
