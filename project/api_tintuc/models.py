from django.db import models

# Create your models here.
class Giaidau(models.Model):
    tenGD = models.CharField(max_length=100, unique=True)
    logoGD = models.CharField(max_length=100)

    def __str__(self):
        return self.tenGD
    
class Tintuc(models.Model):
    tieude = models.CharField(max_length=100)
    tomtat = models.CharField(max_length=100)
    noidung = models.CharField(max_length=1000)
    hinhanh = models.CharField(max_length=100)
    tacgia = models.CharField(max_length=100)
    ngaydang = models.DateTimeField(auto_now_add=True)
    giaidau = models.ForeignKey(Giaidau, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tieude

