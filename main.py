from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def baslangic():
    return render_template("index.html")

@app.route('/hakkimizda')
def hakkimizda():
    return render_template("hakkımızda.html")

@app.route('/iletisim')
def iletisim():
    return render_template("iletişim.html")

@app.route('/urun')
def urun():
    return render_template("ürün.html")

@app.route('/icecekler')
def icecekler():
    return render_template("içecekler.html")

@app.route('/kuruyemis')
def kuruyemis():
    return render_template("kuruyemiş.html")

@app.route('/sebzeler')
def sebzeler():
    return render_template("sebzeler.html")

@app.route('/meyveler')
def meyveler():
    return render_template("meyveler.html")

@app.route('/cips')
def cips():
    return render_template("cips.html")

@app.route('/mesajkaydet', methods=['POST'])
def mesaj_kaydet():
    adsoyad = request.form.get('Adınız Soyadınız')
    email = request.form.get('E-Posta Adresiniz')
    konu = request.form.get('Konu')
    mesaj = request.form.get('Lütfen Mesajınızı Buraya Yazınız...')

    satir = adsoyad + "||" + email + "||" + mesaj + "||" + konu 
    f = open("mesajlar.txt", "a")
    f.write(satir)
    f.close()
    return mesajlar()
    #return "Sayın " + adsoyad + ". Mesajınız için teşekkürler. Tüm mesajlar için tıklayın."

if __name__ == "__main__":
    app.run()