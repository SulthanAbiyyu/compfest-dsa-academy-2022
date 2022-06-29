# Problem Set

Karena kita punya data covid sama mobilitas, jadi menurutku masalah yang akan kita selesaiin nggak jauh-jauh dari bikin saran kebijakan PSBB ke pemerintah.

Akhir-akhir ini covid mulai naik lagi, ditambah hasil forecast pake model SARIMA menunjukkan kalau bulan oktober memungkinkan bakal jadi puncak covid lagi.

![SARIMA](https://github.com/SulthanAbiyyu/compfest-dsa-academy-2022/blob/master/img/SARIMA%20Forecast/output.png)

Tugas kita untuk nentuin sweet spotnya, kira-kira level PSBB yang pas untuk mengurangi lonjakan di bulan oktober tapi tidak mengurangi mobilitas secara signifikan itu seberapa?

Salah satu pendekatan yang aku usulin buat nentuin hubungan 2 variabel yang berbeda (data covid sama mobilitas) itu bisa pakai [causal inference](https://www.youtube.com/watch?v=Od6oAz1Op2k).

- Covid mau naik
- Didukung berita akhir2 ini covid mulai naik
- Bagaimana langkah preventif yang sebaiknya diambil oleh pemerintah untuk mengantisipasi lonjakan kenaikan kasus covid
