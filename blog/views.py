from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Importateur
from django.shortcuts import render, get_object_or_404
from .forms import ImportateurForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.shortcuts import render_to_response

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    return render(request, 'blog/home.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def importateur_detail(request, pk):
    importateur = get_object_or_404(Importateur, pk=pk)
    return render(request, 'blog/importateur_detail.html', {'importateur': importateur})

def importateur_list(request):
    importateurlist = Importateur.objects.all()
    paginator = Paginator(importateurlist, 3)

    search = request.session.get('search', {})
    # Si le formulaire a ete soumis :
    if request.method == 'POST' :
    # On reinitialise la variable 'search'

      search = {}
    if ('search_matricule') in request.POST and request.POST.get('search_matricule'):
      search['matricule'] = request.POST.get('search_matricule')
    if ('search_importateur') in request.POST  and request.POST.get('search_importateur'):
      search['importateur'] = 1
    # Et on reinjecte la variable 'search' dans la session
      request.session['search'] = search

    if 'matricule'  in search and search['matricule']:
      importateurlist = importateurlist.filter(matricule__icontains=search['matricule'])
    if 'importateur' in search:
      importateurlist = importateurlist.filter(importateur=search['importateur'])

       
    try:
       page = int(request.GET.get('page', '1'))
    except ValueError:
       page = 1

    try:
       importateurs = paginator.page(page)
    except (EmptyPage, InvalidPage):
       importateurs = paginator.page(paginator.num_pages)

    #return render(request, 'blog/importateur_list.html', {'importateur': importateurlist} )
    return render(request, 'blog/importateur_list.html', { 'importateur': importateurlist , 'context' : RequestContext(request)})




def importateur_new(request):
    if request.method == "POST":
        form = ImportateurForm(request.POST)
        if form.is_valid():
            importateur = form.save(commit=False)
            #importateur.author = request.user
            importateur.created_date = timezone.now()
            importateur.save()
        return redirect('importateur_detail', pk=importateur.pk)
    else:
        form = ImportateurForm()
    return render(request, 'blog/importateur_edit.html', {'form': form})
    




def importateur_edit(request, pk):
    importateur = get_object_or_404(Importateur, pk=pk)
    if request.method == "POST":
        form =ImportateurForm(request.POST, instance=importateur)
        if form.is_valid():
            importateur = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            importateur.save()
            return redirect('importateur_detail', pk=importateur.pk)
    else:
        form = ImportateurForm(instance=importateur)
    return render(request, 'blog/importateur_edit.html', {'form': form})
