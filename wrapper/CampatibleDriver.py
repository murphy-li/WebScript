from selenium import webdriver


def get_campat_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(r"C:\Users\lihm31909\AppData\Local\Google\Chrome\Machine Data")
    # options.add_argument("cookies-without-same-site-must-be-secure=Disabled")
    # options.add_argument("same-site-by-default-cookies=Disabled")
    # options.add_experimental_option("cookies-without-same-site-must-be-secure", "Disabled")
    experimentalFlags = ['same-site-by-default-cookies@2', 'cookies-without-same-site-must-be-secure@2']
    chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
    options.add_experimental_option('localState', chromeLocalStatePrefs)
    return webdriver.Chrome(options=options)