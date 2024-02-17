from django.db import models

class Problem(models.Model):
    
    DIFFICULTY_CHOICES = [
        ('basic', 'Basic'),
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    statement = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    test_case_file = models.FileField(upload_to='test_cases/')
    expected_output_file = models.FileField(upload_to='expected_output/')  

    

    def __str__(self):
        return self.name

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)


# class TestCase(models.Model):
#     problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
#     input = models.TextField()