from django.contrib import admin

# Register your models here.

from .models import Class, Student


class StudentInfo(admin.TabularInline):
    model = Student
    extra = 2


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin) :
    inlines = [StudentInfo]
    # 列表页属性
    # 显示字段
    def isDelete(self):
        if self.isDelete:
            return 'YES'
        else :
            return 'NOT'
    list_display = ['pk', 'gname','gdate', 'gBoyNum', 'gGrilNum', isDelete]
    # # 添加过滤字段
    list_filter = ['gname' ]
    # # 添加查找框
    search_fields = ['gname']
    # 添加分页, 5表示分页的数量,超过5时会分页
    list_per_page = 5


    # 添加、修改页属性,这里时修改页的属性
    # fields = ['gname','gdate', 'gBoyNum', 'gGrilNum', 'isDelete'] # 可以修改修改时的顺序
    # # 给属性添加分组
    fieldsets = [
        ("num", {'fields':['gBoyNum', 'gGrilNum']}),
        ('BasicInfo', {'fields':['gname','gdate', 'isDelete']})
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sGender:
            return 'Male'
        else:
            return 'Female'
    def isDelete(self):
        if self.isDelete:
            return 'YES'
        else :
            return "NOT"
    gender.short_description = 'Student Gender'
    list_display = ['pk', 'sName', gender, 'sAge', 'sSummary', 'sClass', 'sScore', isDelete]
    list_filter = ['sName', 'sGender', 'sAge', 'sClass', 'sScore']
    search_fields = ['sName', 'sGender', 'sAge', 'sClass', 'sScore']
    list_per_page = 5
    # fields = ['sName', 'sGender', 'sAge', 'sSummary', 'sClass', 'sScore', 'isDelete']
    fieldsets = [
        ('num', {'fields':['sAge', 'sScore']}),
        ('BasicInfo', {'fields': ['sName', 'sClass', 'isDelete']})
    ]


# admin.site.register(Class, ClassAdmin)
# admin.site.register(Student, StudentAdmin)