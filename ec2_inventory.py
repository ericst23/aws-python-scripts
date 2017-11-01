################################################################################

# Libraries

import sys

import os

import boto3

################################################################################



################################################################################

# Environment Varables

# Set the http-proxy variable. You only need one of these.  Use the 'iss' proxy on VPN

# Instantiate the class

#a = awslib()



################################################################################

# Call 'describe_instances' to get a 'dict' of information about the EC2 instances

#ec2instances = a.GetEC2Instances()

ec2 = boto3.client('ec2')

################################################################################



################################################################################

# Call 'describe_instances' to get a 'dict' of information about the EC2 instances

ec2instances = ec2.describe_instances()



# Print Header

print("InstanceId;Type;State;IP Name;IP Addr;AZ;Name;App;ENV;UAI;Owner;Platform;ImageId;")



################################################################################

# Here we loop through the 'dict' created from describe_instances

for ec2res in ec2instances['Reservations']:

 for ec2ins in ec2res['Instances']:

  ##############################################################################

  # InstanceId

  inst_id = "<InstanceId is undefined>"

  if 'InstanceId' in ec2ins:

   inst_id = ec2ins['InstanceId']

  ##############################################################################

  # InstanceType

  inst_type = "<InstanceType is undefined>"

  if 'InstanceType' in ec2ins:

   inst_type = ec2ins['InstanceType']

  ##############################################################################

  # State

  inst_state = "<InstanceState is undefined>"

  if 'State' in ec2ins:

   inst_state = ec2ins['State']['Name']

  ##############################################################################

  # IpName

  inst_priname = "<PrivateDnsName is undefined>"

  if 'PrivateDnsName' in ec2ins:

   inst_priname = ec2ins['PrivateDnsName']

  ##############################################################################

  # IpAddr

  inst_priaddr = "<PrivateIpAddress is undefined>"

  if 'PrivateIpAddress' in ec2ins:

   inst_priaddr = ec2ins['PrivateIpAddress']

  ##############################################################################

  # AZ

  inst_az = "<InstanceAZ is undefined>"

  if 'Placement' in ec2ins:

   inst_az = ec2ins['Placement']['AvailabilityZone']

  ##############################################################################

  # EBS Volumes

  volumes = ''

  for v in ec2ins['BlockDeviceMappings']:

   volumes += ';' + v['Ebs']['VolumeId']

  ##############################################################################

  # Platform

  platform = "linux"

  if 'Platform' in ec2ins:

   platform = ec2ins['Platform']

  ##############################################################################

  # Tags

  tagname = '<Undefined Tag Name>'

  tagowner = '<Undefined Tag owner>'

  tagenv = '<Undefined Tag env>'

  taguai = '<Undefined Tag UAI>'

  tagapp = '<Undefined Tag app>'

  for tag in ec2ins['Tags']:

   if tag['Key'] == 'Name':

    tagname = tag['Value']

    continue

   if tag['Key'] == 'owner':

    tagowner = tag['Value']

    continue

   if tag['Key'] == 'env':

    tagenv = tag['Value']

    continue

   if tag['Key'] == 'UAI':

    taguai = tag['Value']

    continue

   if tag['Key'] == 'app':

    tagapp = tag['Value']

    continue

  ##############################################################################

  # Print

  print('%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s' % (inst_id, inst_type, inst_state, 

         inst_priname, inst_priaddr, inst_az, 

         tagname, tagapp, tagenv, taguai, platform, tagowner))