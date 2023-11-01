# Bhashini_custom_api
Translate to/from Indian regional languages with FastAPI. Efficient, multilingual communication for India. Powered by Bhashini APIs.

# Custom Language Translation API

## Overview
This is a Custom Language Translation API built using FastAPI and powered by Bhashini APIs. It allows translations to and from Indian regional languages. Please read this README to understand how to use the API and for important details.

## Features
- Translation to and from Indian regional languages.
- Fast and efficient translation using Bhashini APIs.
- Support for multiple languages.

## Getting Started
To run this API locally, follow the steps below:

1. Clone the repository:

   ```
   git clone https://github.com/garvit420/Bhashini_custom_api.git
   ```

2. install fastapi and uvicorn:

   ```
   pip install fastapi uvicorn
   ```
   
3. Start the API using Uvicorn:

   ```
   python -m uvicorn custom_api:app --reload
   ```

The API will be available at `http://localhost:8000`. You can access the documentation at `http://localhost:8000/docs`.

## Usage
- **Endpoint**: `/scaler/translate`
- **Method**: POST

**Request Format**
```json
{
  "source_language": <Integer>,
  "content": <String>,
  "target_language": <Integer>
}
```

**Response Format**
```json
{
  "status_code": <Integer>,
  "message": <String>,
  "translated_content": <String>
}
```

## Supported Languages
You can specify languages using their respective numbers in the request.

1. Hindi
2. Gom
3. Kannada
4. Dogri
5. Bodo
6. Urdu
7. Tamil
8. Kashmiri
9. Assamese
10. Bengali
11. Marathi
12. Sindhi
13. Maithili
14. Punjabi
15. Malayalam
16. Manipuri
17. Telugu
18. Sanskrit
19. Nepali
20. Santali
21. Gujarati
22. Odia

## Example Python Script
You can use the provided `ex_check.py` script to check the working of the API and see how to make requests programmatically.

## Documentation
For detailed API documentation, access the Swagger documentation at `http://localhost:8000/docs`. It provides interactive API exploration and usage examples.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
