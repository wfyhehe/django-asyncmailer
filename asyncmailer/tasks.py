from celery import shared_task
from django.template.loader import render_to_string
from celery.schedules import crontab
from celery.task import periodic_task
from asyncmailer.models import Provider
import random


@shared_task(default_retry_delay=5, max_retries=3)
def async_select_and_send(email, title, plain_text, rich_text, html_only=False, **kwargs):
    try:
        providers = Provider.objects.all()
        good_providers = sorted([x for x in providers if x.can_send(email)], key=lambda p: p.can_send, reverse=True)
        top_preference = good_providers[0].preference
        top_providers = [provider for provider in good_providers if provider.preference == top_preference]
        selected_provider = random.choice(top_providers)
        if html_only:
            selected_provider.send(email, title, rich_text, html_only=True)
        else:
            selected_provider.send(email, title, plain_text, html_message=rich_text)
    except Exception as exc:
        raise async_select_and_send.retry(exc=exc)


def async_mail(email, title, context_dict=None, template='asyncmailer/email.html', template_plaintext='asyncmailer/email_pt.html'):
    if len(email) == 1:
        if context_dict:
            rich_text = render_to_string(template, context_dict)
            plain_text = render_to_string(template_plaintext, context_dict)
        else:
            rich_text = render_to_string(template)
            plain_text = render_to_string(template_plaintext)
        async_select_and_send.delay(email[0], title, plain_text, rich_text)
    else:
        for address in email:
            async_mail(email, title, context_dict[address], template, template_plaintext)



@periodic_task(run_every=crontab(hour=0, minute=0))
def clear_daily_usages():
    providers = Provider.objects.filter(quota_type_is_daily=True)
    for p in providers:
        p.reset_usage()


@periodic_task(run_every=crontab(day_of_month=1, hour=0, minute=0))
def clear_monthly_usages():
    providers = Provider.objects.filter(quota_type_is_daily=False)
    for p in providers:
        p.reset_usage()
