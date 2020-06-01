from django.db import models


# Create your models here.
class FamilyCode(models.Model):
    id = models.AutoField(primary_key=True)
    F_Code = models.CharField(null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FamilyHead(models.Model):
    id = models.AutoField(primary_key=True)
    F_Code = models.CharField(null=True, max_length=200)
    Zone_Name = models.CharField(null=True, max_length=200)
    Native_City = models.CharField(null=True, max_length=70)
    Mosad_City = models.CharField(null=True, max_length=70)
    Father_Name = models.CharField(null=True, max_length=200)
    GrandFather_Name = models.CharField(null=True, max_length=200,
                                        help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    Mother_Name = models.CharField(null=True, max_length=200,
                                   help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    HeadPerson_Of_Family = models.CharField(blank=True, max_length=300,
                                            help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")

    Phone_NO_Office = models.CharField(null=True, max_length=200)
    Phone_NO_Home = models.CharField(null=True, max_length=200)
    Email = models.EmailField(null=True, max_length=254)
    Date = models.DateTimeField(auto_now_add=True)
    profile_image = models.FileField(upload_to="media/")
    Address = models.TextField()
    Town = models.CharField(null=True, max_length=200)
    Taluko = models.CharField(null=True, max_length=200)
    District = models.CharField(null=True, max_length=200)
    CITY_PINCODE = models.CharField(null=True, max_length=200)
    objects = models.Manager()


class FamilyMember(models.Model):
    id = models.AutoField(primary_key=True)
    M_F_Code = models.CharField(null=True, max_length=300)
    M_Name = models.CharField(null=True, max_length=200)
    M_Relation_To_Head = models.CharField(null=True, max_length=300)
    M_BOD = models.DateField(null=False)
    M_Study_Qualifications = models.CharField(null=True, max_length=300)
    M_Profession = models.CharField(null=True, max_length=300)
    M_Marital_Status = models.CharField(null=True, max_length=300)
    M_Blood_Group = models.CharField(null=True, max_length=300)
    M_Phone_NO = models.CharField(null=True, max_length=200)
    M_Sex = models.CharField(null=True, max_length=200)
    objects = models.Manager()


class FamilyHeadFamilyMembers(models.Model):
    id = models.AutoField(primary_key=True)
    family_M_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    family_H_id = models.ForeignKey(FamilyHead, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()