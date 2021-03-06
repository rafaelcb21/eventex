from django.db import models
from eventex.subscriptions.validators import validate_cpf
from hashlib import sha1
from random import SystemRandom
from uuid import uuid4

char = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def hash_(size=15, chars=char):
    word = ''.join(SystemRandom().choice(chars) for _ in range(size))
    salt = uuid4().hex
    key_hash = sha1(salt.encode() + word.encode()).hexdigest()
    return key_hash


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    key_hash = models.CharField('hash', max_length=40, default=hash_)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name