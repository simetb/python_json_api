# JSON API with Python and FastAPI

This project is a JSON API developed in Python using FastAPI. It provides a basic structure for building a RESTful API and can be used as a starting point for larger projects.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/your_project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_project
    ```

3. Install the necessary dependencies using `pip` and the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the local server, use the following command:

```bash
uvicorn main:app --reload
```

This will start the local server and automatically reload it whenever changes are made to the code.

##API Documentation

### Get all information

- **Route**: `/champions`
- **Description**: Get all information about the champions.
- **HTTP Method**: GET
- **Successful Response**: Returns a JSON with all champions data.

### Get all champion names

- **Route**: `/champions/names`
- **Description**: Get names of all champions.
- **HTTP Method**: GET
- **Successful Response**: Returns a JSON with names of all champions.

### Get information about a specific champion

- **Route**: `/champions/{champion_name}`
- **Description**: Get specific information about a champion.
- **HTTP Method**: GET
- **Path Parameter**: `champion_name` - The name of the champion.
- **Successful Response**: Returns a JSON with the information of the specified champion.

### Get champion abilities

- **Route**: `/champions/{champion_name}/abilities`
- **Description**: Get the abilities of a champion.
- **HTTP Method**: GET
- **Path Parameter**: `champion_name` - The name of the champion.
- **Successful Response**: Returns a JSON with the abilities of the specified champion.

### Get a specific champion ability

- **Route**: `/champions/{champion_name}/abilities/{ability_label}`
- **Description**: Get a specific ability of a champion.
- **HTTP Method**: GET
- **Path Parameters**:
  - `champion_name` - The name of the champion.
  - `ability_label` - The label of the ability.
- **Successful Response**: Returns a JSON with the specific ability of the champion.

### Get the champion passive

- **Route**: `/champions/{champion_name}/passive`
- **Description**: Get the passive ability of a champion.
- **HTTP Method**: GET
- **Path Parameter**: `champion_name` - The name of the champion.
- **Successful Response**: Returns a JSON with the passive ability of the specified champion.

### Get the champion lane

- **Route**: `/champions/{champion_name}/lane`
- **Description**: Get the lane of a champion.
- **HTTP Method**: GET
- **Path Parameter**: `champion_name` - The name of the champion.
- **Successful Response**: Returns a JSON with the lane of the specified champion.

### Get the champion location

- **Route**: `/champions/{champion_name}/ubication`
- **Description**: Get the location of a champion.
- **HTTP Method**: GET
- **Path Parameter**: `champion_name` - The name of the champion.
- **Successful Response**: Returns a JSON with the location of the specified champion.
