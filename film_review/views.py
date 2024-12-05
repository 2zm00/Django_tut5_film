from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Review, Comment
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.views import generic
# Create your views here.

def review_list(request):
    # 리뷰 목록
    reviews = Review.objects.select_related('film', 'author').all()
    context = {
        'reviews':reviews
    }
    return render(request, 'film_review/review_list.html',context)

def review_detail(request, pk):
    # Comment를 이후에 추가
    review = Review.objects.select_related('film', 'author').get(pk=pk)
    context = {'review':review}
    return render(request, 'film_review/review_detail.html', context)

@login_required
def review_create(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.film = film
            review.save()
            return redirect('review-detail', pk=review.pk)
    else:
        form = ReviewForm(initial={'film': film})
    
    return render(request, 'film_review/review_form.html', {
        'form': form,
        'film': film
    })

class FilmListView(generic.ListView):
    model = Film
    template_name = 'film_review/film_list.html'
    context_object_name = 'films'
    paginate_by = 12

    def get_queryset(self):
        queryset = Film.objects.all()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset.order_by('title')