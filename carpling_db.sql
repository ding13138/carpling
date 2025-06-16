-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2025-03-05 06:24:51
-- サーバのバージョン： 10.4.28-MariaDB
-- PHP のバージョン: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `carpling_db`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `cars`
--

CREATE DATABASE carpling_db;

CREATE TABLE `cars` (
  `car_id` char(5) NOT NULL,
  `car_picture` varchar(255) NOT NULL,
  `brand` varchar(20) NOT NULL,
  `model` varchar(30) NOT NULL,
  `class` varchar(10) NOT NULL,
  `category` varchar(15) NOT NULL,
  `body_type` varchar(15) NOT NULL,
  `min_price` int(20) NOT NULL,
  `max_price` int(20) NOT NULL,
  `fuel_type` varchar(30) NOT NULL,
  `turbo` varchar(5) NOT NULL,
  `drive` varchar(10) NOT NULL,
  `length` int(10) NOT NULL,
  `width` int(10) NOT NULL,
  `height` int(10) NOT NULL,
  `weight` int(10) NOT NULL,
  `description_title` text NOT NULL,
  `description` text NOT NULL,
  `capasity` int(1) NOT NULL,
  `tag_1` varchar(50) NOT NULL,
  `tag_2` varchar(50) NOT NULL,
  `maker_url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `cars`
--

INSERT INTO `cars` (`car_id`, `car_picture`, `brand`, `model`, `class`, `category`, `body_type`, `min_price`, `max_price`, `fuel_type`, `turbo`, `drive`, `length`, `width`, `height`, `weight`, `description_title`, `description`, `capasity`, `tag_1`, `tag_2`, `maker_url`) VALUES
('10002', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001546862.jpg ', 'Toyota', 'アルファード', 'Normal', 'Family', 'ミニバン', 5100000, 10650000, 'ガソリン / ハイブリッド', 'yes', 'FF ', 4995, 1850, 1945, 2240, '上質な室内空間と走りのミニバン！', 'これはダミーテキストです。', 7, '高級志向！', '家族でお出かけ！', 'https://toyota.jp/alphard/'),
('10003', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001466311.jpg ', 'Toyota', 'シエンタ', 'Normal', 'Family', 'ミニバン', 1900000, 3230000, 'ハイブリッド', 'N/A', 'FF ', 4260, 1695, 1715, 1695, '便利で経済的なファミリーカー！', 'これはダミーテキストです。', 5, '家族でお出かけ！', 'たくさん積載！', 'https://toyota.jp/sienta/'),
('10004', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001635279.jpg ', 'Toyota', 'フリード', 'Normal', 'Family', 'ミニバン', 2500000, 3600000, 'ハイブリッド', 'N/A', 'FF ', 4310, 1720, 1780, 1520, '車格を超えた定員と積載！', 'これはダミーテキストです。', 7, '家族でお出かけ！', '運転しやすい！', 'https://www.honda.co.jp/FREED/?utm_source=google&utm_medium=cpc&utm_campaign=freed_2024frd_glis_a01&utm_term=google_cpc&utm_content=glis_rsa_2&gad_source=1&gclid=CjwKCAiAw5W-BhAhEiwApv4goMwSfUB4bIO7zZgy26aoXaoQIH9H7F0FbEqM-Vm39G4UfQIwwS2Y3xoCQv0QAvD_BwE'),
('10005', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001496533.jpg', 'Nissan', 'セレナ', 'Normal', 'Family', 'ミニバン', 2710000, 3930000, 'ガソリン(レギュラー)', 'N/A', '4WD', 4810, 1725, 1895, 1790, '先進機能と上質な空間！', 'これはダミーテキストです', 8, '家族でお出かけ！', 'たくさん積載！', 'https://www3.nissan.co.jp/vehicles/new/serena.html'),
('10006', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001518923.jpg', 'Renault', 'カングー', 'Normal', 'Family', 'ミニバン', 3950000, 4270000, 'ガソリン(ハイオク)', 'N/A', 'FF', 4490, 1860, 1810, 1560, 'フランスより愛をこめて！', 'これはダミーテキストです', 5, 'オシャレな暮らし！', 'たくさん積載！', 'https://www.renault.jp/car_lineup/kangoo/'),
('20002', ' https://nutsrv.co.jp/images/lineup/border/index/top_slide01.jpg?202502051446 ', 'ナッツRV', 'ボーダーバンクス', 'Normal', 'Luxury', 'キャンピング', 17149000, 18029000, '軽油', 'N/A', '625', 2230, 3020, 4740, 0, 'キャンピング！', 'これはダミーテキストです。', 8, 'チルキャンピング！', 'たくさん積載！', 'https://nutsrv.co.jp/lineup/border/'),
('20003', ' https://nutsrv.co.jp/images/lineup/aletta/index/top_slide01.jpg ', 'ナッツRV', 'アレッタ', 'Normal', 'Luxury', 'キャンピング', 9500000, 11673000, '軽油', 'N/A', '485', 1950, 2850, 3000, 0, 'これはダミーテキストです。', 'これはダミーテキストです。', 8, 'チルキャンピング！', 'たくさん積載！', 'https://nutsrv.co.jp/lineup/aletta/'),
('20004', ' https://nutsrv.co.jp/images/lineup/cresson/index/top_slide01.jpg ', 'ナッツRV', 'クレソンジャーニー', 'Normal', 'Luxury', 'キャンピング', 8584000, 10817000, '軽油', 'N/A', '499', 2080, 2900, 3000, 0, 'これはダミーテキストです。', 'これはダミーテキストです。', 8, 'チルキャンピング！', 'たくさん積載！', 'https://nutsrv.co.jp/lineup/cresson/'),
('30002', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001416092.jpg ', 'Nissan', 'フェアレディZ', 'Normal', 'Luxury', 'クーペ', 5490000, 9300000, 'ガソリン(ハイオク)', 'yes', 'FR', 4410, 1870, 1315, 1580, '最新の\"Z\"は歴代最速で最強！', 'これはダミーテキストです。', 4, '高級志向！', 'イケてるスポーツ！', 'https://www3.nissan.co.jp/vehicles/new/z.html'),
('30003', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001351053.jpg ', 'Toyota', 'GR86', 'Normal', 'Celibate', 'クーペ', 2930000, 3990000, 'ガソリン(ハイオク)', 'yes', 'FR', 4265, 1775, 1310, 1490, 'お手頃な本格スポーツカー！', 'これはダミーテキストです。', 4, 'イケてるスポーツ！', '運転しやすい！', 'https://toyota.jp/gr86/'),
('40002', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001459500.jpg ', 'Honda', 'シビック', 'Normal', 'Family', 'コンパクト', 4990000, 5990000, 'ガソリン(ハイオク)', 'yes', 'FF', 4595, 1890, 1405, 1430, '走りのVTECでもファミリー指向！', 'これはダミーテキストです', 5, '高級志向！', '攻めた走り！', 'https://www.honda.co.jp/CIVIC/'),
('40003', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001362084.jpg ', 'Nissan', 'ノートオーラ', 'Normal', 'Celibate', 'コンパクト', 2770000, 3170000, 'ハイブリッド', 'N/A', 'FF ', 4120, 1735, 1525, 1420, 'ワンランク上の室内と軽快な走り！', 'これはダミーテキストです', 5, '運転しやすい！', '燃費良好！', 'https://www3.nissan.co.jp/vehicles/new/aura.html'),
('40004', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001287745.jpg ', 'Toyota', 'GRヤリス', 'Normal', 'Luxury', 'コンパクト', 3490000, 8450000, 'ガソリン(レギュラー)', 'yes', 'AWD', 3995, 1805, 1475, 1300, '攻めの本格ホットハッチ！', 'これはダミーテキストです。', 5, 'イケてるスポーツ！', '攻めた走り！', 'https://toyota.jp/gryaris/'),
('40005', 'https://toyota.jp/tcv/resources/yaris/001_p_013/images/assy/4v8/mxph14-ahxnb_0_30.png', 'Toyota', 'ヤリス(Xグレード)', 'Normal', 'Family', 'コンパクト', 1657700, 2407900, 'ガソリン / ハイブリッド', 'N/A', 'FF', 3950, 1695, 1510, 980, 'トヨタの傑作コンパクト！', 'これはダミーテキストです', 5, 'たくさん積載！', '運転しやすい！', 'https://toyota.jp/yaris/'),
('40006', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001207577.jpg', 'Audi', 'A1 S line TFSI', 'Normal', 'Luxury', 'コンパクト', 3510000, 3760000, 'ガソリン(ハイオク)', 'yes', 'FF', 4040, 1745, 1435, 1220, '欧州の傑作ハッチバック！', 'これはダミーテキストです。', 5, 'オシャレな暮らし！', 'たくさん積載！', 'https://www.audi.co.jp/ja/models/a1/a1_sportback/#Audi-A1-Sportback'),
('40007', 'https://toyota.jp/tcv/resources/yaris/001_p_013/images/assy/2vp/mxph14-ahxeb(s)_0_30.png', 'Toyota', 'ヤリス(Z “URBANO”)', 'Normal', 'Luxury', 'コンパクト', 2347400, 2887500, 'ハイブリッド', 'N/A', 'FF', 3940, 1695, 1500, 1365, '傑作コンパクトの最上級グレード！', 'これはダミーテキストです。', 5, '運転しやすい！', '高級志向！', 'https://toyota.jp/info/yaris/special_urbano/'),
('50001', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0000668823.jpg', 'Daihatsu', 'コペン ローブ', 'Normal', 'Celibate', 'オープン', 1980000, 2250000, 'ガソリン(レギュラー)', 'yes', 'FF', 3395, 1475, 1280, 870, '世界最小のオープンカー！', 'これはダミーテキストです。', 2, '運転しやすい！', '唯一無二の特別！', 'https://www.daihatsu.co.jp/lineup/copen/02_grade.htm?type=0&item=1'),
('50002', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001221286.jpg ', 'Suzuki', 'ハスラー', 'Normal', 'Celibate', '軽自動車', 1510000, 1970000, 'ガソリン(レギュラー)', 'N/A', '4WD', 1475, 1680, 860, 0, 'なんでもできちゃうスゴイ奴！', 'これはダミーテキストです。', 4, '遊べるクルマ！', 'たくさん積載！', 'https://www.suzuki.co.jp/car/hustler/'),
('50003', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001064306.jpg ', 'Suzuki', 'ジムニーシエラ', 'Normal', 'Celibate', '軽自動車', 1650000, 2000000, 'ガソリン(レギュラー)', 'N/A', '4WD', 1475, 1725, 1190, 4, '世界最小の本格クロカン！', 'これはダミーテキストです。', 4, '遊べるクルマ！', 'チルキャンピング！', 'https://www.suzuki.co.jp/car/jimny_nomade_jimny_sierra/'),
('50004', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001583813.jpg ', 'Suzuki', 'スペーシアカスタム', 'Normal', 'Celibate', '軽自動車', 1801800, 1925000, 'ハイブリッド', 'yes', '339', 1475, 1785, 950, 850, '便利な軽ハイトワゴン！', 'これはダミーテキストです。', 4, '遊べるクルマ！', 'たくさん積載！', 'https://www.suzuki.co.jp/car/spacia/'),
('60001', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001458816.jpg', 'Toyota', 'クラウン', 'Normal', 'Luxury', 'セダン', 7300000, 8300000, 'ハイブリッド', 'N/A', 'FR', 5030, 1890, 1475, 2020, '伝統と調和のフラッグシップ！', 'これはダミーテキストです', 5, 'オシャレな暮らし！', '高級志向！', 'https://toyota.jp/crown/'),
('60002', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0000758192.jpg', 'Mazda', 'ロードスター(RS 6MT)', 'Normal', 'Celibate', 'オープン', 3679500, 3679500, 'ガソリン(ハイオク)', 'N/A', 'FR', 3915, 1735, 1235, 1040, 'コンパクトなオープンカー！', 'これはダミーテキストです。', 2, '遊べるクルマ！', '高級志向！', 'https://www.mazda.co.jp/cars/roadster/'),
('80001', ' https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001253767.jpg ', 'Toyota', 'ヤリスクロス', 'Normal', 'Family', 'SUV', 206400, 3228500, 'ハイブリッド', 'N/A', 'FF ', 4200, 1765, 1590, 1270, '燃費と積載のいいとこどり！', 'これはダミーテキストです', 5, '家族でお出かけ！', '燃費良好！', 'https://toyota.jp/yariscross/');

-- --------------------------------------------------------

--
-- テーブルの構造 `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `userid` varchar(20) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(16) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT 'https://example.com/default_avatar.png',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `age` tinyint(3) UNSIGNED DEFAULT NULL COMMENT '年齢',
  `gender` enum('男','女','その他') DEFAULT 'その他' COMMENT '性別',
  `birthday` date DEFAULT NULL COMMENT '誕生日'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `users`
--

INSERT INTO `users` (`id`, `userid`, `username`, `password`, `email`, `phone`, `avatar`, `created_at`, `age`, `gender`, `birthday`) VALUES
(1, 'test01', '山田太郎', '12345', 'yamada@example.com', '08012345678', 'https://th.bing.com/th/id/OIP.Dqaa3kuspQWFg5qhAMN5tgAAAA?w=202&h=202&c=7&r=0&o=5&pid=1.7', '2025-02-25 04:33:13', 30, '男', '1993-05-15'),
(2, 'test02', '佐藤花子', '12345', 'sato@example.com', '09087654321', 'https://th.bing.com/th/id/OIP.nfjnpDlU9VXJ-0slSegg6wAAAA?w=197&h=198&c=7&r=0&o=5&pid=1.7', '2025-02-25 04:33:13', 28, '女', '1995-08-20'),
(3, 'test03', '田中一郎', '00001', NULL, NULL, 'https://th.bing.com/th/id/OIP.9wAT7y3Fu1aSN7im35vrSgAAAA?w=205&h=205&c=7&r=0&o=5&pid=1.7', '2025-02-25 04:33:13', 35, '男', '1988-12-10');

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`car_id`);

--
-- テーブルのインデックス `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `userid` (`userid`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
