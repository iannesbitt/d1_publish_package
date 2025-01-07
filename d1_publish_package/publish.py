from datetime import datetime, timedelta
from d1_client.mnclient_2_0 import MemberNodeClient_2_0
from .utils import get_config, get_token, add_public_access

def set_package_public(pid):
    """
    Fix the access policies for objects uploaded in the last three days.

    This function uses a :py:mod:`d1_client.mnclient_2_0.MemberNodeClient_2_0`
    client to retrieve a list of objects uploaded in the last three days, and
    modifies their access policies to include the groups specified in the
    config document.
    """
    config = get_config()
    token = get_token()
    mnurl = config['mnurl']
    # Initialize the mn client
    options: dict = {
        "headers": {"Authorization": "Bearer " + token},
        "timeout_sec": 9999,
        }
    client: MemberNodeClient_2_0 = MemberNodeClient_2_0(mnurl, **options)
    # Get a data package
    object_list = client.getPackage(pid)
    # Loop through the objects in the package
    for obj in object_list.objectInfo:
        # Retrieve the system metadata for an object
        sysmeta = client.getSystemMetadata(obj.identifier.value())
        # Modify the access policy
        sysmeta.accessPolicy = add_public_access(sysmeta=sysmeta)
        # Update the system metadata with the new access policy
        client.updateSystemMetadata(obj.identifier.value(), sysmeta)
    client._session.close()
