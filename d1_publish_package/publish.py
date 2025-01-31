import d1_common.types
from d1_client.mnclient_2_0 import MemberNodeClient_2_0
import d1_common.types.dataoneTypes
import d1_common.types.exceptions
from .utils import add_public_access

def set_package_public(pid: str, client: MemberNodeClient_2_0):
    """
    Add public read to the access policies of objects in a list.

    This function uses a :py:mod:`d1_client.mnclient_2_0.MemberNodeClient_2_0`
    client to retrieve a list of objects associated with a metadata PID, and
    modifies their access policies to include the public read.
    """
    # Get a data package
    try:
        # Retrieve the system metadata for an object
        sysmeta: d1_common.types.dataoneTypes.AccessPolicy = client.getSystemMetadata(pid)
        # Modify the access policy
        sysmeta.accessPolicy = add_public_access(sysmeta=sysmeta)
        # Update the system metadata with the new access policy
        updated = client.updateSystemMetadata(pid, sysmeta)
        if updated == True:
            print(f'Updated.')
        else:
            print(f'Failed to update {pid}')
    except d1_common.types.exceptions.DataONEException as e:
        print(e)
