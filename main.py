from fastapi import FastAPI,HTTPException, Path ,Query
import json
app=FastAPI()

@app.get('/')
def hello():
    return {'message': "Patient Managment API "}

@app.get('/a')
def about():
    return {"about":"A fully functional API to manage Patients Records"}

def load_data():
    with open('database.json','r') as f:
     var=json.load(f)
    f.close()
    return var


@app.get('/view')
def patient_data():
        return load_data()

#------------------------------------------------------video 4--------------
@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description="ID of the patient in the DB",example='P01')):
     data=load_data()
     if patient_id in data:
        return data[patient_id]
     else:
         raise HTTPException(status_code=404, detail=" Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str=Query(..., description="sorting by height, weight and bmi"),order: str=Query('asc',description="sort in asc or desc order")):
    valid_feilds=['height','weight','bmi']

    def data():
        with open('database.json','r') as f:
         var=json.load(f)
        f.close()
        return var
    
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400,detail=f"invalid field value select from these {valid_feilds}")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail=f'Invalid field and select from asc and desc')
    data = data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
