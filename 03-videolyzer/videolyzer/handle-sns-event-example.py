# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:320262049302:handleLabelDetectionTopic:d06d28bd-6394-44b6-a886-8d8ebc30f282', 'Sns': {'Type': 'Notification', 'MessageId': '54e5d97d-8c92-5c3e-855c-8f7ef8f6592f', 'TopicArn': 'arn:aws:sns:us-east-1:320262049302:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"88269fb8bb610b62e11b244978c5eac220f8b6948daf7eb154668a9e1360466a","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1569288740653,"Video":{"S3ObjectName":"lambs.mp4","S3Bucket":"keithvideolyzervideos123456"}}', 'Timestamp': '2019-09-24T01:32:20.758Z', 'SignatureVersion': '1', 'Signature': 'VNlrwn1HMeB6f+BoV3Dp58y2zqydAGj9LnRm/aR5bEb2vEW2OyuL4A0fX2eqOiyZ+VI3Intkbip1QniQ9JHY40ocvLUX8n6UG7rRH+iEQmsatoA7zFrHJOr5SBWSS4BcfkhpbJB/S5NGdv717n7yiciKhf4KkcVyJ+E52XsZDkZKatmzMr2OIK289OoxFTXuGx8k1zPyYiVCzpqyWagxWRCAcQsYD+4siFwPC5/X8vLjye5la73bBPJEwIK9D3gNkQNk6ua7WizZ7wCJMkVvwZMg/3Hk3FpPtiVZuX4oM7Buct/l4/oSZ3BOvugegypICebRaxSf+qfq75Nc57sa5g==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:320262049302:handleLabelDetectionTopic:d06d28bd-6394-44b6-a886-8d8ebc30f282', 'MessageAttributes': {}}}]}
event
event.keys()
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscription']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns'].keys()
event['Records'][0]['Sns']['Message']
event['Records'][0]['Sns']['Message']['JobId']
type(event['Records'][0]['Sns']['Message']['JobId'])
type(event['Records'][0]['Sns']['Message'])
import json
json.loads(event['Records'][0]['Sns']['Message'])
