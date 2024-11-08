from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # Get form data
        energy = float(request.form['energy'])
        fuel = float(request.form['fuel'])
        methane = float(request.form['methane'])
        transportation = float(request.form['transportation'])
        commute = float(request.form['commute'])
        waste = float(request.form['waste'])
        water = float(request.form['water'])
        land = float(request.form['land'])

        # Carbon footprint calculations for one year (multiply by 12 for monthly data)
        energy_footprint = energy * 0.92 * 12  # Example factor for energy consumption (yearly)
        fuel_footprint = fuel * 2.31 * 12  # Example factor for fuel combustion (yearly)
        methane_footprint = methane * 25 * 12  # Methane emissions factor (yearly)
        transportation_footprint = transportation * 1.45 * 12  # Transportation emissions (yearly)
        commute_footprint = commute * 0.78 * 12  # Commute emissions (yearly)
        waste_footprint = waste * 0.9 * 12  # Waste (yearly)
        water_footprint = water * 0.0065 * 12  # Water usage (yearly)
        land_footprint = land * 0.04 * 12  # Land use changes (yearly)

        # Debugging statements
        print(f"Energy Footprint: {energy_footprint}")
        print(f"Fuel Footprint: {fuel_footprint}")
        print(f"Methane Footprint: {methane_footprint}")
        print(f"Transportation Footprint: {transportation_footprint}")
        print(f"Commute Footprint: {commute_footprint}")
        print(f"Waste Footprint: {waste_footprint}")
        print(f"Water Footprint: {water_footprint}")
        print(f"Land Footprint: {land_footprint}")

        # Total carbon footprint for one year
        total_footprint = energy_footprint + fuel_footprint + methane_footprint + transportation_footprint + commute_footprint + waste_footprint + water_footprint + land_footprint

        # Render result page with calculated values
        return render_template(
            'result.html',
            total_footprint=total_footprint,
            energy=energy_footprint,
            fuel=fuel_footprint,
            waste=waste_footprint,
            water=water_footprint,
            transportation=transportation_footprint
        )

    # If GET request, just show the form
    return render_template('calculate.html')

if __name__ == '__main__':
    app.run(debug=True)
