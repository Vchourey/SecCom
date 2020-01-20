from django.http import HttpResponse


def home(request):

    text = '''
<html>
<head>
<title> Home page</title>
</head>
<body>
<div class="MenuBar">
  <a class="active" href="/home/">Home</a>
  <a href="/Mylearning/">Learning</a>
  <a href="/market/">Share Market</a>
  <a href="/movies/">Movies</a>
  <a href="/music/">Music</a>
  <a href="/books/">Books</a>  
  <a href="/contact/">Contact</a>
  <a href="/about/">About</a>
</div>

<h3>This is first Home page of Vijay Web</h3>


</body>
</html>'''
    return HttpResponse(text)

