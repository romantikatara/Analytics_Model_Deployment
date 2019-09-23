# Analytics Model Deployment
Model ini dibuat dengan memanfaatkan data record nasabah pelaku kredit dengan memanfaatkan data Astra Credit Scoring. Data tersebut didapat dari [Astra Credit Scoring](https://github.com/khairunisa6/Study-Case-Astra-Creditscore).

Dataset berisi informasi terkait nasabah kartu kredit di suatu negara pada periode Januari - Maret 2015. Informasi meliputi latar belakang pelanggan, jumlah tagihan, jumlah pembayaran, lama terlambat bayar dan status pembayaran bulan berikutnya (April 2015).

Terdapat 16 features yang terdiri dari ID, 14 prediktor dan 1 target. 14 Prediktor tersebut terdiri atas usia, batas maksimal kredit, pendidikan, status pernikahan, jenis kelamin, pembayaran ke-1 2 dan 3, jumlah tagihan ke-1 2 dan 3, serta jumlah yang dibayarkan ke-1 2 dan 3.

## Credit Scoring Model
Pada model credit scoring ini digunakan metode random forest classifier dengan memanfaatkan 5 features yang dipilih dari dataset di atas. Features terpilih terdiri atas usia, status pernikahan, pembayaran ke-1 2 dan 3. Dari kelima featres tersebut akan dibuat model credit scoring yang dapat mewakili karakteristik nasabah pelaku kredit di negara tersebut.

Model credit scoring yang terlah dibuat disimpan pada file modelcreditscoring.pkl dan modelcreditscoring.py. Untuk running

## Server

Server 
## Request
