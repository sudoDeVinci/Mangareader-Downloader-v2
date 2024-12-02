from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from time import sleep

def WaitTilAvaliable(driver: Chrome,
                     by:By, 
                     value:str, 
                     expected_error:Exception=(InvalidSelectorException, NoSuchElementException,),
                     max_attempts:int=20, 
                     wait_time:float=0.5) -> WebElement:
    """
    Wait until the element we want is avaliable in the page.

    Args:
        driver (Chrome): The driver of the browser.
        by (By): The method of search.
        value (str): The value to search.
        expected_error (Exception, optional): The expected error to catch. Defaults to (InvalidSelectorException, NoSuchElementException,).
        max_attempts (int, optional): The maximum number of attempts. Defaults to 20.
        wait_time (float, optional): The time to wait between each attempt. Defaults to 0.5.
    
    Returns:
        WebElement: The element found.
    """
    i = 0
    while True:
        try:
            element = driver.find_element(by=by, value=value)
            break
        except expected_error:
            if i >= max_attempts:
                raise expected_error

            sleep(wait_time)
            i += 1
            continue
    
    return element

def ElementExists(driver: Chrome, by:By, value:str, expected_error=(InvalidSelectorException, NoSuchElementException,)) -> bool:
    try:
        driver.find_element(by=by, value=value)
        return True
    except expected_error:
        return False

def FilterPath(path) -> str:
    illegal_chars = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
    for char in illegal_chars:
        path = path.replace(char, "")
    return path