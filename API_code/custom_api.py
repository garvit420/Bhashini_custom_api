from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class TranslationRequest(BaseModel):
    source_language: int
    content: str
    target_language: int

languages = {
    1: "hi",
    2: "gom",
    3: "kn",
    4: "doi",
    5: "brx",
    6: "ur",
    7: "ta",
    8: "ks",
    9: "as",
    10: "bn",
    11: "mr",
    12: "sd",
    13: "mai",
    14: "pa",
    15: "ml",
    16: "mni",
    17: "te",
    18: "sa",
    19: "ne",
    20: "sat",
    21: "gu",
    22: "or"
}



@app.get('/')
async def root():
    return {
        1: "Hindi",
        2: "Gom",
        3: "Kannada",
        4: "Dogri",
        5: "Bodo",
        6: "Urdu",
        7: "Tamil",
        8: "Kashmiri",
        9: "Assamese",
        10: "Bengali",
        11: "Marathi",
        12: "Sindhi",
        13: "Maithili",
        14: "Punjabi",
        15: "Malayalam",
        16: "Manipuri",
        17: "Telugu",
        18: "Sanskrit",
        19: "Nepali",
        20: "Santali",
        21: "Gujarati",
        22: "Odia"
    }



@app.post('/scaler/translate', response_model=dict)
async def translate(request: TranslationRequest):
    source_language = languages[request.source_language]
    content = request.content
    target_language = languages[request.target_language] 

    payload = {
        "pipelineTasks": [
            {
                "taskType": "translation",
                "config": {
                    "language": {
                        "sourceLanguage": source_language,
                        "targetLanguage": target_language
                    }
                }
            }
        ],
        "pipelineRequestConfig": {
            "pipelineId" : "64392f96daac500b55c543cd"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "userID": "e832f2d25d21443e8bb90515f1079041",
        "ulcaApiKey": "39e27ce432-f79c-46f8-9c8c-c0856007cb4b"
    }

    response = requests.post('https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline', json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        service_id = response_data["pipelineResponseConfig"][0]["config"][0]["serviceId"]

        compute_payload = {
            "pipelineTasks": [
                {
                    "taskType": "translation",
                    "config": {
                        "language": {
                            "sourceLanguage": source_language,
                            "targetLanguage": target_language
                        },
                        "serviceId": service_id
                    }
                }
            ],
            "inputData": {
                "input": [
                    {
                        "source": content
                    }
                ],
                "audio": [
                    {
                        "audioContent": None
                    }
                ]
            }
        }

        callback_url = response_data["pipelineInferenceAPIEndPoint"]["callbackUrl"]
        
        headers2 = {
            "Content-Type": "application/json",
            response_data["pipelineInferenceAPIEndPoint"]["inferenceApiKey"]["name"]:
                response_data["pipelineInferenceAPIEndPoint"]["inferenceApiKey"]["value"]
        }

        compute_response = requests.post(callback_url, json=compute_payload, headers=headers2)

        if compute_response.status_code == 200:
            compute_response_data = compute_response.json()
            translated_content = compute_response_data["pipelineResponse"][0]["output"][0]["target"]
            return {
                "status_code": 200,
                "message": "Translation successful",
                "translated_content": translated_content
            }
        else:
            return {
                "status_code": compute_response.status_code,
                "message": "Error in translation",
                "translated_content": None
            }
    else:
        return {
            "status_code": response.status_code,
            "message": "Error in translation request",
            "translated_content": None
        }
