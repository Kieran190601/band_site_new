from django.db import models

class BandMember(models.Model):
    """
    Represents a member of a band, containing information about their
    name, instrument, biography, and image.

    Attributes:
        name (CharField): The full name of the band member, limited to 100 characters.
        instrument (CharField): The instrument that the band member plays, limited to 100 characters.
        bio (TextField): A detailed biography of the band member, providing background information.
        image (ImageField): An image of the band member, uploaded to the 'band_members/' directory.

    Methods:
        __str__(): Returns a string representation of the band member, specifically their name.
    """

    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='band_members/')

    def __str__(self):
        """
        Returns:
            str: The name of the band member.
        """
        return self.name

