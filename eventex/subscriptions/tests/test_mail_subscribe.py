from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Rafael', cpf='12345678901',
                    email='rafael@braga.net', phone='11-99969-8891')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'rafael@braga.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Rafael',
                    '12345678901',
                    'rafael@braga.net',
                    '11-99969-8891'
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
