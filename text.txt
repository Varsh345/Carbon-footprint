from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/calculate', methods=['GET', 'POST'])

def calculate():
    if request.method == 'POST':
        # Get the input values from the form
        energy = float(request.form.get('energy', 0))
        fuel = float(request.form.get('fuel', 0))
        waste = float(request.form.get('waste', 0))
        water = float(request.form.get('water', 0))
        transportation = float(request.form.get('transportation', 0))
        months = int(request.form.get('months', 1))

        # Emission factors (example values in kg CO2 per unit)
        energy_emission_factor = 0.5  # kg CO2 per kWh
        fuel_emission_factor = 2.5  # kg CO2 per liter
        waste_emission_factor = 0.1  # kg CO2 per kg of waste
        water_emission_factor = 0.002  # kg CO2 per liter of water
        transportation_emission_factor = 0.2  # kg CO2 per km

        # Calculate emissions for one month
        energy_emissions = energy * energy_emission_factor
        fuel_emissions = fuel * fuel_emission_factor
        waste_emissions = waste * waste_emission_factor
        water_emissions = water * water_emission_factor
        transportation_emissions = transportation * transportation_emission_factor

        # Total monthly carbon footprint
        monthly_footprint = (energy_emissions + fuel_emissions + waste_emissions +
                             water_emissions + transportation_emissions)

        # Total carbon footprint for the specified number of months
        total_footprint = monthly_footprint * months
        print("12345432", total_footprint)
        return render_template('result.html', total_footprint=total_footprint, energy=energy_emissions,
                               fuel=fuel_emissions, waste=waste_emissions, water=water_emissions,
                               transportation=transportation_emissions)

    return render_template('calculate.html')

if __name__ == '__main__':
    app.run(debug=True)
