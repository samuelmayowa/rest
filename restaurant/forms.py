from meals.models import Message
from django import forms


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ("your_name", "your_email", "message")

        widget = {
            'name': forms.TextInput(),
            'email': forms.EmailField(max_length=100),
            'message': forms.Textarea(),
        }
