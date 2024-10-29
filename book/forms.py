from django import forms

from book.models import SysUser


# 单纯的表单验证
class BookForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=50, label="标题",
                            error_messages={
                                'min_length': '最小长度',
                                'max_length': '大长度'
                            })


# 继承 数据库模型，进行校验
class UserForm(forms.ModelForm):
    class Meta:
        model = SysUser
        # fields = '__all__'
        fields = ('name', 'age')
