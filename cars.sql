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
