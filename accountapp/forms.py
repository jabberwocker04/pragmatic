from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #UserCreationForm을 상속받은 AccountUpdateForm을 만들어준것임
                                        # 상속받은 것에서 username칸을 비활성화시켜주는것으로 커스텀함
        self.fields['username'].disabled = True
