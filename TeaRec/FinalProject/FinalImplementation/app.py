from flask import Flask, render_template, request
import csv

app = Flask(__name__)

if __name__ == "__main__": 
   app.run() 

app.static_folder= 'static'

@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/preferences", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("taste") or not request.form.get("effect"):
        return render_template("error.html")
    file = open("list.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("taste"), request.form.get("effect")))
    file.close()
    # Group 1-Flowery
    if request.form.get("taste") == "Flowery" and request.form.get("effect") == "Nerves":
        return render_template("Group_1_Flowery/1.1fl_ne.html")
    if request.form.get("taste") == "Flowery" and request.form.get("effect") == "Stomach":
        return render_template("Group_1_Flowery/1.2fl_sto.html")
    if request.form.get("taste") == "Flowery" and request.form.get("effect") == "Cold":
        return render_template("Group_1_Flowery/1.3fl_co.html")
    if request.form.get("taste") == "Flowery" and request.form.get("effect") == "Blood Pressure":
        return render_template("Group_1_Flowery/1.4fl_bp.html")
    if request.form.get("taste") == "Flowery" and request.form.get("effect") == "Weight":
        return render_template("Group_1_Flowery/1.5fl_w.html")
    # Group 2-Sweet
    if request.form.get("taste") == "Sweet" and request.form.get("effect") == "Nerves":
        return render_template("Group_2_Sweet/2.1swe_ne.html")
    if request.form.get("taste") == "Sweet" and request.form.get("effect") == "Stomach":
        return render_template("Group_2_Sweet/2.2swe_sto.html")
    if request.form.get("taste") == "Sweet" and request.form.get("effect") == "Cold":
        return render_template("Group_2_Sweet/2.3swe_co.html")
    if request.form.get("taste") == "Sweet" and request.form.get("effect") == "Blood Pressure":
        return render_template("Group_2_Sweet/2.4swe_bp.html")
    if request.form.get("taste") == "Sweet" and request.form.get("effect") == "Weight":
        return render_template("Group_2_Sweet/2.5swe_w.html")
    # Group 3-Herbal
    if request.form.get("taste") == "Herbal" and request.form.get("effect") == "Nerves":
        return render_template("Group_3_Herbal/3.1herb_ne.html")
    if request.form.get("taste") == "Herbal" and request.form.get("effect") == "Stomach":
        return render_template("Group_3_Herbal/3.2herb_sto.html")
    if request.form.get("taste") == "Herbal" and request.form.get("effect") == "Cold":
        return render_template("Group_3_Herbal/3.3herb_co.html")
    if request.form.get("taste") == "Herbal" and request.form.get("effect") == "Blood Pressure":
        return render_template("Group_3_Herbal/3.4herb_bp.html")
    if request.form.get("taste") == "Herbal" and request.form.get("effect") == "Weight":
        return render_template("Group_3_Herbal/3.5herb_w.html")
    # Group 4-Spicy
    if request.form.get("taste") == "Spicy" and request.form.get("effect") == "Nerves":
        return render_template("Group_4_Spicy/4.1spi_ne.html")
    if request.form.get("taste") == "Spicy" and request.form.get("effect") == "Stomach":
        return render_template("Group_4_Spicy/4.2spi_sto.html")
    if request.form.get("taste") == "Spicy" and request.form.get("effect") == "Cold":
        return render_template("Group_4_Spicy/4.3spi_co.html")
    if request.form.get("taste") == "Spicy" and request.form.get("effect") == "Blood Pressure":
        return render_template("Group_4_Spicy/4.4spi_bp.html")
    if request.form.get("taste") == "Spicy" and request.form.get("effect") == "Weight":
        return render_template("Group_4_Spicy/4.5spi_w.html")
    # Group 5-Earthy
    if request.form.get("taste") == "Earthy" and request.form.get("effect") == "Nerves":
        return render_template("Group_5_Eathy/5.1ear_ne.html")
    if request.form.get("taste") == "Earthy" and request.form.get("effect") == "Stomach":
        return render_template("Group_5_Eathy/5.2ear_sto.html")
    if request.form.get("taste") == "Earthy" and request.form.get("effect") == "Cold":
        return render_template("Group_5_Eathy/5.3ear_co.html")
    if request.form.get("taste") == "Earthy" and request.form.get("effect") == "Blood Pressure":
        return render_template("Group_5_Eathy/5.4ear_bp.html")
    if request.form.get("taste") == "Earthy" and request.form.get("effect") == "Weight":
        return render_template("Group_5_Eathy/5.5ear_w.html")
    # Group 6-Fruity
    if request.form.get("taste") == "Fruity" and request.form.get("effect") == "Nerves":
        return render_template("Group_6_Fruity/6.1fru_ne.html")
    if request.form.get("taste") == "Fruity" and request.form.get("effect") == "Stomach":
        return render_template("Group_6_Fruity/6.2fru_sto.html")
    if request.form.get("taste") == "Fruity" and request.form.get("effect") == "Cold":
        return render_template("Group_6_Fruity/6.3fru_co.html")
    if request.form.get("taste") == "Fruity" and request.form.get("effect") == "Blood Pressure":
        return render_template("Group_6_Fruity/6.4fru_bp.html")
    if request.form.get("taste") == "Fruity" and request.form.get("effect") == "Weight":
        return render_template("Group_6_Fruity/6.5fru_w.html")

@app.route("/preferences")
def rsvped():
    file = open("list.csv", "r")
    reader = csv.reader(file)
    rsvps = list(reader)
    file.close()
    return render_template("list.html", preferencesR=preferences)
    
@app.route('/back')
def back():
    return render_template('index.html')




