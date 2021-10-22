# Appium automation project.

## Prerequisites

- Install Python3 in your environment, using PyCharm would be my first recommendation,  but using other IDEs such as Visual Studio Code shouold also work
- Install Android Studio and start an Android Emulated device using the AVD, alternatively you can use a physical device as long as you're able to provide its details to Appium, see the "Executing the tests section"
- Checkout the following branch, you will need the path for the app-debug.apk

## Executing the tests

- Inside the Base.py file, locate and modify the following variables:
    - app, set the absolute path to the app-debug.apk
    - platform_version, set the Android version running in your device
    - device_name, "The name of the device as shown by the AVD Manager"
- The virtual environment is provided in the repository, to start the virtual environment run the following command in console: `source venv/bin/activate`
    
