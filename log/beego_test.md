### 创建一个博客
```
bee new beebolg
```

### html打印
```
<div>
{{str2html .Html}}
</div>
```

### 模板嵌套
```
<html>
    <body>
        <div>
        {{template "test"}}
        </div>
    </body>
</html>

{{define "test"}}
<div>
this is test
</div>
{{end}}
```

### 目录
```
//等同于--"../data/txt/login.txt
/static/js/bootstrap.min.js
```


