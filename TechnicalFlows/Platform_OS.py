import platform


def getplatform_OS():


    Platform=platform.platform()

    if "macos" in  Platform.lower():
        print("The code is running on a MAC!!")
        return "mac"
    elif "windows" in Platform.lower():
        print("The Code is running on windows!!")
        return "windows"