mezzanine-captcha
=================

Caveat
------

This is a hack which looks at the field types in your Mezzanine installation and infers
a safe-enough ID number to use. If, by any reason at all, you were to make apps like
this one, and get the IDs wrong, your forms will see weird side-effects.

A registry for custom fields in Mezzanine would be more worth-while!

Installation
------------

The application needs to be before ``mezzanine.forms`` in ``INSTALLED_APPS``.

I use it between the django and mezzanine ones.

  'django.contrib.staticfiles',
  'captcha',      # \__ the new ones
  'mezzacaptcha', # /
  'mezzanine.boot',

You also need to configure ``urls.py`` in your Mezzanine app.

  ("^captcha/", include('captcha.urls')), # Slap it in before the catch-all
  ("^", include("mezzanine.urls")),

License
-------

BSD. Whatever. Not gonna care too much.

