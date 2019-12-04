from django.db import models
import datetime
from pgcrypto import fields

#first_name = fields.TextPGPSymmetricKeyField(blank=False, null=False)

#to be changed later
"""RAG_CHOICES = (
    (1, 'Green')
    (2, 'Amber')
    (3, 'Red')
    (4, 'N/A')
)"""

class Question(models.Model):
    question_no = models.IntegerField(primary_key=True)
    quest_tx = models.CharField(max_length=1000, default="")
    # quest_tx = fields.TextPGPSymmetricKeyField(blank=False, null=False)
    # quest_tx_hash = fields.TextHMACField(original='quest_tx')
    eval_tx = models.CharField(max_length=1000, default="")
    evidence_tx = models.CharField(max_length=1000, default="")
    results_tx = models.CharField(max_length=1000, default="")
    rag_conditional_int = models.IntegerField(default=4)

class Quadrants(models.Model):
    quadrant_no = models.IntegerField(primary_key=True) 
    quadrant_tx = models.CharField(max_length=3000, default="")
    question_no = models.ForeignKey(Question, on_delete=models.CASCADE)
    
class Questionnaire(models.Model):
    questionnaire_type_no = models.IntegerField(primary_key=True)
    questionnaire_type_tx = models.CharField(max_length=100, default="")
    completed_date_dt = models.DateField(default=datetime.date.today())
    quadrant_no = models.ForeignKey(Quadrants, on_delete=models.CASCADE)

class SME(models.Model):
    company_id_no = models.IntegerField(primary_key=True)
    SME_name_tx = fields.TextPGPSymmetricKeyField(blank=False, null=False) #models.CharField(max_length=3000, default="")
    email_tx = models.CharField(max_length=3000, default="")
    questionnaire_no = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)