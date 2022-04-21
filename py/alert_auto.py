import psutil
from pywinauto.application import Application

# pl = psutil.pids()
# p = psutil.Process(15236)
# print(pl)
# print(p)

# app = Application().connect(path="C:\Program Files\Google\Chrome\Application\chrome.exe")
# tab = app.window(title='新标签页')
# tab.type_keys('{F6}')
# tab.type_keys('{ESC}')
# tab.type_keys('www.google.com')
# tab.type_keys('{ENTER}')

# app.Window_()
# print(app)


app = Application(backend='uia').connect(title_re=".*Chrome.*")
print(app)

# dlg = app.top_window()
# print(dlg)

# dlg = app.window(title_re=".*", control_type="Pane")

# # dlg.print_control_identifiers(depth=5)
# dlg.child_window(title="确定", control_type="Button").click()

# ctrl = dlg.child_window(title="poopcode.com 显示", control_type="Custom")
# ctrl.print_control_identifiers()
