from django.urls import reverse
from django.shortcuts import render, redirect
from votes.models import QuestionDownVote, QuestionUpVote
from question.models import Question
from .models import AskerProfile
from django.contrib.auth.models import User
from .forms import AskerProfileForm
from django.views.generic.edit import UpdateView
# Create your views here.
def AskerView(request, pk):
    user = User.objects.get(id=pk)
    questions = Question.objects.filter(user=user)
    for question in questions:
        question.upvotes = QuestionUpVote.objects.filter(
            question=question).count()
        question.downvotes = QuestionDownVote.objects.filter(
            question=question).count()
    context = {
        'questions': questions,
    }
    if request.method == 'POST':
        form = AskerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            asker_profile = form.save(commit=False)
            asker_profile.user = request.user
            asker_profile.save()
        return redirect('asker', pk=pk)
    else:
        try:
            asker = AskerProfile.objects.get(user=user)
            context = {
                'questions': questions,
                'asker': asker,

            }
            return render(request, 'user/asker.html', context)
        except AskerProfile.DoesNotExist:
            if user == request.user:
                form = AskerProfileForm()
                context = {
                    'questions': questions,
                    'form': form,
                    'user': user

                }
            else:
                context = {
                    'questions': questions,
                    'user': user

                }
            return render(request, 'user/asker.html', context)

# def EditProfileView(request, pk):
#     asker = AskerProfile.objects.get(id=pk)
#     user = asker.user
#     if request.method == 'POST':
#         form = AskerProfileForm(request.POST, request.FILES, instance=asker)
#         if form.is_valid():
#             form.save()
#             return redirect('asker', pk=user.pk)
#     else:
#         form = AskerProfileForm(instance=asker)
#     return render(request, 'user/edit_profile.html', {'form': form, 'asker': asker, 'user': user})


class EditProfileView(UpdateView):
    model = AskerProfile
    form_class = AskerProfileForm
    template_name = 'user/edit_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['asker'] = self.get_object()
        context['user'] = self.get_object().user
        return context