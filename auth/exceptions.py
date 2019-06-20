from rest_framework.exceptions import APIException
from rest_framework import status

from django.utils.translation import ugettext_lazy as _


class LogoutFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('You already logouted.')
    default_code = 'logout_failed'