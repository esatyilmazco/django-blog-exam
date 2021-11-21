from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel


class ProfilDuzenlemeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUserModel
        fields = ('email', 'first_name', 'last_name', 'avatar')

    def __init__(self, *args):
        super(ProfilDuzenlemeForm, self).__init__(*args)
