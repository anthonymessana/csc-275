# Work with Matthew Hannum and Michael Giordano
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from assignment_5 import SMSStatus, SMS, SendSMSService, TwilioAPI
from twilio.rest import Client

class TestSMS(unittest.TestCase):
    def test_SMS_getter(self):
        sms = SMS("Alice", "Bob", "Hello")
        self.assertEqual(sms.message, "Hello")
        
    def test_setter_empty_message(self):
        self.assertRaisesRegex(
            TypeError,
            "Message must have a value",
            SMS, 
            "8327354567", "9124567782", ""
        )
        
    def test_setter_overflow(self):
        self.assertRaisesRegex(
            ValueError,
            "Your message is too long",
            SMS,
            "8327354567", "9124567782", "dedewfweafergreuiewrkhewlrithekwlrhtkewrhtgfjrhfnksfjgnfkshlgrifhkjrehfkjhklafjhekjfhakejfhelkajhskjlhrekjrhajhfkjeahfkjahsefkjahsekfjfhkjrehfkjhklafjhekjfhakejfhelkajhskjlhrekjrhajhfkjeahfkjahsefkjahsekfjfhkjrehfkjhklafjhekjfhakejfhelkajhskjlhrekjrhajhfkjeahfkjahsefkjahsekfjdwdwafefwefwefwef"
        )

class TestSendSMSService(unittest.TestCase):
    def test_SMS_send(self):
        mTwilioApi = MagicMock(autospec=TwilioAPI)
        mSMS = MagicMock(autospec=SMS)
        SMSService = SendSMSService(mTwilioApi)
        SMSService.send(mSMS)
        mTwilioApi.send.assert_called_once_with(body=mSMS.message, from_=mSMS.sender, to_=mSMS.recipient)
        
    def test_complete(self):
        mResponse = MagicMock()
        mResponse.status = MagicMock()
        mTwilioApi = MagicMock(autospec=TwilioAPI)
        SMSService = SendSMSService(mTwilioApi)
        SMSService.complete(mResponse)
        mTwilioApi.get_status.assert_called_once_with(mResponse)

class TestTwilioAPI(unittest.TestCase):
    @patch.object(Client, "messages", autospec=True)
    def test_send(self, mock_messages_object):
        TObject = TwilioAPI()
        TObject.client = ("fake sid", "fake auth token")
        mSMS = MagicMock(autospec=SMS)
        TObject.send(body=mSMS.message, from_=mSMS.sender, to_=mSMS.recipient)
        mock_messages_object.create(body=mSMS.message, from_=mSMS.sender, to_=mSMS.recipient)
    
    def setUp(self):
        self.fixture_data = (
        (
        "accepted",
        SMSStatus.SENT,
        ),
        (
        "sent",
        SMSStatus.SENT,
        ),
        (
        "receiving",
        SMSStatus.SENT
        ),
        (
        "delivered",
        SMSStatus.DELIVERED
        ),
        (
        "received",
        SMSStatus.DELIVERED
        ),
        (
        "failed",
        SMSStatus.FAILED
        ),
        )
    
    def test_get_message_status(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                mResponse = MagicMock()
                mResponse.status = context
                returnStatus = TwilioAPI.get_message_status(mResponse)
                self.assertEqual(returnStatus, expected)
        
        