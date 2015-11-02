from django.db import models

class User(models.Model):
	first_name = models.TextField(blank=False, max_length=20, null=True)
	last_name = models.TextField(blank=False, max_length=20,null=True)
	email = models.TextField(blank=False, max_length=20,null=True)
	description = models.TextField(blank=False, max_length=500,null=True)
	password = models.TextField(blank=False, max_length=20,null=True)
	user_level = models.IntegerField(blank=False, null=True)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'user'

class Message(models.Model):
	sender =  models.ForeignKey(User, related_name="sender_message_user",null=True)
	receiver = models.ForeignKey(User, related_name="receiver_message_user",null=True)
	message = models.TextField(blank=False, max_length=200, null=True)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'messages'


class Comment(models.Model):
	sender = models.ForeignKey(User, related_name="sender_comment_user", null=True)
	message = models.ForeignKey(Message, related_name="comment_message", null=True)
	comment = models.TextField(blank=False, max_length=200)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'comments'

class Poke(models.Model):
	poker = models.ForeignKey(User, related_name="poker", null=True)
	poked = models.ForeignKey(User, related_name = "poked", null=True)
	counter = models.IntegerField(blank=False, null=True, default=0)
	class Meta:
		db_table = 'pokes'