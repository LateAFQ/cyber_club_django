from django.shortcuts import get_object_or_404
from main.models import Text_Photo

txt_img = get_object_or_404(Text_Photo, pk=1)