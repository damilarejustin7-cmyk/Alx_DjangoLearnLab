from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm # Fixed: Added 'import'
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm # Added: Use your custom forms
from django.db.models import Q

# --- Authentication Views ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

# --- Post Views ---
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date'] # Optional: shows newest first

class PostDetailView(DetailView):
    model = Post
    # Django looks for blog/post_detail.html by default

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm # Requirement: Use form that includes tags

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm # Requirement: Include tags in update

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list') # Redirect to list after delete

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author    

# --- Comment Views ---
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm # Using the CommentForm you developed

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Correctly link to the post using the PK from the URL
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirect back to the post detail page after commenting
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.get_object().post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):    
    model = Comment
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.get_object().post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

# --- Search & Tagging Views (Step 3 & 4) ---
def search_posts(request):
    query = request.GET.get('q')
    if query:
        # Complex lookup using Q objects as required
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Filter posts by tag name from the URL
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__name__iexact=tag_slug)