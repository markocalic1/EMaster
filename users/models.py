from django.contrib.auth.models import User as DjangoUser

class User(DjangoUser):

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super(User, self).save(*args, **kwargs)