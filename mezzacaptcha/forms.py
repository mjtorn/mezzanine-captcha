
from django import forms
from captcha.fields import CaptchaField
from mezzanine.generic.forms import ThreadedCommentForm


class CaptchaThreadedCommentForm(ThreadedCommentForm):
    """ Adds a captcha field to the comment form in blog
    """
    captcha = CaptchaField()