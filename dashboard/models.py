from django.db import models
import joblib


# Create your models here.

class Database(models.Model):
    Temperature	= models.FloatField(default=0.0)
    Maltodextrin = models.FloatField(default=0.0)	
    FlowRate = models.FloatField(default=0.0)
    Yield = models.FloatField(default=0.0, blank=True)
    MoistureContent = models.FloatField(default=0.0, blank=True)
    ColorChange = models.FloatField(default=0.0, blank=True)
    R = models.FloatField('Wettability', default=0.0, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # Pass input values into the model 
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/DTRegression_model.sav')
        predicted_result = ml_model.predict(
            [[self.Temperature, self.Maltodextrin, self.FlowRate]])
        self.Yield = predicted_result[0][0]
        self.MoistureContent = predicted_result[0][1]
        self.ColorChange = predicted_result[0][2]
        self.R = predicted_result[0][3]
        return super().save(*args, *kwargs)
        

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Data"