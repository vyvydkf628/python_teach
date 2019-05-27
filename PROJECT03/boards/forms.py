from django import forms
from .models import Board
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','content',]
        
        def __init__(self,*args,**kwargs ):
            super().__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form.method = 'POST'
            self.helper.add_input(Submit('submit','작성합시다.'))
    # title = forms.CharField(
    #     label = '제목',
    #     widget= forms.TextInput(attrs={
    #         'placeholder' :'The title!',
    #     })
    #     )
    # content = forms.CharField(
    #     label = '내용',
    #     widget = forms.Textarea(attrs={
    #         'class' :'input-content',
    #         'rows': 5,
    #         'cols': 50,
    #         'placeholder' : 'Fill the Content!',
    #     }))