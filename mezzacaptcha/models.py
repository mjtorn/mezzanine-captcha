# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.utils.translation import ugettext_lazy as _

from captcha import fields as captcha_fields

from mezzanine.forms import fields as mezzanine_fields

## Figure out what to register us as

GREATEST_ID = max(c[0] for c in mezzanine_fields.NAMES)

ID = GREATEST_ID + 1
NAME = 'CAPTCHA'

setattr(mezzanine_fields, NAME, ID)

mezzanine_fields.NAMES = list(mezzanine_fields.NAMES)
mezzanine_fields.NAMES.append((ID, _('Captcha')))
mezzanine_fields.NAMES = tuple(mezzanine_fields.NAMES)

mezzanine_fields.CLASSES[ID] = captcha_fields.CaptchaField

# EOF

