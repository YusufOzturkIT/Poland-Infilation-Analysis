import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("STARTING - Automated Multi-Page Scanner...")
print("Scanning pages 0 to 10...")
print("-" * 50)

found_any = False

for page in range(10):
    api_url = f"https://api-dbw.stat.gov.pl/api/1.1.0/variable/variable-section-periods?ile-na-stronie=100&numer-strony={page}&lang=en"
    
    print(f"Scanning Page {page}...")
    
    try:
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            full_package = response.json()
            actual_variables = full_package.get('data', [])
            
            for item in actual_variables:
                variable_name = item.get('nazwa-zmienna', '')
                
                if "price" in variable_name.lower() or "inflation" in variable_name.lower():
                    print(f"\nMATCH FOUND ON PAGE {page}!")
                    print(f"Variable ID (id-zmienna): {item.get('id-zmienna')}")
                    print(f"Variable Name: {variable_name}")
                    print(f"Data Schema (id-przekroj): {item.get('id-przekroj')}")
                    print("-" * 40)
                    found_any = True
        else:
            print(f"Warning: Could not read page {page}. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"Error on page {page}: {str(e)}")
    
    time.sleep(0.2)

print("\n--- SCAN COMPLETE ---")
if not found_any:
    print("Still nothing? We might need to scan even deeper or try another door!")
    
    time.sleep(0.2)

print("\n--- SCAN COMPLETE ---")
if not found_any:
    print("Still nothing? We might need to scan even deeper or try another door!")