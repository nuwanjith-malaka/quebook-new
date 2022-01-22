from django import forms
from .models import Question, QuestionComment

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['body', 'tag']
        widgets = {
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Your Question' }),
            'tag':forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tag' })
        }
class QuestionCommentForm(forms.ModelForm):
    class Meta:
        model = QuestionComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'cols':30, 'rows':3, 'class': 'form-control', 'placeholder': 'Type Your Comment' }),
        }