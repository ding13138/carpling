SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@OLD_COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE TABLE `cars` (
  `car_id` CHAR(5) NOT NULL,
  `brand` VARCHAR(20) NOT NULL,
  `model` VARCHAR(30) NOT NULL,
  `category` VARCHAR(15) NOT NULL,
  `price` INT(11) DEFAULT NULL,
  `fuel_type` VARCHAR(10) NOT NULL,
  `description` TEXT NOT NULL,
  `image` VARCHAR(255) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `cars` (`car_id`, `brand`, `model`, `category`, `price`, `fuel_type`, `description`, `image`) VALUES
('10001', 'Toyota', 'Prius', 'Hybrid', 3700000, 'Hybrid', '燃費が良いハイブリッド車', 'images/prius.jpg'),
('10002', 'Hyundai', 'Inster', 'Electric', 2850000, 'Electric', 'コンパクトな電気自動車', 'images/inster.jpg'),
('10003', 'Honda', 'Prelude', 'Sports', NULL, 'Hybrid', '2025年に復活予定のハイブリッドスポーツカー', 'images/prelude.jpg'),
('10004', 'Suzuki', 'Swift Sport', 'Hatchback', 2800000, 'Gasoline', 'ホットハッチのファイナルエディション', 'images/swift_sport.jpg'),
('10005', 'Toyota', 'Urban Cruiser', 'SUV', 6000000, 'Electric', '電気クロスオーバーSUV', 'images/urban_cruiser.jpg');

ALTER TABLE `cars`
  ADD PRIMARY KEY (`car_id`);

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
