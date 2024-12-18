from django.core.management.base import BaseCommand
from account.models import OtpCode
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = 'remove all exp otp codes'

    def handle(self, *args, **options):
        exp_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=5)
        OtpCode.objects.filter(created__lt=exp_time).delete()
        self.stdout.write('all exp otp code removed')


