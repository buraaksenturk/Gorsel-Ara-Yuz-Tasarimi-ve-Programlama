-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 21 Haz 2020, 17:13:37
-- Sunucu sürümü: 10.4.11-MariaDB
-- PHP Sürümü: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `farabirandevu`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `iletisim`
--

CREATE TABLE `iletisim` (
  `iletisim_id` int(11) NOT NULL,
  `kullanici_tc` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `kullanici_eposta` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `mesaj` text COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `iletisim`
--

INSERT INTO `iletisim` (`iletisim_id`, `kullanici_tc`, `kullanici_eposta`, `mesaj`) VALUES
(1, '1', 'Buraak.senturk@gmail.com', 'Sisteminiz Çok Hoş'),
(2, '1', 'farabi@gmail.com', 'Hastane'),
(11, '2', 'emredemir@gmail.com', 'Çok iyi bir uygulama');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanici`
--

CREATE TABLE `kullanici` (
  `kullanici_id` int(11) NOT NULL,
  `adsoyad` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `tc` bigint(20) NOT NULL,
  `sifre` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `tel` bigint(20) NOT NULL,
  `cinsiyet` varchar(255) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kullanici`
--

INSERT INTO `kullanici` (`kullanici_id`, `adsoyad`, `tc`, `sifre`, `tel`, `cinsiyet`) VALUES
(1, 'Burak Şentürk', 1, '1', 5412015257, 'Erkek'),
(2, 'Emre Demir', 2, '2', 5326022448, 'Erkek'),
(3, 'Orhan Enes Kılıç', 3, '3', 5316205361, 'Erkek');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `randevular`
--

CREATE TABLE `randevular` (
  `randevu_id` int(11) NOT NULL,
  `kullanici_tc` int(11) NOT NULL,
  `tarih` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `klinik` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `doktor` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `saat` varchar(50) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `randevular`
--

INSERT INTO `randevular` (`randevu_id`, `kullanici_tc`, `tarih`, `klinik`, `doktor`, `saat`) VALUES
(1, 2, '1Ocak2020', 'Çocuk Sağlığı ve Hastalıkları', 'Dr.Ahmet Güvenç', '10:00'),
(2, 1, '2Şubat2021', 'Dahiliye - İç Hastalıkları', 'Dr.Murat Hamdi Övüç', '11:00'),
(3, 3, '1Mart2022', 'Dahiliye - İç Hastalıkları', 'Dr.Murat Hamdi Övüç', '14:00'),
(4, 3, '4Şubat2020', 'Kadın Hastalıkları ve Doğum', 'Op.Dr.Korhan Enis Kalça', '11:00'),
(5, 3, '9Temmuz2020', 'Kulak Burun Boğaz hastalıkları - KBB', 'Dr.Emel Temel', '13:00'),
(6, 2, '8Temmuz2020', 'Dermatoloji', 'Dr.Sait Atmaca', '17:00'),
(7, 2, '28Aralık2020', 'Çocuk Sağlığı ve Hastalıkları', 'Dr.Şafak Ersöz', '14:00'),
(8, 2, '3Eylül2020', 'Dermatoloji', 'Dr.Seda Özbakır', '19:00'),
(9, 1, '24Temmuz2020', 'Dahiliye - İç Hastalıkları', 'Yrd.Doç.Dr.Burak Şen', '13:00'),
(10, 1, '4Ağustos2020', 'Kulak Burun Boğaz hastalıkları - KBB', 'Dr.Ayhan Aydın', '11:00'),
(11, 1, '6Kasım2020', 'Çocuk Sağlığı ve Hastalıkları', 'Dr.Gülçin Yıldız', '14:00');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `iletisim`
--
ALTER TABLE `iletisim`
  ADD PRIMARY KEY (`iletisim_id`);

--
-- Tablo için indeksler `kullanici`
--
ALTER TABLE `kullanici`
  ADD PRIMARY KEY (`kullanici_id`);

--
-- Tablo için indeksler `randevular`
--
ALTER TABLE `randevular`
  ADD PRIMARY KEY (`randevu_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `iletisim`
--
ALTER TABLE `iletisim`
  MODIFY `iletisim_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Tablo için AUTO_INCREMENT değeri `kullanici`
--
ALTER TABLE `kullanici`
  MODIFY `kullanici_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `randevular`
--
ALTER TABLE `randevular`
  MODIFY `randevu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
