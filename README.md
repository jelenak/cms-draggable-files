## CMS Draggable Files

This application will recieve dragged files on django-cms placeholder and save them to cms.plugin.picture or cms.plugin.file. This plugin checks what file extension is dragged.

This application will make Yours life esier.

## Tutorial:
- Install aplication:
pip install cms-draggable-files

- Add to installed app:
'cms_draggable_files'

- Add to base.html (to main html file in your project):
<link rel="stylesheet" type="text/css" href="{% static "css/placeholder.css" %}">
<script type="text/javascript" src="{% static "js/draggable.js" %}"></script>

- Copy template folder instance to your main project folder. Be shour that placeholder.html from cms_draggable_files is in your template/cms/placeholder.html.

Enjoy drag and drop files future in django-cms.





