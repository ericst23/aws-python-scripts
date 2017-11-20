################################################################################

# Libraries

import sys

import os

import boto3

import json
################################################################################



################################################################################

# Environment Varables

# Set the http-proxy variable. You only need one of these.  Use the proxy on VPN

# Instantiate the class

#a = awslib()



################################################################################

# Call 'describe_instances' to get a 'dict' of information about the EC2 instances

#ec2instances = a.GetEC2Instances()

rds = boto3.client('rds')

################################################################################



################################################################################

# Call 'describe_instances' to get a 'dict' of information about the EC2 instances

rdssnapshots = rds.describe_db_snapshots()



# Print Header

print("DBSnapshotIdentifier;Engine;StorageType;AllocatedStorage;SnapshotType")



################################################################################

# Here we loop through the 'dict' created from db_snapshots

for rdssnap in rdssnapshots['DBSnapshots']:


################################################################################

  # Print

  print(rdssnap['DBSnapshotIdentifier']
  + ';%s' % rdssnap['Engine']
  + ';%s' % rdssnap['StorageType']
  + ';%s' % rdssnap['AllocatedStorage']
  + ';%s' % rdssnap['SnapshotType']
  )
