from django.shortcuts import render, redirect
from studentsapp.models import student,FCN
from studentsapp.forms import PostForm
from studentsapp.filters import FCNFilter

def listone(request,id=None): 
	x=0
	y=0
	unit = FCN.objects.get(id=id) #讀取一筆資料
	#unit = FCN.objects.get(id=1)
	unit1 = FCN.objects.all()
	for o in unit1:
		if o.cinvestor==unit.cinvestor:
			if o.cCND!=None:
				x=x+o.cCND
			if o.cUSD!=None:
				y=y+o.cUSD
	unit.cCND=x
	unit.cUSD=y
	
	return render(request, "listone.html", locals())

def listall(request):  
	students = FCN.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
	return render(request, "listall.html", locals())
	
def index(request):  
	students = student.objects.all().order_by('id')#讀取資料表, 依 id 遞增排序
	FCNs = FCN.objects.all().order_by('id')
	return render(request, "index.html", locals())
	
def post(request):
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
	else:
		mess="表單資料尚未送出!"	
	return render(request, "post.html", locals())
	
def post1(request):  #新增資料，資料不作驗證
	if request.method == "POST":	  #如果是以POST方式才處理
		cbank = request.POST['cbank'] #取得表單輸入資料
		cinvestor =  request.POST['cinvestor']
		ctradingDay =  request.POST['ctradingDay']
		creleaseDay = request.POST['creleaseDay']
		cexpiryDay =  request.POST['cexpiryDay']
		cransomDay =  request.POST['cransomDay']
		cfinalEvaluation = request.POST['cfinalEvaluation'] 
		corder =  request.POST['corder']
		cCND =  request.POST['cCND']
		cUSD = request.POST['cUSD']
		crate =  request.POST['crate']
		cstock1Exist =  request.POST['cstock1Exist']
		cstock1 = request.POST['cstock1']
		cstock1KOPrice =  request.POST['cstock1KOPrice']
		cstock1StartPrice =  request.POST['cstock1StartPrice']
		cstock1TranformPrice =  request.POST['cstock1TranformPrice']
		cstock2Exist =  request.POST['cstock2Exist']
		cstock2 = request.POST['cstock2']
		cstock2KOPrice =  request.POST['cstock2KOPrice']
		cstock2StartPrice =  request.POST['cstock2StartPrice']
		cstock2TranformPrice =  request.POST['cstock2TranformPrice']
		cstock3Exist =  request.POST['cstock3Exist']
		cstock3 = request.POST['cstock3']
		cstock3KOPrice =  request.POST['cstock3KOPrice']
		cstock3StartPrice =  request.POST['cstock3StartPrice']
		cstock3TranformPrice =  request.POST['cstock3TranformPrice']
		cstock4Exist =  request.POST['cstock4Exist']
		cstock4 = request.POST['cstock4']
		cstock4KOPrice =  request.POST['cstock4KOPrice']
		cstock4StartPrice =  request.POST['cstock4StartPrice']
		cstock4TranformPrice =  request.POST['cstock4TranformPrice']
		cobservationTime1 =  request.POST['cobservationTime1']
		cobservationTimeEnd1 =  request.POST['cobservationTimeEnd1']
		cdeliveryDate1 =  request.POST['cdeliveryDate1']
		cobservationTime2 =  request.POST['cobservationTime2']
		cobservationTimeEnd2 =  request.POST['cobservationTimeEnd2']
		cdeliveryDate2 =  request.POST['cdeliveryDate2']
		cobservationTime3 =  request.POST['cobservationTime3']
		cobservationTimeEnd3 =  request.POST['cobservationTimeEnd3']
		cdeliveryDate3 =  request.POST['cdeliveryDate3']
		cobservationTime4 =  request.POST['cobservationTime4']
		cobservationTimeEnd4 =  request.POST['cobservationTimeEnd4']
		cdeliveryDate4 =  request.POST['cdeliveryDate4']
		cobservationTime5 =  request.POST['cobservationTime5']
		cobservationTimeEnd5 =  request.POST['cobservationTimeEnd5']
		cdeliveryDate5 =  request.POST['cdeliveryDate5']
		cobservationTime6 =  request.POST['cobservationTime6']
		cobservationTimeEnd6 =  request.POST['cobservationTimeEnd6']
		cdeliveryDate6 =  request.POST['cdeliveryDate6']
		cobservationTime7 =  request.POST['cobservationTime7']
		cobservationTimeEnd7 =  request.POST['cobservationTimeEnd7']
		cdeliveryDate7 =  request.POST['cdeliveryDate7']
		cobservationTime8 =  request.POST['cobservationTime8']
		cobservationTimeEnd8 =  request.POST['cobservationTimeEnd8']
		cdeliveryDate8 =  request.POST['cdeliveryDate8']
		cobservationTime9 =  request.POST['cobservationTime9']
		cobservationTimeEnd9 =  request.POST['cobservationTimeEnd9']
		cdeliveryDate9 =  request.POST['cdeliveryDate9']
		cobservationTime10 =  request.POST['cobservationTime10']
		cobservationTimeEnd10 =  request.POST['cobservationTimeEnd10']
		cdeliveryDate10 =  request.POST['cdeliveryDate10']
		cobservationTime11 =  request.POST['cobservationTime11']
		cobservationTimeEnd11 =  request.POST['cobservationTimeEnd11']
		cdeliveryDate11 =  request.POST['cdeliveryDate11']
		cobservationTime12 =  request.POST['cobservationTime12']
		cobservationTimeEnd12 =  request.POST['cobservationTimeEnd12']
		cdeliveryDate12 =  request.POST['cdeliveryDate12']
		if cCND =='':
			cCND =None
		if cUSD =='':
			cUSD =None
		if crate =='':
			crate =None
		if cstock1KOPrice =='':
			cstock1KOPrice =None
		if cstock1StartPrice =='':
			cstock1StartPrice =None
		if cstock1TranformPrice =='':
			cstock1TranformPrice =None
		if cstock2KOPrice =='':
			cstock2KOPrice =None
		if cstock2StartPrice =='':
			cstock2StartPrice =None
		if cstock2TranformPrice =='':
			cstock2TranformPrice =None
		if cstock3KOPrice =='':
			cstock3KOPrice =None
		if cstock3StartPrice =='':
			cstock3StartPrice =None
		if cstock3TranformPrice =='':
			cstock3TranformPrice =None
		if cstock4KOPrice =='':
			cstock4KOPrice =None
		if cstock4StartPrice =='':
			cstock4StartPrice =None
		if cstock4TranformPrice =='':
			cstock4TranformPrice =None
		if cobservationTime1 =='':
			cobservationTime1 =None
		if cobservationTimeEnd1 =='':
			cobservationTimeEnd1 =None
		if cdeliveryDate1 =='':
			cdeliveryDate1 =None
		if cobservationTime2 =='':
			cobservationTime2 =None
		if cobservationTimeEnd2 =='':
			cobservationTimeEnd2 =None
		if cdeliveryDate2 =='':
			cdeliveryDate2 =None
		if cobservationTime3 =='':
			cobservationTime3 =None
		if cobservationTimeEnd3 =='':
			cobservationTimeEnd3 =None
		if cdeliveryDate3 =='':
			cdeliveryDate3 =None
		if cobservationTime4 =='':
			cobservationTime4 =None
		if cobservationTimeEnd4 =='':
			cobservationTimeEnd4 =None
		if cdeliveryDate4 =='':
			cdeliveryDate4 =None
		if cobservationTime5 =='':
			cobservationTime5 =None
		if cobservationTimeEnd5 =='':
			cobservationTimeEnd5 =None
		if cdeliveryDate5 =='':
			cdeliveryDate5 =None
		if cobservationTime6 =='':
			cobservationTime6 =None
		if cobservationTimeEnd6 =='':
			cobservationTimeEnd6 =None
		if cdeliveryDate6 =='':
			cdeliveryDate6 =None
		if cobservationTime7 =='':
			cobservationTime7 =None
		if cobservationTimeEnd7 =='':
			cobservationTimeEnd7 =None
		if cdeliveryDate7 =='':
			cdeliveryDate7 =None
		if cobservationTime8 =='':
			cobservationTime8 =None
		if cobservationTimeEnd8 =='':
			cobservationTimeEnd8 =None
		if cdeliveryDate8 =='':
			cdeliveryDate8 =None
		if cobservationTime9 =='':
			cobservationTime9 =None
		if cobservationTimeEnd9 =='':
			cobservationTimeEnd9 =None
		if cdeliveryDate9 =='':
			cdeliveryDate9 =None
		if cobservationTime10 =='':
			cobservationTime10 =None
		if cobservationTimeEnd10 =='':
			cobservationTimeEnd10 =None
		if cdeliveryDate10 =='':
			cdeliveryDate10 =None
		if cobservationTime11 =='':
			cobservationTime11 =None
		if cobservationTimeEnd11 =='':
			cobservationTimeEnd11 =None
		if cdeliveryDate11 =='':
			cdeliveryDate11 =None
		if cobservationTime12 =='':
			cobservationTime12 =None
		if cobservationTimeEnd12 =='':
			cobservationTimeEnd12 =None
		if cdeliveryDate12 =='':
			cdeliveryDate12 =None
		#新增一筆記錄
		unit = FCN.objects.create(cbank=cbank, cinvestor=cinvestor, ctradingDay=ctradingDay, creleaseDay=creleaseDay,cexpiryDay=cexpiryDay, cransomDay=cransomDay,cfinalEvaluation=cfinalEvaluation, corder=corder, cCND=cCND, cUSD=cUSD,crate=crate, cstock1Exist=cstock1Exist, cstock1=cstock1, cstock1KOPrice=cstock1KOPrice,cstock1StartPrice=cstock1StartPrice, cstock1TranformPrice=cstock1TranformPrice, cstock2Exist=cstock2Exist, cstock2=cstock2, cstock2KOPrice=cstock2KOPrice,cstock2StartPrice=cstock2StartPrice, cstock2TranformPrice=cstock2TranformPrice, cstock3Exist=cstock3Exist, cstock3=cstock3, cstock3KOPrice=cstock3KOPrice,cstock3StartPrice=cstock3StartPrice, cstock3TranformPrice=cstock3TranformPrice, cstock4Exist=cstock4Exist, cstock4=cstock4, cstock4KOPrice=cstock4KOPrice,cstock4StartPrice=cstock4StartPrice, cstock4TranformPrice=cstock4TranformPrice, cobservationTime1=cobservationTime1, cobservationTimeEnd1=cobservationTimeEnd1, cdeliveryDate1=cdeliveryDate1, cobservationTime2=cobservationTime2, cobservationTimeEnd2=cobservationTimeEnd2, cdeliveryDate2=cdeliveryDate2, cobservationTime3=cobservationTime3, cobservationTimeEnd3=cobservationTimeEnd3, cdeliveryDate3=cdeliveryDate3, cobservationTime4=cobservationTime4, cobservationTimeEnd4=cobservationTimeEnd4, cdeliveryDate4=cdeliveryDate4, cobservationTime5=cobservationTime5, cobservationTimeEnd5=cobservationTimeEnd5, cdeliveryDate5=cdeliveryDate5, cobservationTime6=cobservationTime6, cobservationTimeEnd6=cobservationTimeEnd6, cdeliveryDate6=cdeliveryDate6, cobservationTime7=cobservationTime7, cobservationTimeEnd7=cobservationTimeEnd7, cdeliveryDate7=cdeliveryDate7, cobservationTime8=cobservationTime8, cobservationTimeEnd8=cobservationTimeEnd8, cdeliveryDate8=cdeliveryDate8, cobservationTime9=cobservationTime9, cobservationTimeEnd9=cobservationTimeEnd9, cdeliveryDate9=cdeliveryDate9, cobservationTime10=cobservationTime10, cobservationTimeEnd10=cobservationTimeEnd10, cdeliveryDate10=cdeliveryDate10, cobservationTime11=cobservationTime11, cobservationTimeEnd11=cobservationTimeEnd11, cdeliveryDate11=cdeliveryDate11, cobservationTime12=cobservationTime12, cobservationTimeEnd12=cobservationTimeEnd12, cdeliveryDate12=cdeliveryDate12) 
		unit.save()  #寫入資料庫
		return redirect('/index/')	
	else:
		message = '請輸入資料(資料不作驗證)'
	return render(request, "post1.html", locals())	
	
def post2(request):  #新增資料，資料必須驗證
	if request.method == "POST":  #如果是以POST方式才處理
		postform = PostForm(request.POST)  #建立forms物件
		if postform.is_valid():			#通過forms驗證
			cName = postform.cleaned_data['cName'] #取得表單輸入資料
			cSex =  postform.cleaned_data['cSex']
			cBirthday =  postform.cleaned_data['cBirthday']
			cEmail = postform.cleaned_data['cEmail']
			cPhone =  postform.cleaned_data['cPhone']
			cAddr =  postform.cleaned_data['cAddr']
			#新增一筆記錄
			unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
			unit.save()  #寫入資料庫
			message = '已儲存...'
			return redirect('/index/')	
		else:
			message = '驗證碼錯誤！'	
	else:
		message = '姓名、性別、生日必須輸入！'
		postform = PostForm()
	return render(request, "post2.html", locals())		
		
def delete(request,id=None):  #刪除資料
	if id!=None:
		if request.method == "POST":  #如果是以POST方式才處理
			id=request.POST['cId'] #取得表單輸入的編號
		try:
			unit = student.objects.get(id=id)  
			unit.delete()
			return redirect('/index/')
		except:
			message = "讀取錯誤!"			
	return render(request, "delete.html", locals())	
	
def edit(request,id=None,mode=None):  
	if mode == "edit":  # 由 edit.html 按 submit
		unit = student.objects.get(id=id)  #取得要修改的資料記錄	
		unit.cName=request.GET['cName']
		unit.cSex=request.GET['cSex']
		unit.cBirthday=request.GET['cBirthday']
		unit.cEmail=request.GET['cEmail']
		unit.cPhone=request.GET['cPhone']
		unit.cAddr=request.GET['cAddr']		
		unit.save()  #寫入資料庫
		message = '已修改...'
		return redirect('/index/')	
	else: # 由網址列
		try:
			unit = student.objects.get(id=id)  #取得要修改的資料記錄
			strdate=str(unit.cBirthday)
			strdate2=strdate.replace("年","-")
			strdate2=strdate.replace("月","-")
			strdate2=strdate.replace("日","-")
			unit.cBirthday = strdate2
		except:
			message = "此 id不存在！"	
		return render(request, "edit.html", locals())	
		
def edit2(request,id=None,mode=None):
    if mode == "load":  # 由 index.html 按 編輯二 鈕
      unit = student.objects.get(id=id)  #取得要修改的資料記
      strdate=str(unit.cBirthday)
      strdate2=strdate.replace("年","-")
      strdate2=strdate.replace("月","-")
      strdate2=strdate.replace("日","-")
      unit.cBirthday = strdate2		
      return render(request, "edit2.html", locals())
    elif mode == "save": # 由 edit2.html 按 submit		
      unit = student.objects.get(id=id)  #取得要修改的資料記錄	
      unit.cName=request.POST['cName']
      unit.cSex=request.POST['cSex']
      unit.cBirthday=request.POST['cBirthday']
      unit.cEmail=request.POST['cEmail']
      unit.cPhone=request.POST['cPhone']
      unit.cAddr=request.POST['cAddr']		
      unit.save()  #寫入資料庫
      message = '已修改...'
      return redirect('/index/')
	  
def postform(request):  #新增資料，資料必須驗證
	postform = PostForm()  #建立PostForm物件
	return render(request, "postform.html", locals())		  

def selected(request):
    sname = FCN.objects.all()
    fcnFilter = FCNFilter(queryset=sname)
    if request.method == "POST":
        fcnFilter = FCNFilter(request.POST, queryset=sname)
    context = {
        'fcnFilter': fcnFilter
    }
    return render(request, 'selected.html', context)
