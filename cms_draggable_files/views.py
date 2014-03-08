# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, render_to_response
from .forms import FileForm

from cms.plugins.picture.models import Picture
from cms.models import Placeholder
from cms.api import add_plugin
from cms.models import Page

EXECUTABLE_FILE_EXTENSIONS = (
            '.ade', '.adp', '.bas', '.bat', '.chm', '.cmd',
            '.com', '.cpl', '.crt', '.dll', '.exe', '.hlp',
            '.hta', '.inf', '.ins', '.isp', '.js', '.jse',
            '.lnk', '.mdb', '.mde', '.msc', '.msi', '.msp',
            '.mst', '.osc', '.pcd', '.pif', '.pot', '.ppt', 
            '.reg', '.scr', '.sct', '.shb', '.shs', '.sys',
            '.url', '.vb', '.vbe', '.vbs', '.wsc', '.wsf', 
            '.wsh'
            )

PICTURE_EXTENSIONS = (
        '.png', '.jpg', '.bmp', '.tiff', '.jpeg', '.PNG', '.JPG', '.PMB', '.TIFF', '.JEPG'
    )

class BaseCreator(object):
    """ Class that is responsible of creating plugins from drag-uploaded files. 
    This class has to return True/False via is_valid method if file is applicable (I.E. by checking extension)
    And to return created plugin object when called with process() method
    """
    def __init__(self, page, placeholder, current_language, dragged_file):
        self.page = page
        self.placeholder = placeholder
        self.current_language = current_language
        self.dragged_file = dragged_file
        
    """ Method to check, if self.dragged_file is applicable to Creator plugin """  
    def is_valid(self):
        raise Exception('Not implemented!')
    
    """ Method to handle uploaded file """  
    def process(self):
        raise Exception('Not implemented!')
    
    class Meta:
        abstract = True

class PictureCreator(BaseCreator):
    
    def is_valid(self):
        dragged_file = str(self.dragged_file)
        for pic_extension in PICTURE_EXTENSIONS:
            if dragged_file.endswith(pic_extension):
                return True 
 
        else: 
            return False          

         
    def process(self):
        return add_plugin(self.placeholder, "PicturePlugin", self.current_language, image=self.dragged_file)


class FileCreator(BaseCreator):
    
    def is_valid(self):
        dragged_file = str(self.dragged_file)
        for ex_file in EXECUTABLE_FILE_EXTENSIONS:
            if dragged_file.endswith(ex_file):
                return False
        else: 
            return True         
         
    def process(self):
        return add_plugin(self.placeholder, "FilePlugin", self.current_language, file=self.dragged_file)



DRAGGABLE_PLUGIN_CREATORS = [
    PictureCreator,
    FileCreator
]


def file_upload(request):
    current_language = request.LANGUAGE_CODE
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        page = Page.objects.get(id=request.POST['page'])      
        placeholder = Placeholder.objects.get(pk=request.POST['placeholder_pk'])
        for dragged_file in request.FILES.getlist('dragged_files'):
            for creator in DRAGGABLE_PLUGIN_CREATORS:
                creator_instance = creator(page, placeholder, current_language, dragged_file)
                if creator_instance.is_valid():
                    creator_instance.process()
                    break
                
    else:
        form = FileForm()
    return render_to_response('index.html', { 
                                             'form': form 
                                            },
        context_instance=RequestContext(request)
    )
    


