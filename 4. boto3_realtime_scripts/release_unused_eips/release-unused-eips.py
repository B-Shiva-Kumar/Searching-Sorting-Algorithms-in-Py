#  activate venv = boto3
# virtualenv venv-boto3
# venv-boto3\Scripts\activate

# install boto3
# pip install boto3

import boto3

# client = boto3.client('ec2', region_name="us-west-1")
client = boto3.client('ec2')
eipAddresses = client.describe_addresses()["Addresses"]
# print(eipAddresses) 
# print(eipAddresses["Addresses"])   # filter only Eip Addresses 

if eipAddresses != []:
    for eip in eipAddresses:
        # print(eip)
        if ("AssociationId" not in eip) and ("NetworkInterfaceId" not in eip):
            print(eip['PublicIp'] + " is unused, releasing...")
            client.release_address(AllocationId = eip['AllocationId'])
            print("Release Elastic-ip Succeeded!")

        else:
            print(eip["PublicIp"], " associated with EC2 server.")
else:
    # if eipAddresses outputs epmpty list []
    print("No elastic IPs found.")



# NOTE:
        # using lamda function will not show output
        # but provides output logs in cloudWatch - START and END logs.