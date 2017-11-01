################################################################################

# Libraries

import sys

import os

import boto3

import json

################################################################################



################################################################################

# Environment Varables

# Set the http-proxy variable. You only need one of these.  Use the 'iss' proxy on VPN

# Instantiate the class

#a = awslib()



################################################################################

# Call 'describe_instances' to get a 'dict' of information about the EC2 instances

#ec2instances = a.GetEC2Instances()

elb = boto3.client('elb')

################################################################################



################################################################################

# Call 'describe_instances' to get a 'dict' of information about the EC2 instances

elbinstances = elb.describe_load_balancers()

# Print Header

print("LoadBalancerName;App;")


################################################################################

# Here we loop through the 'dict' created from describe_instances

for elbdesc in elbinstances['LoadBalancerDescriptions']:


################################################################################

  # Load Balancer Name

  elb_name = "<LoadBalancerName is undefined>"

  if 'LoadBalancerName' in elbdesc:

   elb_name = elbdesc['LoadBalancerName']

##############################################################################

  elbtags = elb.describe_tags(LoadBalancerNames=[elb_name])

  for elbres in elbtags['TagDescriptions']:


##############################################################################

  # Tags

    tagname = '<Undefined Tag Name>'

  #tagowner = '<Undefined Tag owner>'

  #tagenv = '<Undefined Tag env>'

  #taguai = '<Undefined Tag UAI>'

  #tagapp = '<Undefined Tag app>'

  for tag in elbres['Tags']:

   if tag['Key'] == 'Name':

    tagname = tag['Value']

    continue

   #if tag['Key'] == 'owner':

    #tagowner = tag['Value']

    #continue

   #if tag['Key'] == 'env':

    #tagenv = tag['Value']

    #continue

   #if tag['Key'] == 'UAI':

    #taguai = tag['Value']

    #continue

   if tag['Key'] == 'Application':

    tagapp = tag['Value']

    continue

  ##############################################################################

  # Print

  print('%s;%s' % (elb_name, tagapp))