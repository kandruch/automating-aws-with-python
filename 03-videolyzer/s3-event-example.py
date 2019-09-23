# coding: utf-8
import urllib
event = {
	'Records': [{
		'eventVersion': '2.1',
		'eventSource': 'aws:s3',
		'awsRegion': 'us-east-1',
		'eventTime': '2019-09-23T01:39:32.929Z',
		'eventName': 'ObjectCreated:Put',
		'userIdentity': {
			'principalId': 'AWS:AIDAJG66T3OMB3TDANXIE'
		},
		'requestParameters': {
			'sourceIPAddress': '54.243.0.222'
		},
		'responseElements': {
			'x-amz-request-id': 'B657862B507A60F1',
			'x-amz-id-2': 'dXxGObgjDBZHiDeB7EUby7AnILnsbYBDwmix5C5hfqCc1SdnnTm7t7SCuRI+f4VaNp6+KgpveJQ='
		},
		's3': {
			's3SchemaVersion': '1.0',
			'configurationId': 'eab316a8-26ad-47ea-9f6e-34bbd2022234',
			'bucket': {
				'name': 'keithvideolyzervideos123456',
				'ownerIdentity': {
					'principalId': 'A26GOZJFY0CZ8M'
				},
				'arn': 'arn:aws:s3:::keithvideolyzervideos123456'
			},
			'object': {
				'key': 'Pexels+Videos+2880.mp4',
				'size': 8123504,
				'eTag': 'a705c560565ea3aae621383a33362f2e',
				'sequencer': '005D882254BB745527'
			}
		}
	}]
}
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])