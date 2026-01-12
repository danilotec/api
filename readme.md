# API Project

This project is a FastAPI-based application that provides endpoints for managing firmware updates. It includes authentication, version management, and logging for successful or failed updates.

## Features

- **Home Endpoint**: A simple home page endpoint.
- **Firmware Management**:
    - Get the current firmware version.
    - Download the firmware file.
    - Upload a new firmware file.
    - Update the firmware version.
    - Log successful or failed updates.
- **Authentication**: Bearer token-based authentication for secure access.

## Project Structure

```
api/
├── app.py                # Main application entry point
├── firrmware_routes.py   # Firmware-related endpoints
├── security.py           # Authentication logic
├── .env-example          # Example environment variables file
└── firmwares/            # Directory for firmware files
```

## Endpoints

### Home

- **GET /**  
    Returns a welcome message.

### Firmware

- **GET /firmware/**  
    Retrieves the current firmware version.

- **GET /firmware/download**  
    Downloads the firmware file.

- **POST /firmware/set-version**  
    Updates the firmware version.  
    **Body**: `{"version": "new_version"}`

- **POST /firmware/update**  
    Uploads a new firmware file.  
    **Form Data**: `firmware` (file)

- **POST /firmware/success**  
    Logs a successful firmware update.  
    **Body**: `{"name": "device_name", "version": "firmware_version"}`

- **POST /firmware/fail**  
    Logs a failed firmware update.  
    **Body**: `{"name": "device_name", "version": "firmware_version"}`

## Authentication

The API uses a bearer token for authentication. Include the token in the `Authorization` header of your requests:

```
Authorization: Bearer <your_token>
```

The token is defined in the `.env` file.

## Environment Variables

Create a `.env` file in the root directory and define the following variable:

```
api_token=<your_api_token>
```

You can use the `.env-example` file as a reference.

## Setup

1. Clone the repository.
2. Install dependencies:
     ```bash
     pip install fastapi uvicorn python-dotenv
     ```
3. Create a `.env` file and set your API token.
4. Run the application:
     ```bash
     uvicorn app:app --reload
     ```

## Logs

- **success.log**: Logs successful firmware updates.
- **fail.log**: Logs failed firmware updates.

## License

This project is licensed under the MIT License.