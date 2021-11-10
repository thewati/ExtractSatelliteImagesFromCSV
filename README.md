# ExtractSatelliteImagesFromCSV
This repo shows you how to extract satellite images using a CSV file that contains coordinates (latitude and longitude). The extracted images can be used for different machine learning tasks such as path loss prediction (Of course the coordinates would have to be around the same area).

Note: This was run in PyCharm on a Windows environment. It works perfectly on Ubuntu too.

# Instructions
1. Create a mapbox account here: www.mapbox.com. 
2. Once logged in, scroll down to Default Public Token. Copy it! You will need it in the ExtractSatelliteImages.py file
3. Make sure you have downloaded and installed GeckoDriver in your computer. You can get it here: https://github.com/mozilla/geckodriver/releases
4. Store the GeckoDriver.exe file in your root folder
5. Run the ExtractSatelliteImages.py file. More explanations are in the comments

# Results
Using the data in the coordinates.csv file, some of the extracted images will look as below:
## Malawi Parliament Building
![Malawi Parliament](https://user-images.githubusercontent.com/39279950/141091623-abdd2f47-c612-4554-859d-6e6f451dedd6.png)

## Amaryllis Hotel
![Amaryllis Hotel](https://user-images.githubusercontent.com/39279950/141092404-85aedb3c-2c5e-4214-a348-43369e7bb447.png)

## Bingu National Stadium
![Bingu National Stadium](https://user-images.githubusercontent.com/39279950/141092575-12b0614d-4f4a-4bc5-a9be-f6327d087373.png)

Go on and give it a try! :relaxed:
