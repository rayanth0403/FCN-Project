from django.contrib import admin
from studentsapp.models import student,FCN

class studentAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
	list_filter=('cName','cSex')
	search_fields=('cName',)
	ordering=('id',)
	
admin.site.register(student,studentAdmin)

class FCNAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cbank','cinvestor','ctradingDay','creleaseDay','cexpiryDay','cransomDay','cfinalEvaluation','corder','cCND','cUSD','crate','cstock1Exist','cstock1','cstock1KOPrice','cstock1StartPrice','cstock1TranformPrice','cstock2Exist','cstock2','cstock2KOPrice','cstock2StartPrice','cstock2TranformPrice','cstock3Exist','cstock3','cstock3KOPrice','cstock3StartPrice','cstock3TranformPrice','cstock4Exist','cstock4','cstock4KOPrice','cstock4StartPrice','cstock4TranformPrice','cobservationTime1','cobservationTimeEnd1','cdeliveryDate1','cobservationTime2','cobservationTimeEnd2','cdeliveryDate2','cobservationTime3','cobservationTimeEnd3','cdeliveryDate3','cobservationTime4','cobservationTimeEnd4','cdeliveryDate4','cobservationTime5','cobservationTimeEnd5','cdeliveryDate5','cobservationTime6','cobservationTimeEnd6','cdeliveryDate6','cobservationTime7','cobservationTimeEnd7','cdeliveryDate7','cobservationTime8','cobservationTimeEnd8','cdeliveryDate8','cobservationTime9','cobservationTimeEnd9','cdeliveryDate9','cobservationTime10','cobservationTimeEnd10','cdeliveryDate10','cobservationTime11','cobservationTimeEnd11','cdeliveryDate11','cobservationTime12','cobservationTimeEnd12','cdeliveryDate12')
	list_filter=('cbank','cinvestor','creleaseDay')
	search_fields=('cbank','cinvestor','creleaseDay',)
	ordering=('id',)
	
admin.site.register(FCN,FCNAdmin)
	
# 第一種方式，未加入 ModelAdmin 類別 
#admin.site.register(student)

# 第二種方式，加入 ModelAdmin 類別，定義顯示欄位
#class studentAdmin(admin.ModelAdmin):
#	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
#admin.site.register(student,studentAdmin)
