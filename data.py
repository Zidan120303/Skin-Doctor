# Data penyakit kulit
data_penyakit_kulit = [
    ['P01', 'Eksim'],
    ['P02', 'Dermatitis'],
    ['P03', 'Impetigo'],
    ['P04', 'Jerawat'],
    ['P05', 'Kudis'],
    ['P06', 'Kurap'],
    ['P07', 'Panu'],
    ['P08', 'Lichen Planus'],
    ['P09', 'Hives'],
]
# Data gejala
data_gejala = [
    ['G01', 'Rasa Panas dan dingin yang berlebihan pada bagian kulit yang terkena eksim.'],
    ['G02', 'Rasa gatal terutama terasa pada malam hari.'],
    ['G03', 'Tampak lepuhan-lepuhan kecil dan kulit bersisik yang keras pada permukaan kulit yang akan disertai dengan pembengkakan.'],
    ['G04', 'Kulit kering, bersisik, kemerahan.'],
    ['G05', 'Timbul bintil-bintil yang mengandung air atau nanah.'],
    ['G06', 'Ruam kemerahan.'],
    ['G07', 'Peradangan.'],
    ['G08', 'Gatal yang kadang-kadang terasa parah.'],
    ['G09', 'Kering.'],
    ['G10', 'Pembengkakan.'],
    ['G11', 'Kulit kering.'],
    ['G12', 'Bersisik.'],
    ['G13', 'Lecet melepuh.'],
    ['G14', 'Menebal.'],
    ['G15', 'Pecah-pecah.'],
    ['G16', 'Kulit melepuh dan berisi cairan.'],
    ['G17', 'Pecahan kulit yang melepuh dan berwarna kuning.'],
    ['G18', 'Munculnya bercak merah menyerupai luka yang tidak terasa sakit, namun gatal.'],
    ['G19', 'Bercak bisa menyebar dalam waktu singkat ketika disentuh atau digaruk, kemudian berganti menjadi kerak berwarna kecokelatan.'],
    ['G20', 'Munculnya bintik-bintik.'],
    ['G21', 'Kulit berminyak.'],
    ['G22', 'Sakit atau panas apabila disentuh.'],
    ['G23', 'Gatal yang sangat terasa pada permukaan kulit.'],
    ['G24', 'Berwarna kemerahan dan biasanya disertai infeksi lanjutan seperti yang diakibatkan oleh bakteri maupun jamur.'],
    ['G25', 'Bisul pada telapak tangan atau kaki.'],
    ['G26', 'Ruam kemerahan yang berbentuk cincin dengan garis luar yang tidak beraturan.'],
    ['G27', 'Ruam terasa bersisik dan gatal.'],
    ['G28', 'Lingkaran ruam kurap juga dapat melebar dan muncul di bagian tubuh mana saja.'],
    ['G29', 'Ruam membentuk benjolan dan melepuh.'],
    ['G30', 'Kulit pecah-pecah di bagian yang terinfeksi serta kulit bersisik.'],
    ['G31', 'Ruam yang gatal, kering, dan terkelupas di antara jari kaki.'],
    ['G32', 'Rasa gatal ketika berkeringat dan warna sebagian kulit berubah menjadi putih.'],
    ['G33', 'Terdapat sisik halus yang menutupinya.'],
    ['G34', 'Benjolan berwarna ungu kemerahan dengan bagian atas yang rata dan mengkilat.'],
    ['G35', 'Terbentuknya sebagian kulit yang menebal dan bersisik, biasanya di sekitar pergelangan kaki.'],
    ['G36', 'Terasa gatal.'],
    ['G37', 'Perubahan warna kulit menjadi gelap setelah benjolan-benjolan mereda.'],
    ['G38', 'Adanya warna merah pada kulit serta ruam gatal.'],
    ['G39', 'Gatal-gatal disertai kemerahan pada kulit.'],
    ['G40', 'Busung.'],
    ['G41', 'Kulit terasa panas.'],
    ['G42', 'Pembengkakan yang berlebihan dari kelopak mata.'],
    ['G43', 'Kesulitan bernafas atau menelan.'],
]
# Data aturan/rules
data_aturan = [
    ['1', 'G01,G02,G03,G04,G05', 'P01', 'Eksim'],
    ['2', 'G06,G07,G08,G09,G10,G11,G12,G13,G14,G15', 'P02', 'Dermatitis'],
    ['3', 'G16,G17,G18,G19', 'P03', 'Impetigo'],
    ['4', 'G20,G21,G22', 'P04', 'Jerawat'],
    ['5', 'G23,G24,G25', 'P05', 'Kudis'],
    ['6', 'G26,G27,G28,G29,G30,G31', 'P06', 'Kurap'],
    ['7', 'G32,G33', 'P07', 'Panu'],
    ['8', 'G34,G35,G36,G37', 'P08', 'Lichen Planus'],
    ['9', 'G38,G39,G40,G41,G42,G43', 'P09', 'Hives']
]
# Data solusi dan informasi penyakit
solusi_penyakit = {
    'Eksim': {
        'solusi': [
            'Pengobatan Eksim \n Dipercaya jika belum ada obat yang dapat mengatasi eksim. Perawatan terhadap kondisi ini bertujuan untuk menyembuhkan kulit yang terserang serta mencegah gejalanya.berikut beberapa cara pengobatan yang bisa dilakukan:\n\n Pengobatan rumahan\n Ada beberapa perawatan rumahan yang bisa dilakukan untuk mengatasi eksim, yaitu: \n- Mandi dengan air hangat. \n- Mengoleskan pelembap setelah mandi. \n- Menggunakan pelembap setiap hari. \n- Memakai katun dan kain lembut. \n- Menghindari bahan pakaian yang kasar, gatal, serta pakaian yang ketat. \n- Menggunakan pelembap udara dalam cuaca yang kering atau dingin. \n- Menghindari pemicu terjadinya eksim. \n\n Dan jika Pengobatan rumahan ini tidak berhasil anda harus konsultasi ke dokter spesialis kulit di rumah sakit yang ada di sekitar tempat tinggal anda.'
        ],
        'info': [
            'Eksim adalah istilah terkait gangguan pembengkakan pada kulit. Gangguan ini disebut juga dengan dermatitis. Saat terjadi, reaksi alergi pada kulit dapat ditandai dengan timbulnya warna kemerahan, ruam, dan rasa gatal. Kondisi ini dapat menimbulkan rasa tidak nyaman serta mengganggu penampilan.\nEksim bukan penyakit yang menular dan sejauh ini penyebabnya belum diketahui. Kemungkinan besar terjadi akibat adanya faktor genetik dan lingkungan. Seseorang yang mengidap demam dan asma biasanya juga memiliki penyakit ini. Penyakit yang disebut dermatitis ini juga dapat menjadi penyakit yang dapat bertahan lama.\n\nGejala Eksim :\nSemua orang dapat mengalami eksim tanpa terkecuali, dari orang dewasa hingga anak-anak. Gejalanya pun dapat muncul sejak seseorang usianya sudah di atas dua tahun. Eksim bisa menghilang seiring bertambahnya usia, tetapi juga bisa menjadi penyakit seumur hidup.\nNah, gejala eksim paling umum yang dapat timbul saat gangguan ini terjadi adalah : \n- Kulit yang menjadi kering dan bersisik.\n- Kulit yang memerah.\n- Terasa gatal.\n- Luka yang terbuka atau berkerak.'
        ],
        'url' : 'https://static.honestdocs.id/989x500/webp/system/blog_articles/main_hero_images/000/006/219/original/iStock-1076980556_%281%29.jpg'
    },
    'Dermatitis': {
        'solusi': [
            'Pengobatan\n\n1. Mengompres dingin\nKompres dingin bertujuan untuk meredakan gatal tanpa menggaruknya. Bungkuslah beberapa buah es dengan handuk, lalu tempelkan ke kulit selama 20 menit sebanyak 3-4 kali sehari.\n\n2. Mandi air hangat\nMandi air hangat juga membantu meredakan gatal-gatal yang mengganggu. Namun, jangan mandi terlalu lama atau dengan air yang terlalu panas karena hal ini justru membuat kulit makin kering sehingga memperparah gejala.\n\n3. Jangan menggaruk kulit\nAgar kondisi kulit tidak bertambah parah, jangan menggaruk terlalu keras bagian kulit Anda yang terkena dermatitis. Sebagai gantinya, cobalah menepuk-nepuk, mencubit lembut, atau menggunakan kompres untuk meredakan gatal.\n\n4. Gunakan pakaian berbahan katun\nPakaian berbahan katun membantu mencegah iritasi akibat eksim. Selain menyerap keringat, bahan ini juga aman dan lembut di kulit sehingga tidak akan melukai area yang terkena dermatitis.\n\n5. Lakukan kegiatan menyenangkan\nStres adalah salah satu hal yang memperparah gejala dermatitis. Anda bisa mencoba menghalaunya dengan kegiatan menyenangkan seperti yoga, melakukan hobi baru, mendengarkan musik, atau sekadar menarik napas dalam-dalam agar tubuh rileks.\n\n6. Mengoleskan tea tree oil\nTea tree oil mengandung zat antijamur, dan antiradang sehingga membantu mengatasi dermatitis seboroik. Cukup campurkan beberapa tetes tea tree oil dengan minyak kelapa atau zaitun, lalu oleskan ke kulit kepala Anda secara rutin.\n\n7. Menggunakan aloe vera\nLidah buaya termasuk tanaman dengan kandungan antiradang yang tinggi. Sebuah studi yang diterbitkan dalam Indian Journal of Dermatology bahkan menyebutkan bahwa ekstrak tanaman ini bisa meringankan gejala dermatitis seboroik.\n\n8. Minum suplemen minyak ikan\nSuplemen minyak ikan membantu menekan gejala dermatitis yang dipicu oleh alergi. Selain itu, suplemen yang satu ini juga membantu menjaga kesehatan tubuh secara keseluruhan karena mengandung asam lemak omega 3.\n\nDan jika Pengobatan rumahan ini tidak berhasil anda harus konsultasi ke dokter spesialis kulit di rumah sakit yang ada di sekitar tempat tinggal anda.'
        ],
        'info': [
            'Penyakit kulit dermatitis adalah penyakit kulit yang disebabkan oleh peradangan akibat kontak langsung dengan zat iritan (mudah mengiritasi kulit) atau alergen (pemicu alergi) di lingkungan sekitar. Masalah kulit ini juga dapat dipengaruhi oleh faktor genetik.\nGejala utamanya adalah ruam bengkak kemerahan yang tampak sangat kering dan terasa gatal. Kulit yang terdampak biasanya terasa nyeri ketika disentuh serta dipenuhi lepuhan kecil yang dapat mengelupas mengeluarkan cairan.\nDermatitis bukan penyakit kulit menular. Meski begitu, gejalanya perlu dikenali sejak dini. Penyakit ini bisa dikendalikan dengan baik melalui kombinasi pengobatan dan pencegahan kontak terhadap hal-hal yang memicu peradangan kulit.'
        ],
        'url' : 'https://res.cloudinary.com/dk0z4ums3/image/upload/v1667887108/attached_image/dermatitis-0-alodokter.jpg'
    },
    'Impetigo': {
        'solusi': [
            'Pengobatan Impetigo :\nSalep atau krim antibiotik, seperti mupirocin atau polymyxin B, digunakan jika infeksi yang terjadi tergolong ringan, hanya menyerang satu area tubuh, dan belum menyebar terlalu luas. Sebelum mengoleskan krim atau krim antibiotik, dianjurkan untuk merendam luka dengan air hangat atau mengompres hangat untuk melunakkan koreng.\nJika impetigo bertambah parah dan mulai menyebar ke bagian tubuh lainnya, dokter akan memberikan antibiotik dalam bentuk tablet, seperti clindamycin atau antibiotik golongan sefalosporin.'
        ],
        'info': [
            'Impetigo adalah infeksi kulit menular yang banyak dialami oleh bayi dan anak-anak. Infeksi ini ditandai dengan kemunculan bercak merah dan lepuhan di kulit, terutama di wajah, tangan, dan kaki.'
        ],
        'url' : 'https://asset.kompas.com/crops/7XwxHD0rtoCeYPoarP1RdF683B4=/96x36:896x570/1200x800/data/photo/2022/03/26/623e5ffa8380d.jpg'
    },
    'Jerawat': {
        'solusi': [
            'Pengobatan dan Pencegahan Jerawat\n\nPengobatan jerawat disesuaikan dengan tingkat keparahan kondisinya. Pengobatan jerawat terbagi menjadi dua, yaitu pemberian obat untuk mengatasi atau menghilangkan jerawat, dan terapi estetika untuk membantu pengobatan jerawat serta memperbaiki penampilan kulit.'
        ],
        'info': [
            'Jerawat adalah masalah kulit yang terjadi ketika pori-pori kulit, tepatnya folikel rambut, tersumbat oleh kotoran, debu, minyak, atau sel kulit mati.'
        ],
        'url' : 'https://res.cloudinary.com/dk0z4ums3/image/upload/v1655092166/attached_image/jerawat-0-alodokter.jpg'
    },
    'Kudis': {
        'solusi': [
            'Pengobatan Kudis\nDianjurkan untuk melakukan pemeriksaan ke dokter.\n\n Penanganan scabies bertujuan untuk membasmi tungau, meredakan gatal dan peradangan, serta mengatasi infeksi sekunder.'
        ],
        'info': [
            'Kudis adalah kondisi yang ditandai dengan gatal di kulit, terutama di malam hari. Gatal ini disertai dengan kemunculan ruam berbintik yang menyerupai jerawat atau lepuhan kecil bersisik.'
        ],
        'url' : 'https://res.cloudinary.com/dk0z4ums3/image/upload/v1679899670/attached_image/kenali-5-obat-kudis-di-apotek-0-alodokter.jpg'
    },
    'Kurap': {
        'solusi': [
            'Pengobatan dan Pencegahan Kurap\n\nKurap dapat diatasi dengan salep kurap atau antijamur, seperti clotrimazole atau miconazole.'
        ],
        'info': [
            'Kurap adalah infeksi jamur pada kulit yang menimbulkan ruam melingkar berwarna merah.'
        ],
        'url' : 'https://asset.kompas.com/crops/MCN6CEsf797au1sw04CpoeHf8c4=/0x0:600x400/1200x800/data/photo/2023/03/11/640c656ea8fb2.png'
    },
    'Panu': {
        'solusi': [
            'Pengobatan dan Pencegahan Panu\n\nPengobatan panu adalah dengan pemberian obat antijamur.'
        ],
        'info': [
            'Panu adalah infeksi jamur pada kulit yang disebabkan oleh golongan jamur Malassezia.'
        ],
        'url' : 'https://res.cloudinary.com/dk0z4ums3/image/upload/v1672042369/attached_image/panu-0-alodokter.jpg'
    },
    'Lichen Planus': {
        'solusi': [
            'Dianjurkan untuk melakukan pemeriksaan ke dokter. \n\nPengobatan lichen planus bertujuan untuk meredakan gejala, mencegah munculnya komplikasi, dan menurunkan risiko terjadinya kekambuhan penyakit ini di kemudian hari.'
        ],
        'info': [
            'Lichen planus adalah peradangan di kulit, kuku, atau selaput lendir (mukosa) akibat adanya kelainan pada sistem kekebalan tubuh.'
        ],
        'url' : 'https://res.cloudinary.com/dk0z4ums3/image/upload/v1660619446/attached_image/lichen-planus-0-alodokter.jpg'
    },
    'Hives': {
        'solusi': [
            'Pengobatan dan Pencegahan Biduran/Hives\n\nBiduran ringan biasanya akan sembuh tanpa pengobatan.'
        ],
        'info': [
            'Biduran adalah reaksi di kulit yang ditandai dengan munculnya bentol berwarna kemerahan dan disertai rasa gatal.'
        ],
        'url' : 'https://www.houstonent.com/hubfs/shutterstock_2021018495%20%281%29.jpg'
    }
}
