from django.db import models
 
 
class Role(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('member', 'Member'),
        ('viewer', 'Viewer'),
    )
 
    role_type = models.CharField(max_length=50, unique=True)
    description = models.TextField()
 
    def __str__(self):
        return self.role_type
 
 
class AppUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    empid = models.CharField(max_length=50)
 
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )
 
    supervisor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
 
    def __str__(self):
        return self.email
 