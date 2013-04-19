# -*- encoding: utf-8 -*-
# Create your views here.
import datetime
from django.contrib import messages
from documents.forms import LeadSearchForm
from accounts.models import Company
from django.utils.timezone import utc, make_naive, get_default_timezone
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response, get_object_or_404, get_list_or_404
from documents.models import DocumentDownloadLog
from seminars.models import SeminarEntryLog
from trwk.libs.csv_utils import export_csv
from django.template import RequestContext

@login_required
def company_leads(request):
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, '管理者ではありません')
        return None
    user = request.user
    companies = Company.objects.all()
    if 'search' in request.GET:
        form = LeadSearchForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['start_date']:
                start = datetime.datetime.strptime( str(form.cleaned_data['start_date']),'%Y-%m-%d').replace(tzinfo=timezone.utc)
            if form.cleaned_data['end_date']:
                #時刻まで条件に入っているっぽく、前日までしかとれないので+1日
                end =   datetime.datetime.strptime( str(form.cleaned_data['end_date']),'%Y-%m-%d').replace(tzinfo=timezone.utc) + datetime.timedelta(days=1)
    else:
        form = LeadSearchForm()

    return render_to_response(
        'operations/company_lead_list.html',
        {
            'companies' : companies,
            'form'  : form,
        },
        context_instance=RequestContext(request)
    )

@login_required
def download_leads(request, log_type, company_id):
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, '管理者ではありません')
        return None
    if log_type == 'document':
        log_obj = DocumentDownloadLog
        date_field = 'download_date'
    elif log_type == 'seminar':
        log_obj = SeminarEntryLog
        date_field = 'entry_date'
    else:
        messages.add_message(request, messages.ERROR, 'log_typeが正しくありません')
        return None

    csv_fields = log_obj.csv_fields
    leads = log_obj.objects
    filename = company_id +'-'+ log_type
    if 'search' in request.GET:
        form = LeadSearchForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['start_date']:
                start = datetime.datetime.strptime( str(form.cleaned_data['start_date']),'%Y-%m-%d').replace(tzinfo=timezone.utc)
                query = {
                    '{0}__{1}'.format(date_field, 'gte'):start,
                }
                leads = leads.filter(**query)
                filename = filename + '-' + str(form.cleaned_data['start_date'])+ '^'
            if form.cleaned_data['end_date']:
                #時刻まで条件に入っているっぽく、前日までしかとれないので+1日
                end =   datetime.datetime.strptime( str(form.cleaned_data['end_date']),'%Y-%m-%d').replace(tzinfo=timezone.utc) + datetime.timedelta(days=1)
                query = {
                    '{0}__{1}'.format(date_field, 'lte'):end,
                }
                leads = leads.filter(**query)
                if not form.cleaned_data['start_date']:
                    filename += '-^'
                filename = filename + str(form.cleaned_data['end_date'])
    else:
        form = LeadSearchForm()

    company = Company.objects.get(pk=company_id)
    leads = leads.filter(
        company=company,
    ).order_by(date_field)
    filename = filename + '.csv'
    return export_csv(leads, csv_fields, filename)

