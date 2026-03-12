import os

def fix():
    path = r'd:\agri\backend\app.py'
    with open(path, 'rb') as f:
        data = f.read()
    
    # Use bytes for finding to avoid encoding issues
    start_marker = b"WEATHER RISK ALERTS"
    end_marker = b"@app.post(\"/register\")"
    
    start_pos = data.find(start_marker)
    end_pos = data.find(end_marker)
    
    if start_pos != -1 and end_pos != -1:
        # Rebuild the file
        header = data[:start_pos + 100] # roughly after the header block
        # Find the next clean line
        clean_start = data.find(b"\n", start_pos + 80) + 1
        
        new_code = r"""
@app.post("/weather_alerts")
def get_weather_alerts(q: WeatherQuery):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model_g = genai.GenerativeModel('gemini-1.5-flash')

        crops_str = ", ".join(q.crops) if q.crops else "general crops"
        prompt = f'''You are an expert Indian agricultural disease risk predictor.

Current weather in {q.city}: Temperature {q.temp} C, Humidity {q.humidity}%, Conditions: {q.condition}.
Crops being grown: {crops_str}.

Based on this weather, identify the TOP 3 disease/pest risks RIGHT NOW.
For each risk, provide:
- title: short alert name (e.g. "Fungal Blight Alert")
- level: "high", "medium", or "low"
- message: 1 sentence explaining the risk and 1 preventive action
- crop: which crop is most affected
- icon: a single emoji

Return ONLY raw JSON array (no markdown):
[{{"title":"...","level":"high/medium/low","message":"...","crop":"...","icon":"..."}}]'''

        response = model_g.generate_content(prompt)
        text = response.text.replace('```json','').replace('```','').strip()
        alerts = json.loads(text)
        return {"alerts": alerts, "city": q.city, "temp": q.temp, "humidity": q.humidity}

    except Exception as e:
        return {
            "alerts": [
                {"title": "Fungal Disease Risk", "level": "high", "message": f"Humidity {q.humidity}% is high. Spray Mancozeb.", "crop": "All", "icon": "!"},
                {"title": "Pest Activity Alert", "level": "medium", "message": f"Temperature {q.temp}C favors pests. Use Neem oil.", "crop": "All", "icon": "!"},
                {"title": "Irrigation Advisory", "level": "low", "message": "Check soil moisture.", "crop": "All", "icon": "!"}
            ],
            "city": q.city, "temp": q.temp, "humidity": q.humidity
        }

""".encode('utf-8')
        
        final_data = data[:clean_start] + new_code + data[end_pos:]
        with open(path, 'wb') as f:
            f.write(final_data)
        print("Done.")
    else:
        print(f"Not found: {start_pos}, {end_pos}")

if __name__ == '__main__':
    fix()
