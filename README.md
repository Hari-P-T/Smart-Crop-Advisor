# SmartCrop Advisor

The SmartCrop Advisor is a Python-based project that provides crop recommendations and suggests suitable pesticides based on user input of land area and location. It uses a Random Forest Classifier algorithm to predict the top 3 crops that are most suitable for a given area and location. Additionally, it recommends pesticides suitable for the predicted crops to help farmers make informed decisions about crop selection and pest management.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Input Data](#input-data)
- [Output](#output)
- [Contributing](#contributing)

## Introduction
Agriculture heavily depends on making informed decisions about crop selection and pest management. The SmartCrop Advisor aims to assist farmers and agricultural experts in identifying the most suitable crops for a specific location and area and provides relevant pesticide recommendations. The project uses machine learning techniques to predict crop suitability and recommends pesticides based on historical data .

## Requirements
- Python 3.x
- pandas
- matplotlib
- scikit-learn

## Installation
1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
```python
pip install pandas matplotlib scikit-learn
 ```

## Usage
1. Prepare the input data files:
- `crop_data.csv`: Contains crop-related information such as year, state, district, and crop name.
- `pesticides.csv`: Contains pesticide data, including the corresponding crops for which they are suitable.

2. Run the script `crop_prediction.py`:
```python
python crop_prediction.py
 ```


3. Follow the on-screen prompts to enter the area of land (in hectares) and location information (year, state, district).

4. The script will output the top 3 predicted crops suitable for the given area and location, along with a list of suitable pesticides for these crops.

## Input Data
- `crop_data.csv`: The CSV file should contain the following columns:
- `year`: The year of crop data.
- `state`: The state where the crop is grown.
- `district`: The district where the crop is grown.
- `crop_name`: The name of the crop.

- `pesticides.csv`: The CSV file should contain the following columns:
- `Crop`: The crop for which the pesticide is suitable.
- `Pesticide`: The name of the pesticide.

Ensure that the data in these files is correctly formatted and contains relevant information for accurate predictions.

## Output
The SmartCrop Advisor will display the top 3 predicted crops suitable for the given area and location. Additionally, it will provide a list of suitable pesticides for these crops.

## Contributing
Contributions to the SmartCrop Advisor project are welcome! If you encounter any issues or have suggestions for improvements, feel free to create a pull request or open an issue in the GitHub repository.
