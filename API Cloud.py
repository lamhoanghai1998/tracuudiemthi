from fastapi import FastAPI, Query
import json

app = FastAPI()

# Load dữ liệu JSON vào bộ nhớ
with open('all_data_merged.json', encoding='utf-8') as f:
    data = json.load(f)

@app.get("/tra-cuu")
def tra_cuu_diem(SBD: str = Query(..., description="Số báo danh")):
    result = next((record for record in data if record['SOBAODANH'] == SBD), None)
    if result:
        return {"success": True, "data": result}
    else:
        return {"success": False, "message": "Không tìm thấy thí sinh."}
