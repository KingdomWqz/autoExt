from pywinauto.application import Application
from pywinauto.findwindows import find_windows
import pywinauto.mouse as mouse

app = Application(backend='uia').connect(title_re=".*Chrome.*")
win = app.window(title_re=".*Chrome.*", control_type="Pane")
# dlg = dlg['TitleBar']
# dlg = dlg['ToolBar'] 
# dlg = tab['Pane2']

menu = win.child_window(title="扩展程序", control_type="MenuItem")
menu_rect = menu.rectangle()
mouse.click(button="left", coords=(menu_rect.left, menu_rect.top))

# dlg.click()
# tab.print_control_identifiers(depth=2)
# print(tab.print_control_identifiers(depth=8))

# extPane = app.window(title="", control_type="Pane")
# print(extPane)

ext = win.child_window(title="FeHelper(前端助手)", control_type="Button")
ext_rect = ext.rectangle()
mouse.click(button="left", coords=(ext_rect.left, ext_rect.top))


popup = win.child_window(title_re=".*FeHelper.*", control_type="Document")
popup_rect = popup.rectangle()
mouse.click(button="right", coords=(popup_rect.left, popup_rect.top))

inpector = win.child_window(title_re=".*检查.*", control_type="MenuItem")
inpector_rect = inpector.rectangle()
mouse.click(button="left", coords=(inpector_rect.left, inpector_rect.top))


# inpector = app.window(title="", control_type="Pane")
# tab.print_control_identifiers(depth=4)

# print(find_windows(title_re=".*", control_type="Pane"))