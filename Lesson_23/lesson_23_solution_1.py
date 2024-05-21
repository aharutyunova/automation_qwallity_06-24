'''
1. //*[@id='benzradio'] or if no id //*[@id='radio-btn-example']//input[@value='benz' and @type='radio']
2. //*[@id='hondacheck'] or if no id //*[@id='checkbox-example-div']//descendant::input[3]
3. //*[@id='opentab'] or if no id //a[@class='btn-style class1 class2']
4. //option[@value='orange' or @value='peach'] or if no id //*[@id='multiple-select-example']//option[contains(text(), 'Orange') or contains(text(), 'Peach')]
5. //*[@id='show-textbox']
6. //*[@id='displayed-text']
7. //*[@id='name']
8. //*[@id='mouse-hover-example-div']/div/fieldset/legend
9. //td[contains(text(), 'Python Programming Language')]
'''

xPath_dict = {
    "rbtn_benz": "[@id='benzradio']",
    "chkbx": "//*[@id='hondacheck']",
    "sw_tab_open": "//*[@id='opentab']",
    "m_select": "//option[@value='orange' or @value='peach']",
    "el_displ_show": "//*[@id='show-textbox']",
    "hide_show": "//*[@id='displayed-text']",
    "name": "//*[@id='name']",
    "mouse_hov": "//*[@id='mouse-hover-example-div']/div/fieldset/legend",
    "web_table": "//td[contains(text(), 'Python Programming Language')]"
}

count = 0
for items in xPath_dict:
    count += 1
print(count)
