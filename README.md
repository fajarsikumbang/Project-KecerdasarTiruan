
# Rice Nutrient Deficiency Consultation

This project is a Flask web application that helps users identify nutrient deficiencies in rice plants based on symptoms and growth phases.

## Project Structure

- `app.py`: Main Flask application file
- `kekurangan_nutrisi_padi_bersih.csv`: CSV file containing data on nutrient deficiencies in rice
- `templates/`: Directory containing HTML templates for the web interface

## Features

- Web interface for users to input symptoms and growth phases
- Search functionality to find matching nutrient deficiencies
- Partial matching for more flexible search results

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install flask pandas
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`
3. Enter symptoms and growth phase in the search form
4. View the results of nutrient deficiencies based on your input

## Data

The application uses a CSV file (`kekurangan_nutrisi_padi_bersih.csv`) containing information about nutrient deficiencies in rice plants. This data includes:

- Symptoms of nutrient deficiencies
- Growth phases of rice plants
- Corresponding nutrient deficiencies

## Contributing

Contributions to improve the application or expand the dataset are welcome. Please submit a pull request or open an issue to discuss proposed changes.
