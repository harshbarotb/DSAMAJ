from django.db import models


# Create your models here


class FamilyCode(models.Model):
    Family_Code = models.CharField(max_length=200, null=True)
    Date = models.DateTimeField(null=True)

    def __str__(self):
        return self.Family_Code


class ZoneCode(models.Model):
    ZoneName = models.CharField(max_length=200, null=True)
    ZoneCode = models.CharField(max_length=200, null=True)
    Family_Code = models.ForeignKey(FamilyCode, null=True, max_length=50, on_delete=models.CASCADE)

    def __str__(self):
        return self.ZoneCode


class HeadPerson(models.Model):
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female'),
        (3, 'not specified'),
    )
    Marital_Status = (
        (1, 'UnMarried'),
        (2, 'Married'),
    )
    Zone_Name = models.CharField(null=True, max_length=200)
    Zone_Code = models.ManyToManyField(ZoneCode, max_length=50)
    Family_Code = models.OneToOneField(FamilyCode, null=True, max_length=50, on_delete=models.CASCADE)
    Native_City = models.CharField(null=True, max_length=70)
    HeadPerson_Of_Family = models.CharField(blank=True, max_length=300,
                                            help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    gender = models.IntegerField(blank=True, choices=GENDER_CHOICES, default=" ")
    Age = models.IntegerField(null=True, default='0')
    CURRENT_CITY = models.CharField(null=True, max_length=200)
    Phone_NO = models.IntegerField(null=True)
    Email = models.EmailField(null=True, max_length=254)
    Date = models.DateTimeField(null=True, )

    def __str__(self):
        return self.HeadPerson_Of_Family


class Male(models.Model):
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female'),
        (3, 'not specified'),
    )
    Marital_Status = (
        (1, 'UnMarried'),
        (2, 'Married'),
    )
    Relation_With_HeadPerson = (
        (0, '--------'),
        (1, 'Daughter'),
        (2, 'Wife'),
        (3, 'Husband'),
        (4, 'Daughter-In-Law'),
        (5, 'Son-In-Law'),
        (6, 'Father'),
        (7, 'Mother'),
        (8, 'Grand-Father'),
        (9, 'Grand-Mother'),
        (10, 'Father-In-Law'),
        (11, 'Mother-In-Law'),
        (12, 'Son'),
        (13, 'HeadPerson'),
    )
    Sr_Id = models.AutoField
    Zone_Name = models.CharField(null=True, max_length=200)
    Zone_Code = models.ManyToManyField(ZoneCode, verbose_name="List Of ZoneCode", max_length=50)
    Family_Code = models.ForeignKey(FamilyCode, max_length=300, null=True, on_delete=models.CASCADE,
                                    help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")

    Relation_With_HeadPerson = models.CharField(null=True, max_length=200, choices=Relation_With_HeadPerson,
                                                default=" ")
    Father_Name = models.CharField(null=True, max_length=200)
    GrandFather_Name = models.CharField(null=True, max_length=200,
                                        help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    Mother_Name = models.CharField(null=True, max_length=200,
                                   help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    Member_Name = models.CharField(null=True, max_length=200)
    gender = models.CharField(null=True, max_length=200, choices=GENDER_CHOICES, default=" ")
    Age = models.IntegerField(null=True, default='0')
    MaritalStatus = models.CharField(null=True, max_length=200, choices=Marital_Status, default=" ")
    Address = models.TextField(null=True, max_length=400)
    CURRENT_CITY = models.CharField(null=True, max_length=200)
    CITY_PINCODE = models.IntegerField(null=True)
    Phone_NO = models.IntegerField(null=True)
    Email = models.EmailField(null=True, max_length=254)
    Image_Field = models.ImageField(blank=True, null=True, upload_to='media/images')
    Date = models.DateTimeField(null=True)

    def __str__(self):
        return self.Member_Name


class FeMale(models.Model):
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female'),
        (3, 'not specified'),
    )
    Marital_Status = (
        (1, 'UnMarried'),
        (2, 'Married'),
    )
    Relation_With_HeadPerson = (
        (0, '--------'),
        (1, 'Daughter'),
        (2, 'Wife'),
        (3, 'Husband'),
        (4, 'Daughter-In-Law'),
        (5, 'Son-In-Law'),
        (6, 'Father'),
        (7, 'Mother'),
        (8, 'Grand-Father'),
        (9, 'Grand-Mother'),
        (10, 'Father-In-Law'),
        (11, 'Mother-In-Law'),
        (12, 'Son'),
        (13, 'HeadPerson'),
    )
    Sr_Id = models.AutoField
    Zone_Name = models.CharField(null=True, max_length=200)
    Zone_Code = models.ManyToManyField(ZoneCode, verbose_name="List Of ZoneCode", max_length=50)
    Family_Code = models.ForeignKey(FamilyCode, null=True, max_length=50, on_delete=models.CASCADE)
    Native_City = models.CharField(null=True, max_length=70)
    HeadPerson_Of_Family = models.CharField(max_length=300, null=True,
                                            help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    Relation_With_HeadPerson = models.CharField(null=True, max_length=200, choices=Relation_With_HeadPerson,
                                                default=" ")
    Father_Name = models.CharField(null=True, max_length=200)
    GrandFather_Name = models.CharField(null=True, max_length=200,
                                        help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    Mother_Name = models.CharField(null=True, max_length=200,
                                   help_text="Please use the following format: <em>SurName- FirstName- LastName-</em>.")
    Member_Name = models.CharField(null=True, max_length=200)
    gender = models.CharField(null=True, max_length=200, choices=GENDER_CHOICES, default=" ")
    Age = models.IntegerField(null=True, default='0')
    MaritalStatus = models.CharField(null=True, max_length=200, choices=Marital_Status, default=" ")
    Address = models.TextField(null=True, max_length=400)
    CURRENT_CITY = models.CharField(null=True, max_length=200)
    CITY_PINCODE = models.IntegerField(null=True)
    Phone_NO = models.IntegerField(null=True)
    Email = models.EmailField(null=True, max_length=254)
    Image_Field = models.ImageField(null=True, blank=True, upload_to='media/images')
    Date = models.DateTimeField(null=True)

    def __str__(self):
        return self.Member_Name
