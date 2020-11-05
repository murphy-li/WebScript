from wrapper.CampatibleDriver import get_campat_driver
from uf.login import login_199
from wrapper.Operation import Operation

if __name__ == "__main__":
    # http://npm.taobao.org/mirrors/chromedriver/
    driver = get_campat_driver()
    operation = Operation(driver)
    login_199(operation)

