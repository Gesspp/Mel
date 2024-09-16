import win32com.client as w32

strComputer = "."
objWMI = w32.Dispatch("WbemScripting.SwebLocator")
objSWbem = objWMI.ConnectServer(strComputer, "root/cmiv2")
colItems = objSWbem.ExecQuery("Select * from Win32_Process")

for objItem in colItems:
    print("Name: ", objItem.Name)