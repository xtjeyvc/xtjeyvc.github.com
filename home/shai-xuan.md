### 廉政意见批量筛选工具

廉政意见批量筛选工具主要是通过数据对比，将符合条件的结果筛选出来，这个工具主要是两个功能：

1、筛选数据
2、表格数据导出为固定格式文本（类似邮件合并）

#### 一、原理

**任何OA系统本质上都是数据库，使用方法上基本上都是导出EXCEL表格，然后进行筛选操作，**在日常的工作之中，一个内容不同格式可能会反反复复的调用，几十甚至上百遍，要解决这样的一个基层问题，首先要作好数据的存储和提取工作，这个是基本的，也是最重要的部分，只有数据准确，后续的统计、分析工作才能是建立在牢固的地基之上，否则就是造报表。

#### 二、实例

1、收到任务要对于一批党员领导干部的信访情况进行筛选，筛选名单提供了姓名和身份证号

2、要将本地数据库与筛选名单进行对比，如果本地数据库与筛选名单一致，则形成一个结果名单，模板里是以第二列数据作为对比项

#### 三、注意事项

1、对于VBA有一些了解

2、该工具对于信访和案管部门需要大批量进行数据对比筛选的是非常有帮助的，效率至少可以提升80%

3、该工具可以衍生一些变体，比如根据台账生成固定格式文书。

4、要考虑好对比的数列，一般是身份证号或者是姓名。如果是对比姓名则需要二次筛选，因为可能会涉及到重名的问题。



下载地址：纪检工作笔记 公众号回复：筛选工具

#### 四、源代码

1、筛选代码

```
Sub CompareAndCopyColumns()
    Dim ws1 As Worksheet, ws2 As Worksheet, ws3 As Worksheet
    Dim lastRow1 As Long, lastRow2 As Long, i As Long, j As Long
    Dim found As Boolean
    
    ' 设置工作表变量
    Set ws1 = ThisWorkbook.Sheets("表1") ' 请根据实际工作表名称修改
    Set ws2 = ThisWorkbook.Sheets("表2") ' 请根据实际工作表名称修改
    Set ws3 = ThisWorkbook.Sheets.Add(After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count)) ' 创建新工作表（表3）
    ws3.Name = "表3" ' 设置新工作表的名称
    
    ' 获取表1和表2的最后一行
    lastRow1 = ws1.Cells(ws1.Rows.Count, 2).End(xlUp).Row
    lastRow2 = ws2.Cells(ws2.Rows.Count, 2).End(xlUp).Row
    
    ' 复制表1的表头到表3
    ws1.Rows(1).Copy Destination:=ws3.Range("A1")
    
    ' 遍历表1的第二列，查找匹配项并复制到表3
    For i = 2 To lastRow1 ' 从第2行开始，假设第1行为表头
        found = False
        For j = 2 To lastRow2 ' 遍历表2的第二列
            If InStr(1, ws1.Cells(i, 2).Value, ws2.Cells(j, 2).Value, vbTextCompare) > 0 Then  ' 需要更改数据的可以把这个地方进行修改，ws1.Cells(i, 2)为表1的第2列，ws2.Cells(j, 2)为表2的第2列，要进行对比哪一列需要进行修改，默认都是第二列
                found = True
                Exit For ' 匹配到后退出循环
            End If
        Next j
        
        If found Then ' 如果找到匹配项，则复制整行到表3
            ws1.Rows(i).Copy Destination:=ws3.Range("A" & ws3.Cells(ws3.Rows.Count, 1).End(xlUp).Row + 1)
        End If
    Next i
    
    MsgBox "比较并复制完成，请查看表3。", vbInformation, "完成"
End Sub
```

2、导出文本代码

```
Sub ExportToWord()
    Dim objWord As Object
    Dim objDoc As Object
    Dim rng As Object
    Dim lastRow As Long
    Dim i As Long
    
    ' 设置Excel最后一行的变量
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    ' 创建Word对象
    Set objWord = CreateObject("Word.Application")
    objWord.Visible = True ' 设置Word可见，便于观察过程
    
    ' 新建Word文档
    Set objDoc = objWord.Documents.Add
    
    ' 遍历Excel表格中的每一行
    For i = 2 To lastRow ' 假设第一行为标题，从第二行开始
        ' 在Word中添加新段落并写入数据
        Set rng = objDoc.Content
        rng.InsertAfter "序号、 " & Cells(i, 1).Value & " 收到关于 " & Cells(i, 2).Value & " 的事，交给 " & Cells(i, 3).Value & " 去干。" & vbCrLf ' 换行,1、2、3这个数字是需要修改为对应的单元格的列数
    Next i
    
    MsgBox "数据已导出到Word文档！", vbInformation, "完成"
    
    ' 清理对象
    Set objDoc = Nothing
    Set objWord = Nothing
End Sub
```