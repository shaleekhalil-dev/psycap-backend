from django.db import models

class EmployeePsyCap(models.Model):
    name = models.CharField(max_length=100)
    hope = models.FloatField(default=0.0)
    efficacy = models.FloatField(default=0.0)
    resilience = models.FloatField(default=0.0)
    optimism = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def average_score(self):
        # حساب المتوسط الحسابي للأبعاد الأربعة
        return (self.hope + self.efficacy + self.resilience + self.optimism) / 4

    @property
    def status(self):
        avg = self.average_score
        if avg >= 4.5: return "High (Thriving)"
        elif avg >= 3.0: return "Moderate (Stable)"
        else: return "Low (At Risk)"

    def __str__(self):
        return f"{self.name} - {self.status}"
