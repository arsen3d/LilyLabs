import base64
from fastapi import FastAPI

from lpesmfold_light.job_state_manager import job_state_manager

app = FastAPI()

from lpesmfold_light.api_models import RunEsmFoldPredictionRequest, RunEsmFoldPredictionResponse, IsJobRunningResponse
from lpesmfold_light.loggers import Log
from lpesmfold_light.services import run_facebook_api_folding
import json
import requests
@app.post("/run-folding")
def predict_through_api(request: RunEsmFoldPredictionRequest) -> RunEsmFoldPredictionResponse:
    print(request)
    serialized_request = json.dumps(request.to_dict())

    print("Request received for folding", serialized_request)
    print("starting job lpesmfold_light")
    Log.folding_through_api_request(request)
    if request.job_id:
        job_state_manager.start_job(request.job_id)
    
        # result = run_facebook_api_folding(request)
    payload = {
        "module": "github.com/arsen3d/lp_esmfold_light_module:main",
        "input": {
            "name": "JSON",
            "value": base64.b64encode(json.dumps({
                "protein_sequence": "SNPYQRGPNPTRSALTADGPFSVATYTVSRLSVSGFGGGVIYYPTGTSLTFGGIAMSPGYTADASSLAWLGRRLASHGFVVLVINTNSRFDYPDSRASQLSAALNYLRTSSPSAVRARLDANRLAVAGHSMGGGGTLRIAEQNPSLKAAVPLTPWHTDKTFNTSVPVLIVGAEADTVAPVSQHAIPFYQNLPSTTPKVYVELDNASHFAPNSNNAAISVYTISWMKLWVDNDTRYRQFLCNVNDPALSDFRTNNRHCQ",
                "job_id": ""
            }, ensure_ascii=False).encode('utf-8')).decode('utf-8')
        }
    }
    print("payload",json.dumps(payload))
    response = requests.post("https://api.devnet.arsenum.com/run/job", data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    print("dataid",response.json()["dataid"])
    response = requests.get("https://api.devnet.arsenum.com/files/"+ response.json()["dataid"] +"/stdout")
    
    print(response.text)
    result = RunEsmFoldPredictionResponse(pdb_content=response.text)
    
    print("Response for folding", request.job_id)
    if request.job_id:
        job_state_manager.finish_job(request.job_id)
    Log.folding_through_api_response(result)
    return result

@app.get("/job/{job_id}/is-running")
def is_job_running(job_id: str) -> IsJobRunningResponse:
    return IsJobRunningResponse(is_running=job_state_manager.is_job_running(job_id))

@app.get("/jobs/running")
def get_running_jobs():
    return {"running_jobs": job_state_manager.get_running_jobs()}