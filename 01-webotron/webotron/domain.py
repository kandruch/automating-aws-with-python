# -*- coding: utf-8 -*-

"""Classes for Route53 domains."""

class DomainManager:
	"""Manage a Route 53 domain."""
	
	def __init__(self, session):
		"""Create DomainManager object."""
		self.session = session
		self.client = self.session.client('route53')

# kittenweb.awscloudbuilder.com
# subdomain.kittenweb.awscloudbuilder.com
	def find_hosted_zone(self, domain_name):
		paginator = self.client.get_paginator('list_hosted_zones')
		for page in paginator.paginate():
			for zone in page['HostedZones']:
				if domain_name.endswith(zone['Name'][:-1]):
					return zone
		return None