## CMS Draggable Files

This application will recieve dragged files on django-cms placeholder and save them to cms.plugin.picture or cms.plugin.file. This plugin checks what file extension is dragged.

This application will make Yours life esier.

## Tutorial:
- Install aplication:
pip install cms-draggable-files

- Add to installed app:
'cms_draggable_files'

- Add static files to base.html (or to main html file in your project):
**/static/css/placeholder.css
/static/js/draggable.js**

- Copy template folder instance to your main project folder. Be shour that placeholder.html from cms_draggable_files is in your template/cms/placeholder.html.

- Add cms-draggable-files to your project urls.py:
  $ url(r'^', include('cms_draggable_files.urls')),

- If You want additional custom file creator that for example will convert files from odf to pdf on drag and drop, You need in settings register your custom creator class:
  DRAGGABLE_ADDITIONAL_PLUGIN_CREATORS = [ ODF_TO_PDF_CREATOR, ]

Enjoy drag and drop files future in django-cms.





