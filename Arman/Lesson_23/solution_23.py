from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Radio Button Example XPath
radio_button_xpath = driver.find_element(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label[@class='benz']")
# Anna - didn't find this locator, @for='benz' not class


# Checkbox Example XPath
checkbox_xpath = driver.find_element(By.XPATH, "//div[@id='checkbox-example-div']/fieldset/label[@class='honda]")

# Anna - the same for checkbox, didn't find with this locator

# Switch Tab Example XPath
switch_tab_xpath = driver.find_element(By.XPATH, "//div[@id='open-tab-example-div']/fieldset/a[@id='opentab']")

# Anna -more optimal //a[@id='opentab']

# Multiple Select Example XPath
# Orange select value XPath
multiple_select_orange_xpath = driver.find_element(By.XPATH,
                                                   "//div[@id='multi-select-example-div']/fieldset/select"
                                                   "/option["
                                                   "@value='orange']")

# Peach select value XPath
multiple_select_peach_xpath = driver.find_element(By.XPATH,
                                                  "//div[@id='multi-select-example-div']/fieldset/select/option["
                                                  "@value='peach']")

# Element Displayed Example XPath
# Show button XPath
show_button_xpath = driver.find_element(By.XPATH,
                                        "//div[@id='hide-show-example-div']/fieldset/input[@id='show-textbox']")

# Anna - more optmial xpath - //input[@id='show-textbox']

# Hide/Show Example XPath
hide_show_example_xpath = driver.find_element(By.XPATH,
                                              "//div[@id='hide-show-example-div']/fieldset/input[@id='displayed-text']")

# Switch to Alert Example XPath
enter_your_name_xpath = driver.find_element(By.XPATH,
                                            "//div[@id='alert-example-div']/fieldset/input[@id='name']")

# Mouse Hover Example XPath
mouse_hover_button_xpath = driver.find_element(By.XPATH,
                                               "//div[@class='mouse-hover']/button[@id='mousehover']")

# Web Table Example XPath
web_table_example_xpath = driver.find_element(By.XPATH,
                                              "//*[@id='product']/tbody/tr[3]/td[@class='course-name']")

# Anna - xpaths are correct(except first 2 xpaths), but not optimal, try to use minimum attributes in xpaths like this //a[@id='opentab']
# Anna - And also you didn't get number of elements you get
