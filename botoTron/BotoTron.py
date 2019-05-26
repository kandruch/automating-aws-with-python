#!/usr/bin/python
# -*- coding: utf-8 -*-

"""BotoTron: Retrieve AWS Information on select services.

BotoTron automates the process of retriving AWS information
- List EC2 instance details
"""

import boto3
import click
from termcolor import colored


# session = boto3.Session(profile_name='default')
ec2resource = boto3.resource('ec2')

@click.group()
@click.option('--profile', default=None,
				help="Use a given AWS profile.")
def cli(profile):
    """Retrieve EC2 server data from AWS."""
    global session
    
    session_cfg = {}
    if profile:
    	session_cfg['profile_name'] = profile

# @cli.command('list-running-ec2')
# def list_running_ec2():
#     """List EC2 instance ids and public ip addresses."""
#     instances = ec2resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
#     for instance in instances:
#         print(
#         	"Instance" + ' ' + instance.id, 
#         	"Type" + ' ' + instance.instance_type,
#         	"PublicIP" + ' ' + instance.public_ip_address,
#         	"PrivateIP" + ' ' + instance.private_ip_address)


@cli.command('all-ec2-data')
def get_all_ec2_data():
    """Get All EC2 Data."""
    for i in ec2resource.instances.all():

        print("############################################")
        print("#            CONSOLE OUTPUT                #")
        print("############################################")
        
        print("Id: {0}\tState: {1}\tLaunched: {2}\tRoot Device Name: {3}".format(
            colored(i.id, 'cyan'),
            colored(i.state['Name'], 'green'),
            colored(i.launch_time, 'cyan'),
            colored(i.root_device_name, 'cyan')
        ))
    
        print("\tArch: {0}\tHypervisor: {1}".format(
            colored(i.architecture, 'cyan'),
            colored(i.hypervisor, 'cyan')
        ))
    
        print("\tPriv. IP: {0}\tPub. IP: {1}".format(
            colored(i.private_ip_address, 'red'),
            colored(i.public_ip_address, 'green')
        ))
    
        print("\tPriv. DNS: {0}\tPub. DNS: {1}".format(
            colored(i.private_dns_name, 'red'),
            colored(i.public_dns_name, 'green')
        ))
    
        print("\tSubnet: {0}\tSubnet Id: {1}".format(
            colored(i.subnet, 'cyan'),
            colored(i.subnet_id, 'cyan')
        ))
    
        print("\tKernel: {0}\tInstance Type: {1}".format(
            colored(i.kernel_id, 'cyan'),
            colored(i.instance_type, 'cyan')
        ))
    
        print("\tRAM Disk Id: {0}\tAMI Id: {1}\tPlatform: {2}\t EBS Optimized: {3}".format(
            colored(i.ramdisk_id, 'cyan'),
            colored(i.image_id, 'cyan'),
            colored(i.platform, 'cyan'),
            colored(i.ebs_optimized, 'cyan')
        ))
    
        print("\tBlock Device Mappings:")
        for idx, dev in enumerate(i.block_device_mappings, start=1):
            print("\t- [{0}] Device Name: {1}\tVol Id: {2}\tStatus: {3}\tDeleteOnTermination: {4}\tAttachTime: {5}".format(
                idx,
                colored(dev['DeviceName'], 'cyan'),
                colored(dev['Ebs']['VolumeId'], 'cyan'),
                colored(dev['Ebs']['Status'], 'green'),
                colored(dev['Ebs']['DeleteOnTermination'], 'cyan'),
                colored(dev['Ebs']['AttachTime'], 'cyan')
            ))
    
        print("\tTags:")
        for idx, tag in enumerate(i.tags, start=1):
            print("\t- [{0}] Key: {1}\tValue: {2}".format(
                idx,
                colored(tag['Key'], 'cyan'),
                colored(tag['Value'], 'cyan')
            ))
    
        print("\tProduct codes:")
        for idx, details in enumerate(i.product_codes, start=1):
            print("\t- [{0}] Id: {1}\tType: {2}".format(
                idx,
                colored(details['ProductCodeId'], 'cyan'),
                colored(details['ProductCodeType'], 'cyan')
            ))
    
        # print("DATA:")
        print("")
        # Commented out because this creates a lot of clutter..
        # print(i.console_output()['Output'])
    
        # print("############################################")
        # print("#            CONSOLE OUTPUT                #")
        # print("############################################")
    
if __name__ == '__main__':
    cli()
