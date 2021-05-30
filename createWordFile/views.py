from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Document
from django.urls import reverse_lazy
from docx import Document as docx_doc
from django.http import HttpResponse, HttpResponseNotFound
from html.parser import HTMLParser

# Create your views here.
class Index(ListView):
    model = Document
    template_name = 'home/index.html'

class ViewFile(UpdateView):
     model = Document
     template_name = 'details/index.html'
     fields = '__all__'

class EditFile(UpdateView):
     model = Document
     template_name = 'edit/index.html'
     fields = ['content']
     success_message = 'File updated successfully'
     success_url = '/'

class CreateFile(CreateView):
     model = Document
     template_name = 'create/index.html'
     fields = '__all__'

class DeleteFile(DeleteView):
     model = Document
     template_name = 'document_confirm_delete.html'
     success_url = reverse_lazy('index')

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


def downloadFile(filename, content):
        doc = docx_doc()
        parser = MyHTMLParser()
        preHTML = '<html><head><title>Test</title></head><body>'
        postHTML = '</body></html>'
        print(parser.feed(preHTML+content+postHTML))
        doc.add_paragraph(content)
        doc.save('{0}.docx'.format(filename))

        file_location = './{0}.docx'.format(filename)

        try:
            # sending response 
            fo=open(file_location, 'rb')
            data=fo.read()
            response = HttpResponse(data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingm')
            response['Content-Disposition'] = 'attachment; filename={0}.docx'.format(filename)
            return response

        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound('<h1>File not exist</h1>')

        return response

class Download(View):
    model = Document
    def get(self, request, pk):
        print('-------------- {0}'.format(pk))
        # key=pk
        content = Document.objects.filter(pk=pk)
        return downloadFile(pk, content[0].content)
