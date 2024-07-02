# SmartCrop Advisor

The SmartCrop Advisor is a project that provides crop recommendations and suggests suitable pesticides based on user input of land area and location. It uses a Random Forest Classifier algorithm to predict the top 3 crops that are most suitable for a given area and location. Additionally, it recommends pesticides suitable for the predicted crops to help farmers make informed decisions about crop selection and pest management. The project includes a React-based frontend and a Node.js/Express backend.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Input Data](#input-data)
- [Output](#output)
- [Contributing](#contributing)

## Introduction
Agriculture heavily depends on making informed decisions about crop selection and pest management. The SmartCrop Advisor aims to assist farmers and agricultural experts in identifying the most suitable crops for a specific location and area and provides relevant pesticide recommendations. The project uses machine learning techniques to predict crop suitability and recommends pesticides based on historical data.

## Requirements
### Backend
- Node.js
- Express
- Python 3.x
- pandas
- matplotlib
- scikit-learn

### Frontend
- React
- Axios

## Installation
### Backend
1. Clone the repository to your local machine.
2. Navigate to the `backend` directory:
    ```sh
    cd backend
    ```
3. Install the required Node.js packages using npm:
    ```sh
    npm install
    ```
4. Install the required Python packages using pip:
    ```sh
    pip install pandas matplotlib scikit-learn
    ```

### Frontend
1. Navigate to the `frontend` directory:
    ```sh
    cd frontend
    ```
2. Install the required React packages using npm:
    ```sh
    npm install
    ```

## Usage
### Backend
1. Prepare the input data files:
- `crop_data.csv`: Contains crop-related information such as year, state, district, and crop name.
- `pesticides.csv`: Contains pesticide data, including the corresponding crops for which they are suitable.

2. Ensure your Python script (`script.py`) is configured to save images to the `images` directory.
3. Run the Node.js server:
    ```sh
    node server.js
    ```

### Frontend
1. Start the React app:
    ```sh
    npm start
    ```

2. Open your browser and navigate to `http://localhost:3000`.
3. Click the "Run Script" button to run the Python script on the backend, which will save the image, and then display the image on the frontend.

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
