# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class LettersGroup(models.Model):
    letters_group_id = models.IntegerField(primary_key=True, db_column='Letters_Group_ID') # Field name made lowercase.
    letters_group = models.CharField(max_length=20L, db_column='Letters_Group') # Field name made lowercase.
    letters_group_socialbelonging = models.CharField(max_length=510L, db_column='Letters_Group_SocialBelonging') # Field name made lowercase.
    letters_group_sense = models.CharField(max_length=510L, db_column='Letters_Group_Sense') # Field name made lowercase.
    class Meta:
        db_table = 'letters_group'

class PhonmeGroup(models.Model):
    phonme_group_id = models.CharField(max_length=100L, primary_key=True, db_column='Phonme_Group_ID') # Field name made lowercase.
    phonme_group = models.CharField(max_length=100L, db_column='Phonme_Group') # Field name made lowercase.
    phonme_group_sense = models.CharField(max_length=510L, db_column='Phonme_Group_Sense', blank=True) # Field name made lowercase.
    phonme_group_neigbor_relation = models.CharField(max_length=510L, db_column='Phonme_Group_Neigbor_Relation', blank=True) # Field name made lowercase.
    corresponding_chinese_word = models.CharField(max_length=100L, db_column='Corresponding_Chinese_Word', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'phonme_group'

class PhonmeGroupLinkPhonmeRelation(models.Model):
    table_id = models.CharField(max_length=100L, primary_key=True, db_column='Table_ID') # Field name made lowercase.
    phonme_group_id = models.CharField(max_length=510L, db_column='Phonme_Group_ID') # Field name made lowercase.
    phonme_id = models.CharField(max_length=510L, db_column='Phonme_ID') # Field name made lowercase.
    phonme_sense = models.CharField(max_length=510L, db_column='Phonme_Sense', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'phonme_group_link_phonme_relation'

class PhonmeRelation(models.Model):
    phonme_id = models.CharField(max_length=255L, primary_key=True, db_column='Phonme_ID') # Field name made lowercase.
    phonme = models.CharField(max_length=510L, db_column='Phonme') # Field name made lowercase.
    phonme_sense = models.CharField(max_length=510L, db_column='Phonme_Sense', blank=True) # Field name made lowercase.
    word_example = models.CharField(max_length=510L, db_column='Word_Example', blank=True) # Field name made lowercase.
    phonme_neigbor_relation = models.CharField(max_length=510L, db_column='Phonme_Neigbor_Relation', blank=True) # Field name made lowercase.
    phonme_sort = models.IntegerField(null=True, db_column='Phonme_Sort', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'phonme_relation'

class PhraseComponent(models.Model):
    table_id = models.IntegerField(primary_key=True, db_column='Table_ID') # Field name made lowercase.
    phrase = models.CharField(max_length=510L, db_column='Phrase', blank=True) # Field name made lowercase.
    phrase_component = models.CharField(max_length=510L, db_column='Phrase_Component', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'phrase_component'

class PhraseTotal(models.Model):
    table_id = models.IntegerField(primary_key=True, db_column='Table_ID') # Field name made lowercase.
    class_id = models.IntegerField(db_column='Class_ID') # Field name made lowercase.
    phrase = models.CharField(max_length=510L, db_column='Phrase') # Field name made lowercase.
    chinese_sense = models.CharField(max_length=510L, db_column='Chinese_Sense', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'phrase_total'

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=160L)
    principal_id = models.IntegerField()
    diagram_id = models.IntegerField(primary_key=True)
    version = models.IntegerField(null=True, blank=True)
    definition = models.TextField(blank=True)
    class Meta:
        db_table = 'sysdiagrams'

class WordAndWordRootId(models.Model):
    table_id = models.IntegerField(primary_key=True, db_column='Table_ID') # Field name made lowercase.
    word = models.CharField(max_length=510L, db_column='Word', blank=True) # Field name made lowercase.
    word_root_id = models.CharField(max_length=510L, db_column='Word_Root_ID', blank=True) # Field name made lowercase.
    word_sort_order = models.IntegerField(db_column='Word_Sort_Order') # Field name made lowercase.
    class Meta:
        db_table = 'word_and_word_root_id'

class WordAndWordRootSet(models.Model):
    word = models.CharField(max_length=255L, primary_key=True, db_column='Word') # Field name made lowercase.
    word_root_set = models.CharField(max_length=510L, db_column='Word_Root_Set') # Field name made lowercase.
    word_background = models.CharField(max_length=510L, db_column='Word_BackGround', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'word_and_word_root_set'

class WordClassSet(models.Model):
    class_id = models.IntegerField(primary_key=True, db_column='Class_ID') # Field name made lowercase.
    class_field = models.CharField(max_length=510L, db_column='Class', blank=True) # Field name made lowercase. Field renamed because it was a Python reserved word.
    class Meta:
        db_table = 'word_class_set'

class WordRoot(models.Model):
    word_root_id = models.CharField(max_length=255L, primary_key=True, db_column='Word_Root_ID') # Field name made lowercase.
    word_root = models.CharField(max_length=510L, db_column='Word_Root') # Field name made lowercase.
    word_root_component = models.CharField(max_length=510L, db_column='Word_Root_Component', blank=True) # Field name made lowercase.
    word_root_english_sense = models.TextField(db_column='Word_Root_English_Sense', blank=True) # Field name made lowercase.
    word_root_chinese_sense = models.CharField(max_length=510L, db_column='Word_Root_Chinese_Sense', blank=True) # Field name made lowercase.
    word_example = models.CharField(max_length=510L, db_column='Word_Example', blank=True) # Field name made lowercase.
    word_root_sort = models.IntegerField(null=True, db_column='Word_Root_Sort', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'word_root'

class WordTotal(models.Model):
    table_id = models.IntegerField(primary_key=True, db_column='Table_ID') # Field name made lowercase.
    class_id = models.IntegerField(null=True, db_column='Class_ID', blank=True) # Field name made lowercase.
    word = models.CharField(max_length=510L, db_column='Word', blank=True) # Field name made lowercase.
    chinese_sense = models.CharField(max_length=510L, db_column='Chinese_Sense', blank=True) # Field name made lowercase.
    pronunciation = models.CharField(max_length=510L, db_column='Pronunciation', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'word_total'
