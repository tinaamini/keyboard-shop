from celery import shared_task
from datetime import datetime, timedelta
import pytz
from account.models import OtpCode


@shared_task()
def remove_expired_otp_codes():
    exp_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=5)
    OtpCode.objects.filter(created__lt=exp_time).delete()
