from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.views import View
from .forms import Form_Student, HotelForm
from .models import Profile, Hotel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialazers import Profile_Seroalzers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class form_profile(View):
    # def get(self, request):
    #     cf = Form_Student
    #     request render(request, 'student/profile.html', {'cf'=cf})
    def get(self, request):
        cf = Form_Student
        return render(request, 'student/profile.html', {'cf': cf})

    def post(self, request):
        if request.method == "POST":
            cf = Form_Student(request.POST)
            if cf.is_valid():
                savecf = Profile(username=cf.cleaned_data['username'], password=cf.cleaned_data['password'], name=cf.cleaned_data[
                    'name'], email=cf.cleaned_data['email'], sex=cf.cleaned_data['sex'], birth_date=cf.cleaned_data['birth_date'])
                # print(cf.cleaned_data['username'])
                savecf.save()
                return HttpResponse('Save success')
            else:
                return HttpResponse('not POST')


class hotel_image_view(APIView):
    def get(self, request):
        form = HotelForm
        return render(request, 'student/image.html', {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = HotelForm(request.POST, request.FILES)
            if form.is_valid():
                savecf = Hotel(
                    name=form.cleaned_data['name'], hotel_Main_Img=form.cleaned_data['hotel_Main_Img'])
                savecf.save()
                return HttpResponse('Save success')
            else:
                return HttpResponse('not POST')


class ProfileAPI(APIView):
    def get(self, request):
        # usernames = [profile.username for profile in Profile.objects.all()] get username
        profile = Profile.objects.all()
        serializer_class = Profile_Seroalzers(profile, many=True)
        return Response(serializer_class.data)

# def hotel_image_view(request):

#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return HttpResponse('Save success')
#     else:
#         form = HotelForm()
#     return render(request, 'student/image.html', {'form': form})


# def success(request):
#     return HttpResponse('successfully uploaded')
