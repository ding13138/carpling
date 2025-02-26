START TRANSACTION;

CREATE TABLE `cars` (
  `car_id` CHAR(5) NOT NULL,
  `car_picture` VARCHAR(255) NOT NULL,
  `brand` VARCHAR(20) NOT NULL,
  `model` VARCHAR(30) NOT NULL,
  `class` VARCHAR(10) NOT NULL,
  `category` VARCHAR(15) NOT NULL,
  `body_type` VARCHAR(15) NOT NULL,
  `price` VARCHAR(50) NOT NULL,
  `fuel_type` VARCHAR(30) NOT NULL,
  `drive` VARCHAR(3) NOT NULL,
  `length` INT(10) NOT NULL,
  `width` INT(10) NOT NULL,
  `height` INT(10) NOT NULL,
  `weight` INT(10) NOT NULL,
  `description_title` TEXT NOT NULL,
  `description` TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `cars`
  ADD PRIMARY KEY (`car_id`);

INSERT INTO `cars` (`car_id`, `car_picture`, `brand`, `model`, `class`, `category`, `body_type`, `price`, `fuel_type`, `drive`, `length`, `width`, `height`, `weight`, `description_title`, `description`) VALUES
('10001', 'https://toyota.jp/tcv/resources/noah/004_p_001/images/assy/070/zwr90w-apxrb_0_30.png', 'Toyota', 'ノア', 'Normal', 'Family', 'ミニバン', '2,670,000~3,810,000', 'ハイブリッド(ガソリン)/ガソリン(レギュラー)', 'FF', 4695, 1730, 1925, 1640, '上質で広い室内空間を持つトヨタのベーシックミニバン。', 'これはダミーテキストです。'),

('20001', 'https://cdn.autoc-one.jp/images/article/202103/12153801205_2725_o.jpg', 'Toyota', 'カムロード(リバティ 52DB)', 'Normal', 'Luxury', 'キャンピング', '14,350,000~', '軽油', 'AWD', 5230, 2040, 2880, 3570, 'トヨタが送る大型キャンピングカー。', 'これはダミーテキストです。'),

('30001', 'https://toyota.jp/tcv/resources/prius/005_p_003/images/assy/3u5/mxwh61-ahxhb_0_30.png', 'Toyota', 'プリウス', 'Normal', 'Family', 'クーペ', '2,750,000~4,600,000', 'ハイブリッド(ガソリン)', 'FF', 4600, 1780, 1430, 1400, '最新世代のハイブリッドクーペの決定版。', 'これはダミーテキストです。'),

('40001', 'https://www.honda.co.jp/Fit/webcatalog/design/images/home/img_bodycolor_01.jpg', 'Honda', 'フィット', 'Normal', 'Celibate', 'コンパクト', '1,720,400~2,846,800', 'ハイブリッド(ガソリン) / ガソリン(レギュラー)', 'FF', 3995, 1695, 1540, 1030, '高い燃費性能と室内空間を両立するコンパクトカー。', 'これはダミーテキストです。'),

('50001', 'https://www.honda.co.jp/Nbox/common/images/type/cs_turbo_twotone/c_gray_silver.jpg', 'Honda', 'N-BOX', 'Normal', 'Celibate', '軽自動車', '1,689,600~2,382,600', 'ガソリン(レギュラー)', 'FF', 3395, 1475, 1815, 1020, '日本一売れている実用性バツグンの軽自動車。', 'これはダミーテキストです。');

COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

















INSERT INTO `cars` (`car_id`, `car_picture`, `brand`, `model`, `class`, `category`, `body_type`, `price`, `fuel_type`, `drive`, `length`, `width`, `height`, `weight`, `description_title`, `description`) VALUES
('10002', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001546862.jpg', 'Toyota', 'アルファード', 'Normal', 'Family', 'ミニバン', '5,100,000~10,650,000', 'ハイブリッド(ガソリン)/ガソリン(レギュラー)', 'FF/4WD', 4995, 1850, 1945, 2240, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('10003', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001466311.jpg', 'Toyota', 'シエンタ', 'Normal', 'Family', 'ミニバン', '1,900,000~3,230,000', 'ハイブリッド(ガソリン)/ガソリン(レギュラー)', 'FF/4WD', 4260, 1695, 1715, 1695, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('10004', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001635279.jpg', 'Toyota', 'フリード', 'Normal', 'Family', 'ミニバン', '2,500,000~3,600,000', 'ハイブリッド(ガソリン)/ガソリン(レギュラー)', 'FF/4WD', 4310, 1720, 1780, 1520, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('20002', 'https://nutsrv.co.jp/images/lineup/border/index/top_slide01.jpg?202502051446', 'ナッツRV', 'ボーダーバンクス', 'Normal', 'Luxury', 'キャンピング', '17,149,000~18,029,000', '軽油', 'AWD', 6255, 2230, 3020, 4740, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('20003', 'https://nutsrv.co.jp/images/lineup/aletta/index/top_slide01.jpg', 'ナッツRV', 'アレッタ', 'Normal', 'Luxury', 'キャンピング', '9,500,000~11,673,000', '軽油', 'AWD', 4850, 1950, 2850, 3000, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('20004', 'https://nutsrv.co.jp/images/lineup/cresson/index/top_slide01.jpg', 'ナッツRV', 'クレソンジャーニー', 'Normal', 'Luxury', 'キャンピング', '8,584,000~10,817,000', '軽油', 'AWD', 4990, 2080, 2900, 3000, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('30002', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001416092.jpg', '日産', 'フェアレディZ', 'Normal', 'Family', 'クーペ', '5,490,000~9,300,000', 'ガソリン(ハイオク)', 'FR', 4410, 1870, 1315, 1580, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('30003', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001351053.jpg', 'Toyota', 'GR86', 'Normal', 'Family', 'クーペ', '2,930,000~3,990,000', 'ガソリン(ハイオク)', 'FR', 4265, 1775, 1310, 1490, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('30004', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001287745.jpg', 'Toyota', 'GRヤリス', 'Normal', 'Family', 'クーペ', '3,490,000~8,450,000', 'ガソリン(レギュラー)/ガソリン(ハイオク)', 'AWD', 3995, 1805, 1475, 1300, 'これはダミーテキストです。', 'これはダミーテキストです。'),
('40002', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001459500.jpg', 'Honda', 'シビックタイプR', 'Normal', 'Celibate', 'コンパクト', '4,990,000~5,990,000', 'ガソリン(ハイオク)', 'FF', 4595, 1890, 1405, 1430, 'これはダミーテキストです', 'これはダミーテキストです'),
('40003', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001362084.jpg', '日産', 'オーラ', 'Normal', 'Celibate', 'コンパクト', '2,770,000~3,170,000', 'ハイブリッド(ガソリン)', 'FF/4WD', 4120, 1735, 1525, 1420, 'これはダミーテキストです', 'これはダミーテキストです'),
('40004', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001253767.jpg', 'Toyota', 'ヤリスクロス', 'Normal', 'Celibate', 'コンパクト', '1,790,000~3,150,000', 'ハイブリッド(ガソリン)', 'FF/4WD', 4200, 1765, 1590, 1270, 'これはダミーテキストです', 'これはダミーテキストです'),
('50002', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001221286.jpg', 'Honda', 'ハスラー', 'Normal', 'Celibate', '軽自動車', '1,510,000~1,970,000', 'ハイブリッド(ガソリン)', 'FF/4WD', 3395, 1475, 1680, 860, 'これはダミーテキストです', 'これはダミーテキストです。'),
('50003', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001064306.jpg', 'スズキ', 'ジムニー', 'Normal', 'Celibate', '軽自動車', '1,650,000~2,000,000', 'ガソリン(レギュラー)', '4WD', 3395, 1475, 1725, 1190, 'これはダミーテキストです', 'これはダミーテキストです。'),
('50004', 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0001583813.jpg', 'スズキ', 'スペーシアカスタム', 'Normal', 'Celibate', '軽自動車', '1,800,000~2,190,000', 'ハイブリッド(ガソリン)', 'FF/4WD', 3395, 1475, 1785, 950, 'これはダミーテキストです', 'これはダミーテキストです。');
