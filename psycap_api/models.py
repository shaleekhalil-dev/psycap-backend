from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class EmployeePsyCap(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الموظف")
    
    # أبعاد رأس المال النفسي مع قيود (0-5)
    hope = models.FloatField(default=0.0, validators=[MinUintValidator(0), MaxValueValidator(5)])
    efficacy = models.FloatField(default=0.0, validators=[MinUintValidator(0), MaxValueValidator(5)])
    resilience = models.FloatField(default=0.0, validators=[MinUintValidator(0), MaxValueValidator(5)])
    optimism = models.FloatField(default=0.0, validators=[MinUintValidator(0), MaxValueValidator(5)])
    
    # حقول التفاعل الجديدة (للحفظ الدائم)
    likes = models.PositiveIntegerField(default=0, verbose_name="عدد الإعجابات")
    dislikes = models.PositiveIntegerField(default=0, verbose_name="عدد الاعتراضات")
    employee_notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات/تعليقات الموظف")
    
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def average_score(self):
        # تقريب النتيجة لخانة عشرية واحدة لجمالية العرض
        avg = (self.hope + self.efficacy + self.resilience + self.optimism) / 4
        return round(avg, 2)

    @property
    def status(self):
        avg = self.average_score
        if avg >= 4.5: return "High (Thriving)"
        elif avg >= 3.0: return "Moderate (Stable)"
        else: return "Low (At Risk)"

    def __str__(self):
        return f"{self.name} - Avg: {self.average_score}"

    class Meta:
        verbose_name = "تقييم موظف"
        verbose_name_plural = "تقييمات الموظفين"
        ordering = ['-created_at'] # عرض الأحدث أولاً