from django.core.exceptions import ObjectDoesNotExist


class UserNotExists(ObjectDoesNotExist):
    pass


class ProductNotExists(ObjectDoesNotExist):
    pass
