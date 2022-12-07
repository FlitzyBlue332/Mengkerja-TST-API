# API-Authentication  

Repositori ini dibuat untuk tugas implementasi autentikasi API pada matkul TST.  
Repositori ini juga akan dipakai sebagai dasar dari API utama yang akan digunakan untuk tugas akhir TST. 


Jika API baru pertama kali dinyalakan, Terdapat fungsi yang tidak dapat diakses oleh pengguna dikarenakan pengguna belum melakukan autentikasi. fungsi-fungsi yang memerlukan autentikasi adalah:  
1. Fungsi Sign Up
2. Fungsi Post untuk menambah post  

link menuju API yang sudah dideploy: https://finalauth1flitzyblue332.azurewebsites.net/  

untuk mengecek apakah API berjalan atau tidak dapat melakukan HTTP request dibawah:
>curl -X 'GET' \
  'https://finalauth1flitzyblue332.azurewebsites.net' \
  -H 'accept: application/json'
>

# Autentikasi
Untuk melakukan autentikasi, user harus melakukan beberapa hal berikut
1. Login dengan menggunakan akun yang sudah ada. Secara default akun saat ini: 
> email: FlitzyBlue332@sugarmail.com  
password: Minut200130
>
untuk melakukan login dapat melakukan HTTP request dibawah
> curl -X 'POST' \
  'https://finalauth1flitzyblue332.azurewebsites.net/user/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "FlitzyBlue332@sugarmail.com",
  "password": "Minut200130"
}'
>
setelah itu user dapat melakukan sign up jika user ingin menambah lebih banyak akun yang dapat menggunakan fungsi-fungsi API. Untuk melakukan sign up, user dapat melakukan HTTP request seperti dibawah ini
>curl -X 'POST' \
  'https://finalauth1flitzyblue332.azurewebsites.net/user/signup' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer TOKEN  \ 
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username",
  "email": "youremail@sugarmail.com",
  "password": "passw0rd"
}'
>
ganti "TOKEN" dengan access token yang anda dapatkan dari API setelah melakukan login

Untuk menggunakan fitur seperti Merequest HTTP POST, user dapat melakukan sesuai dengan dibawah ini
> curl -X 'POST' \
  'https://finalauth1flitzyblue332.azurewebsites.net/posts' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer TOKEN \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Sugar",
  "content": "Wangy Wangy Wangy Wangy"
}'
>
ganti "TOKEN" dengan access token yang anda dapatkan dari API setelah melakukan login

Untuk mengecek posts sekarang, dapat melakukan request seperti dibawah
>curl -X 'GET' \
  'https://finalauth1flitzyblue332.azurewebsites.net/posts' \
  -H 'accept: application/json'
>