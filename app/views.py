from django.shortcuts import render,redirect
from app.models import Movie,Profiles
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm


# ProfileForm00
class Home(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect(to='app:profile_list')
        return render(request,'index.html')


@method_decorator(login_required,name='dispatch')
class ProfileList(View):

    def get(self,request,*args,**kwargs):

        profiles=request.user.profiles.all()

        print(profiles)
        context = {
            'profiles':profiles
        }

        return render(request,'profileList.html',context)



class ProfileCrete(View):
    def get(self,request,*args,**kwargs):
        form=ProfileForm()
        return render(request,'profileCreate.html',{'form':form})
        
    def post(self,request,*args,**kwargs):
        form = ProfileForm(request.POST or None)

        if form.is_valid():
            print(form.cleaned_data)
            profile = Profiles.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect(f'/watch={profile.uuid}')
        
        return render(request,'profileCreate.html',{
            'form':form
        })



@method_decorator(login_required,name='dispatch')
class Watch(View):
    def get(self,request,profile_id,*args,**kwargs):
        try:
            profile = Profiles.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            print(len(movies))
            try:
                showcase = movies[0]
            except :
                showcase = None

            if profile not in request.user.profiles.all():
                return redirect(to='app:profile_list')
            return render(request,'movieList.html',{
                'movies':movies,
                "show_case": showcase
            })
        except Profiles.DoesNotExist:
            return redirect(to='app:profile_list')

@method_decorator(login_required, name='dispatch')  
class ShowMovieDeatil(View):
    def get(self,request,movie_id,*args,**kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)

            return render(request,'movieDetail.html',{
                'movie':movie
            })
        except Movie.DoesNotExist:
            return redirect('app:profile_list')


class ShowMove(View):
    def get(self,request,movie_id,*args,**kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.videos.values()
            context = {
                'movie':list(movie)
            }
            return render(request,'showMovie.html',context)
        except Movie.DoesNotExist:
            return redirect('app:profile_list')






























