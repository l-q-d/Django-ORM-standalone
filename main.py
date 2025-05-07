import os
import django
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    print('Всего пропусков:', Passcard.objects.count())
    print('Активных пропусков:', len(active_passcards))