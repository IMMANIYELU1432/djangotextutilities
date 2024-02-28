from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def textutilities(request):
    inputText=request.POST.get('text','default')
    punctuations=request.POST.get('punctuations','off')
    capitalize=request.POST.get('capitalize','off')
    space=request.POST.get('space')
    if punctuations=="on":
        punc='''~`@#$%^&*()_-+={[|\!:;'"<>,./?]}'''
        analyze=""
        for i in inputText:
            if i not in punc:
                analyze=analyze+i
        final_text={"punctuations":"remove punctuations","display":analyze}
        inputText=analyze
    if capitalize=='on':
        analyze=inputText.upper()
        final_text={"capitalize":"capitalize","display":analyze}
        inputText=analyze
    if space=='on':
        s=" "
        analyze=""
        for i in inputText:
            if i not in s:
                analyze=analyze+i
        final_text={"space":"space remove","display":analyze}
    return render(request,'analyze.html',final_text)
   