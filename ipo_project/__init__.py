from django.db import models

class IPO(models.Model):
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    company_name = models.CharField(max_length=255)
    open_date = models.CharField(max_length=50, default="Not Issued")
    close_date = models.CharField(max_length=50, default="Not Issued")
    issue_size = models.CharField(max_length=50, blank=True)
    issue_type = models.CharField(max_length=50, blank=True)
    price_band = models.CharField(max_length=50, default="Not Issued")
    listing_date = models.CharField(max_length=50, default="Not Issued")
    status = models.CharField(max_length=50, blank=True)
    
    # New Listed IPO Details
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    listing_gain = models.CharField(max_length=50, blank=True)
    listing_gain_date = models.DateField(blank=True, null=True)
    cmp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_return = models.CharField(max_length=50, blank=True)
    rhp = models.CharField(max_length=255, blank=True)
    drhp = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.company_name
