from django import forms
from .models import ImageUploadModel

# # Django에서 제공하는 ModelForm을 활용해 form 구성
# class PostForm(forms.ModelForm):
#
#     # Form을 통해 받아들여야할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결)
#     class Meta:
#         model = GuessNumbers
#         fields = ('name', 'text',) # 사용자로부터 form 통해 입력받을 데이터

#원래는 위와같은 형태였으나 밑의 경우는 모델폼이 아니라 그냥 빈양식의 폼이라고 생각

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    # ImageField Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
    # file = forms.FileField()
    image = forms.ImageField()


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document',)
