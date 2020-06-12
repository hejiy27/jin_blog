from django import forms

from.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = ['username', 'first_name','last_name','email']
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '15자 이내로 입력 가능합니다'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(),
        }
        labels = {
            'username': '아이디',
            'email': '이메일',
            'password': '비밀번호',
            'confirm_password': '비밀번호 확인'
        }

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!')

        return cd['confirm_password']