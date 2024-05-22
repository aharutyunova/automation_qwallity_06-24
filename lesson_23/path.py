radio_button = ('//*[@id="radio-btn-example"]/fieldset/label[2]')
checkbox = ('//*[@id="checkbox-example-div"]/fieldset/label[3]')
tab = ('//*[@id="opentab"]')
mul_select_or = ('//*[@id="multiple-select-example"]/option[2]')
mul_select_peach = ('//*[@id="multiple-select-example"]/option[3]')
disp_el = ('//*[@id="show-textbox"]')
hide = ('//*[@id="displayed-text"]')
swich_alert = ('//*[@id="name"]')
mouse_hover = ('//*[@id="mouse-hover-example-div"]/div[1]/fieldset/legend')
pplanguage = ('//*[@id="product"]/tbody/tr[3]/td[2]')

print(len([radio_button, checkbox, tab, mul_select_or, mul_select_peach, disp_el, hide, swich_alert, mouse_hover, pplanguage]))

# Anna - in xpaths try avoid use indexes,in case you neet select specific value better to write something like //*[@id="radio-btn-example"]//label[@for='benz']
# for count elements will be better to open browser and check found elements, or even use loop not hardcode all variables in the list, like in line 12