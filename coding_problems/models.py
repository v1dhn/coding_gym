from django.db import models

class Problem(models.Model):
    statement = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    expected_output = models.TextField()
