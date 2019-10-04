import os.path
import win32com.client


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


