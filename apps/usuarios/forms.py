from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Ex: Cadu Moreira"
            })
        )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
            "placeholder":"Digite sua senha"
            })
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome Completo",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Ex: Cadu Moreira"
            })
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={
            "class":"form-control",
            "placeholder":"exemplo@exemplo.com"
            })
    )
    senha_cadastro = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
            "placeholder":"Digite a sua senha"
            })
    )

    senha_confirmacao = forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
            "placeholder":"Digite a sua senha novamente"
            })
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaço no campo usuário!")
            else:
                return nome
            
    def clean_senha_confirmacao(self):
        senha_cadastro = self.cleaned_data['senha_cadastro']
        senha_confirmacao = self.cleaned_data['senha_confirmacao']

        if senha_cadastro and senha_confirmacao:
            if senha_cadastro != senha_confirmacao:
                raise forms.ValidationError('Senhas diferentes.')
            else:
                return senha_confirmacao