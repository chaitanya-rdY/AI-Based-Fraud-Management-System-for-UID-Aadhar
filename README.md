# AI-Based Fraud Management for UID Aadhar

## Project Overview

This project aims to develop an AI-based system for detecting and managing fraud in UID Aadhar cards. The system leverages machine learning models for image classification and object detection, along with Optical Character Recognition (OCR) to extract and verify key information from Aadhar cards. The project is implemented using Python and various libraries such as YOLO, OpenCV, EasyOCR, and Pandas.

## Features

### Image Classification
- Utilizes YOLO models to classify images as Aadhar cards or non-Aadhar cards.
- Ensures high accuracy in identifying valid Aadhar cards.

### Object Detection
- Detects key fields on Aadhar cards, including Name, UID, and Address.
- Uses YOLO models trained on custom datasets for precise detection.

### Optical Character Recognition (OCR)
- Integrates EasyOCR to extract text from detected regions on Aadhar cards.
- Handles multiple lines of text and combines them into structured data.

### Data Processing and Integration
- Processes and integrates extracted data using Pandas.
- Combines new data with existing datasets, ensuring data consistency and handling missing files.

### Automation and Scripting
- Automates data extraction and processing workflows.
- Creates scripts to automate the extraction of text from images and integration of extracted data into Excel files.

### Data Analysis and Reporting
- Analyzes and reports on extracted data.
- Generates reports and exports results to Excel for further analysis.

### Version Control and Documentation
- Manages code versions using Git.
- Provides clear and concise documentation for functions and workflows.

## Project Structure
- `main.py`: Main script to process images, extract data, and update the database.
- `integ.py`: Integration script for image classification, object detection, and OCR.
- `matching/Name_match.py`: Functions for matching names with various normalization techniques.
- `matching/UID_match.py`: Function for matching UIDs.
- `detection/`: Directory containing YOLO model configurations and training scripts.
- `recognition/`: Directory containing OCR-related scripts and notebooks.
- `aadhar_classification_yolo/`: Directory containing YOLO classification model configurations and training scripts.

## Installation

Clone the repository:
```bash
git clone <(https://github.com/chaitanya-rdY/AI-Based-Fraud-Management-System-for-UID-Aadhar)>
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Download and place the YOLO model weights in the appropriate directories.

## Usage

1. **Process an Image**:
    ```bash
    python main.py --input path_to_image
    ```

2. **Train YOLO Models**:
    - Update the configuration files in the `detection` and `aadhar_classification_yolo` directories.
    - Run the training scripts to train the models on custom datasets.

3. **Extract and Verify Data**:
    - Use the `process_image` function in `integ.py` to classify images, detect objects, and extract text.
    - Verify the extracted data against existing records in the database.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Acknowledgements

- YOLO for the object detection and classification models.
- EasyOCR for the OCR capabilities.
- OpenCV for image processing.
- Pandas for data manipulation and analysis.
