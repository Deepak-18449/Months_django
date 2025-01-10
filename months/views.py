from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound ,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

month_ly = {
        "Jan": "Hello January",
        "feb": "Hello February",
        "mar": "Hello March",
        "api": "Hello Apirl",
        "may": "Hello May",
        "jun": "Hello June",
        "jul": "Hello July",
        "aug": "Hello August",
        "sep": "Hello September",
        "oct": "Hello October",
        "nov": "Hello November",
        "dec": "Hello December",
    }


def index(request):
    list_items =''
    months = list(month_ly.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<h1><a href="{month_path}">{capitalized_month}</a></h1>'

    respone_data = f"<ol>{list_items}</ol>"
    return HttpResponse(respone_data)

def Month_by_number(request , month):
    print("redirect_month")
    months =list(month_ly.keys())
    if month > len(months):
        return HttpResponseNotFound("Month_by_number_path not found")
    
    redirect_month = months[month-1]
    # return HttpResponseRedirect('/month/'+ redirect_month)
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def Month_by_name (request , month):

    try:
        challeng_text=month_ly[month]
        # return HttpResponse(f'<center><h1 style="color:blue;">{challeng_text}</h1></center>')
        # return HttpResponse(render_to_string('month/month.html'))
        return HttpResponse(render(request,'month/month.html',{
            'challeng_text':month
        }))
    except:
        return HttpResponseNotFound("month not found") 
    








    # Create your views here.
# def jan(request):
#     return HttpResponse('hello jan')

# def feb(request):
#     return HttpResponse('hello feb')

# def Random(request , month):
#     if month == 'jan':
#         return HttpResponse("hello jan")
#     elif month == 'feb':
#         return HttpResponse("hello feb")
#     else :
#         return HttpResponseNotFound("invalid month")

    # for i in month():
    #     if i == 1:
    #         return HttpResponse("hello jan")
            
    #     elif i == 2:
    #         return HttpResponse("hello feb")
            
    #     elif i == 3:
    #         return HttpResponse("hello march")
            
    #     elif i == 4:
    #         return HttpResponse("hello apirl")
            
    #     elif i == 5:
    #         return HttpResponse("hello may")
            
    #     elif i == 6:
    #         return HttpResponse("hello june")
            
    #     elif i == 7:
    #         return HttpResponse("hello july")
            
    #     elif i == 8:
    #         return HttpResponse("hello aug")
            
    #     elif i == 9:
    #         return HttpResponse("hello sep")
            
    #     elif i == 10:
    #         return HttpResponse("hello oct")
            
    #     elif i == 11:
    #         return HttpResponse("hello nov")
            
    #     elif i == 12:
    #         return HttpResponse("hello dec")
            
    #     else:
    #         return HttpResponseNotFound("sorry enter a valid output")

# def Random (request,month):
#     for i in month.values():
#         a= None
#         month = {
#             1: "jan",
#             2: "feb",
#             3: "mar",
#             4: "api",
#             5: "may",
#             6: "jun",
#             7: "jul",
            
#         }
#         if i == month:
#             a="hello jan"
#         else:
#             a="sorry"
#     return a
