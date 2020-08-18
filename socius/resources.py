from import_export import resources
from .models import UserList
from .models import DirectoryCreation


class UserListResource(resources.ModelResource):
    class Meta:
        model = UserList
class DirectoryResource(resources.ModelResource):
    class Meta:
        model=DirectoryCreation