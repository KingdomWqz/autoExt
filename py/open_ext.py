from pywinauto.application import Application
import pywinauto.mouse as mouse

app = Application(backend='uia').connect(title_re=".*Chrome.*")
tab = app.window(title_re=".*", control_type="Pane")
# dlg = dlg['TitleBar']
# dlg = dlg['ToolBar']
# dlg = tab['Pane2']
menu = tab.child_window(title="扩展程序", control_type="MenuItem")
menu_rect = menu.rectangle()
# dlg.click()
# dlg.print_control_identifiers(depth=2)

mouse.click(button="left", coords=(menu_rect.left + 10, menu_rect.top + 5))

# time.sleep(5)

# print(tab.print_control_identifiers(depth=8))

test = tab.child_window(title="FeHelper(前端助手)")
test_rect = test.rectangle()
mouse.click(button="left", coords=(test_rect.left, test_rect.top))