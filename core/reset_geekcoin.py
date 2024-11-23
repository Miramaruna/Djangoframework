from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apps.news.models import Students

def reset_geekcoin():
    Students.objects.update(geekcoin=4)
    print("Geekcoin balances have been reset to 4.")

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

scheduler.add_job(
    reset_geekcoin,
    trigger='cron', 
    day=1,
    hour=0,
    minute=0,
    id="reset_geekcoin",  
    replace_existing=True,
)

scheduler.start()