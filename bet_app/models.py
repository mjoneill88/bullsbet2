from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Bet(models.Model):
    bet_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    expiration_date = models.DateTimeField('date_expires')
    correct_choice = models.CharField(max_length=200, default='maybe')

    def __str__(self):
        return self.bet_text


@python_2_unicode_compatible
class Choice(models.Model):
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text



@python_2_unicode_compatible
class MyBets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bet_taken = models.ForeignKey(Bet, on_delete=models.CASCADE)

    def __str__(self):
        return self.bet_taken
