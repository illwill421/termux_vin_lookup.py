#vin_lookup.py

import requests

def check_stolen_status(vin, api_key):
    """
    Optional helper function to query a commercial API for stolen records.
    Requires a valid API key from a commercial provider.
    """
    if not api_key:
        return "N/A (API Key Required)"
        
    url = f"https://api.vehicledatabases.com/stolen-check/{vin}"
    headers = {"x-api-key": api_key}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return "YES (REPORTED STOLEN)" if data.get("is_stolen") else "CLEAN / NO RECORD"
        return "API Error / Check Failed"
    except Exception:
        return "Network Error"

def lookup_vin(vin, api_key=""):
    # Public NHTSA vPIC Endpoint (Free - No Key Required)
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json"
    headers = {"User-Agent": "Termux-VIN-Lookup/1.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("Results"):
            vehicle = data["Results"][0]
            
            # Check stolen status if key provided
            stolen_info = check_stolen_status(vin, api_key)
            
            print("\n" + "=" * 40)
            print("         VEHICLE SPECIFICATIONS")
            print("=" * 40)
            print(f"  VIN:           {vin.upper()}")
            print(f"  Year:          {vehicle.get('ModelYear') or 'N/A'}")
            print(f"  Make:          {vehicle.get('Make') or 'N/A'}")
            print(f"  Model:         {vehicle.get('Model') or 'N/A'}")
            print(f"  Trim:          {vehicle.get('Trim') or 'N/A'}")
            print(f"  Body Class:    {vehicle.get('BodyClass') or 'N/A'}")
            print(f"  Drive Type:    {vehicle.get('DriveType') or 'N/A'}")
            print(f"  Engine Specs:  {vehicle.get('DisplacementL')}L {vehicle.get('EngineConfiguration')} {vehicle.get('EngineCylinders')} Cyl")
            print(f"  Fuel Type:     {vehicle.get('FuelTypePrimary') or 'N/A'}")
            print(f"  Plant Country: {vehicle.get('PlantCountry') or 'N/A'}")
            print(f"  Stolen Status: {stolen_info}")
            print("=" * 40 + "\n")

    except requests.exceptions.RequestException as e:
        print(f"[!] Network error occurred: {e}")

if __name__ == "__main__":
    user_vin = input("Enter 17-digit VIN: ").strip()
    if len(user_vin) == 17:
        # Pass your commercial API key inside quotes if you have one, e.g., lookup_vin(user_vin, "YOUR_KEY_HERE")
        lookup_vin(user_vin)
    else:
        print("[!] Error: VIN must be exactly 17 characters.")
