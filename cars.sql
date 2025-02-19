SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@OLD_COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE TABLE `cars` (
  `car_id` CHAR(5) NOT NULL,
  `car_picture` VARCHAR(255) NOT NULL,
  `brand` VARCHAR(20) NOT NULL,
  `model` VARCHAR(30) NOT NULL,
  `class` VARCHAR(10) NOT NULL,
  `category` VARCHAR(15) NOT NULL,
  `body_type` VARCHAR(15) NOT NULL,
  `price` VARCHAR(50) NOT NULL,
  `fuel_type` VARCHAR(10) NOT NULL,
  `drive` VARCHAR(3) NOT NULL,
  `length` INT(10) NOT NULL,
  `width` INT(10) NOT NULL,
  `height` INT(50) NOT NULL,
  `weight` INT(10) NOT NULL,
  `description_title` TEXT NOT NULL,
  `description` TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `cars` (`car_id`, `car_picture` , `brand`, `model`,`class`, `category` , `body_type`, `price`, `fuel_type`,`drive`,`length`,`width`,`height`,`weight`, `description_title`,`description`) VALUES
('10001', ' ../img/ ', 'Toyota', 'Prius', 'Normal', 'Family', 'クーペ', '2,750,000~4,600,000', 'ハイブリッド(ガソリン)','FF', 4600 , 1780, 1430 , 1400 ,'最新世代のハイブリッドクーペの決定版。',''),
('10002', ' ../img/ ', 'Hyundai', 'Inster', 'Normal', 'Celibate', 'コンパクト',  '2,850,000~3,570,000', '電気','FR', 4600 , 1780, 1430 , 1400 , '韓国発。コンパクトでお手頃な最新EV',''),
('10003', ' ../img/ ', 'Honda', 'Fit', 'Normal', 'Celibate', '1,720,400~2,846,800', 'コンパクト',  'ハイブリッド(ガソリン) / ガソリン(レギュラー)','FF', 3995 , 1695, 1540 , 1030 , '高い燃費性能と室内空間を両立するコンパクトカー',''),
('10004', ' ../img/ ', 'Suzuki', 'Swift', 'Normal', 'Celibate', 'コンパクト',  '2800000', 'ガソリン(レギュラー)', 3860 , 1695 , 1525 , 970 ,'FF', '軽量高性能なコンパクトハッチ',''),
('10005', ' ../img/ ', 'Toyota', 'Urban Cruiser', 'Normal', 'Luxury', 'SUV', '6,000,000', '電気', 4600 , 1780, 1430 , 1400 ,'AWD', '電動クロスオーバーSUV','');


ALTER TABLE `cars`
  ADD PRIMARY KEY (`car_id`);

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
