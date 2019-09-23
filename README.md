# Analytics Model Deployment

Model ini dibuat dengan memanfaatkan data record nasabah pelaku kredit dari data Astra Credit Scoring pada [Link ini](https://github.com/khairunisa6/Study-Case-Astra-Creditscore). Dataset tersebut berisi informasi terkait nasabah kartu kredit di suatu negara pada periode Januari - Maret 2015. Pada dataset terdapat 16 features yang terdiri dari ID, 14 prediktor dan 1 target. Ke-14 Prediktor tersebut terdiri atas usia, batas maksimal kredit, pendidikan, status pernikahan, jenis kelamin, pembayaran ke-1 2 dan 3, jumlah tagihan ke-1 2 dan 3, serta jumlah yang dibayarkan ke-1 2 dan 3.

## Credit Scoring Model

Pada model credit scoring ini digunakan metode random forest classifier dengan memanfaatkan 5 features yang dipilih dari dataset di atas. Features terpilih terdiri atas usia, status pernikahan, pembayaran ke-1 2 dan 3. Dari kelima features tersebut akan dibuat model credit scoring yang dapat mewakili karakteristik nasabah pelaku kredit di negara tersebut. Sehingga dapat dimanfaatkan untuk memprediksi nasabah lain di area yang sama apakah kredit yang diajukan dapat dipenuhi ataupun tidak. Metode credit scoring yang digunakan pada dataset tersebut adalah dengan random forest classifier.

## File Terlampir Pada Github
1. **modelcreditscoring.pkl** : model credit scoring dengan random forest classifier yang dimsimpen dalam ekstensi pickel. File ini dapat digunakan untuk deployment model dengan postman.
2. **modelcreditscoring.py** : model credit scoring dengan random forest classifier yang disimpan dalam ekstensi python. File ini dapat digunakan untuk deployment pada localhost server.
2. **serverCS.py** : file dengan ekstensi python yang digunakan untuk request POST, memuat kebutuhan untuk flask, dan untuk memanage API.
3. **requestCS.py** : berisi code python yang digunakan untuk memproses request POST ke server.

## Langkah-langkah Menjalankan Model Credit Scoring
1. 
