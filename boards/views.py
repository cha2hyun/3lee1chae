from django.shortcuts import render
from .models import Board
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect


# Create your views here.


class BoardListView(ListView):
    model = Board
    template_name = 'board/list.html'


class BoardUploadView(CreateView):
    model = Board
    fields = [
        'photo', 'text', 'date'
    ]
    template_name = 'board/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/boards')
        else:
            return self.render_to_response({'form': form})


class BoardDeleteView(DeleteView):
    model = Board
    success_url = '/boards'
    template_name = 'board/delete.html'


class BoardUpdateView(UpdateView):
    model = Board
    fields = ['photo', 'text', 'date']
    template_name = 'board/update.html'
    success_url = '/boards'


class BoardDetailView(DetailView):
    model = Board
    template_name = 'board/detail.html'
