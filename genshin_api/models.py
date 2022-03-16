from django.db import models

# Create your models here.

class CharacterType (models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=3)
	class Meta:
		db_table = "character_type"

class CharacterNation (models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=10)
	class Meta:
		db_table = "character_nation"


# class CharacterData (models.Model):
# 	id=models.AutoField(primary_key=True)
# 	character_name=models.CharField(max_length=10)
# 	character_grade=models.SmallIntegerField()
# 	character_nation=models.Foreignkey(CharacterNation)
# 	character_gender=models.CharField(max_length=1)

# 	weapon_type
# 	skill_book
# 	character_type