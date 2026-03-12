import os

def fix_app():
    path = r'd:\agri\backend\app.py'
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    start_idx = -1
    end_idx = -1
    
    for i, line in enumerate(lines):
        if 'WEATHER RISK ALERTS' in line:
            start_idx = i + 1
        if '@app.post("/register")' in line:
            end_idx = i
            break
            
    if start_idx != -1 and end_idx != -1:
        new_func = [
            '@app.post("/weather_alerts")\n',
            'def get_weather_alerts(q: WeatherQuery):\n',
            '    try:\n',
            '        genai.configure(api_key=GEMINI_API_KEY)\n',
            '        model_g = genai.GenerativeModel("gemini-1.5-flash")\n',
            '\n',
            '        crops_str = ", ".join(q.crops) if q.crops else "general crops"\n',
            '        prompt = f"""You are an expert Indian agricultural disease risk predictor.\n',
            '\n',
            'Current weather in {q.city}: Temperature {q.temp} C, Humidity {q.humidity}%, Conditions: {q.condition}.\n',
            'Crops being grown: {crops_str}.\n',
            '\n',
            'Based on this weather, identify the TOP 3 disease/pest risks RIGHT NOW.\n',
            'For each risk, provide:\n',
            '- title: short alert name (e.g. \\"Fungal Blight Alert\\")\n',
            '- level: \\"high\\", \\"medium\\", or \\"low\\"\n',
            '- message: 1 sentence explaining the risk and 1 preventive action\n',
            '- crop: which crop is most affected\n',
            '- icon: a single emoji\n',
            '\n',
            'Return ONLY raw JSON array (no markdown):\n',
            \'[{"title":"...","level":"high/medium/low","message":"...","crop":"...","icon":"..."}]"""\n',
            '\n',
            '        response = model_g.generate_content(prompt)\n',
            '        text = response.text.replace("```json", "").replace("```", "").strip()\n',
            '        alerts = json.loads(text)\n',
            '        return {"alerts": alerts, "city": q.city, "temp": q.temp, "humidity": q.humidity}\n',
            '\n',
            '    except Exception as e:\n',
            '        print(f"Weather AI error: {e}")\n',
            '        return {\n',
            '            "alerts": [\n',
            '                {"title": "Fungal Disease Risk", "level": "high", "message": f"Humidity {q.humidity}% is high. Spray Mancozeb 75% WP.", "crop": "Tomato, Rice", "icon": "O"},\n',
            '                {"title": "Pest Activity Alert", "level": "medium", "message": f"Temperature {q.temp} C favors pests. Use Neem oil.", "crop": "Chilli, Brinjal", "icon": "X"},\n',
            '                {"title": "Irrigation Advisory", "level": "low", "message": "Check soil moisture. Water stress reduces yield.", "crop": "All Crops", "icon": "W"}\n',
            '            ],\n',
            '            "city": q.city, "temp": q.temp, "humidity": q.humidity\n',
            '        }\n',
            '\n',
            '\n'
        ]
        
        final_lines = lines[:start_idx+1] + new_func + lines[end_idx:]
        
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(final_lines)
        print("Fixed.")
    else:
        print("Failed.")

if __name__ == '__main__':
    fix_app()
