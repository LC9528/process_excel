import os.path
import win32com.client

#VBA programs have existed in excel file
def changeMacro(macro,file):
    if os.path.exists('./test/'+file):
        excel_macro = win32com.client.DispatchEx('Excel.Application')
# whether display excel or not when execute this file
#        excel_macro.Visible = True
        excel_macro.DisplayAlerts = False
        excel_path = os.path.expanduser('./test/'+file)
        wb = excel_macro.Workbooks.Open(Filename=excel_path)
        excel_macro.Run(macro)
#    wb.Save('../test/xx.xlsb')
        wb.Save()
# when you close the file, this file display whether you wanna store it or not. SaveChanges=1 express you're gonna store this.
#    wb.Close(SaveChanges=1)
        wb.Close(0)
        excel_macro.Quit()
        print(macro + "_macro ran successfully!")
        del wb
        del excel_macro

#add new VBA programs into excel file
def addVBA(filename,VBAname):
    #select sheet name is "CUSTOMER" and then control column of pivot table
    vbacode = \
    '''
    Sub REGION()
        Sheets("CUSTOMER").Select
        ActiveSheet.PivotTables("樞紐分析表1").PivotFields("QC_REGION_GROUP").ShowDetail = False   
    End Sub
    '''

    #to check path whether exists file
    if os.path.exists('./test/'+filename):
        excel = win32com.client.DispatchEx('Excel.Application')
      #  excel.Visible = True
        excel.DisplayAlerts = False
        excel_path = ".\\"+filename
        wb = excel.Workbooks.Open(Filename=excel_path)
        ws = wb.Sheets('CUSTOMER')
        if VBAname == 'REGION':
            mod = wb.VBProject.VBComponents.Add(1)
            mod.CodeModule.AddFromString(vbacode.strip())
            excel.Run(VBAname)                     
        else:
            mod = wb.VBProject.VBComponents.Add(1)
            mod.CodeModule.AddFromString(vbacode2.strip())
            excel.Run(VBAname)             
        wb.Save()
        wb.Close(0)
        excel.Quit()
        print(VBAname+" VBA ran successfully!")
        del wb
        del excel


