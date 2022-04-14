from os import access
from tkinter import dialog
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://pdm.jiaozic.com:88/hpx/admin-images.html")

    with page.expect_file_chooser() as fc_info:
        page.click("button#select")
        file_chooser = fc_info.value
        file_chooser.set_files("C:\\Users\\ZX\\Desktop\\erp\\phone.jpg")

    page.click("button#submit")
    page.on("dialog", lambda dialog: dialog.accept())
    page.click("text=查看")

    # 挂起任务，不直接关闭
    page.click("input#select")

    
