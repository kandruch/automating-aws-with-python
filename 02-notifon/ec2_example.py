# coding: utf-8
import boto3
session = boto3.Session(profile_name='default')
session
ec2 = session.resource('ec2')
ec2
key_name
key_name = 'auto_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l auto_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l auto_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-0c6b1d09930fac512')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20190508-x86_64-gp2'
filters = [{'Name': 'name', 'Vaules': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instance
instances
instances
ec2.Instance(id='i-0252aa153d68d58c4')
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups()
inst.security_groups
inst.public_ip_address
# Look up the security group
#Autorize incoming connections from out public IP address. on port 22 (the port SSH uses)
sec_group = ec2.describe_security_groups(GroupIds=['sg-38213147'])
sec_group = inst.describe_security_groups(GroupIds=['sg-38213147'])
security_group = ec2.SecurityGroup('sg-38213147')
security_group
sg = security_group
sg
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges':[{'CidrIp': '24.226.120.5/32', 'Description': 'my-ip-address'}]}])
get_ipython().run_line_magic('history', '')
