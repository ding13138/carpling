SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO"; 
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,         -- 自增ID
  `userid` VARCHAR(20) UNIQUE NOT NULL,        -- 账号（唯一）
  `username` VARCHAR(50) NOT NULL,             -- 用户名
  `password` VARCHAR(16) NOT NULL,             -- 密码（支持哈希存储）
  `email` VARCHAR(100) UNIQUE DEFAULT NULL,    -- 邮箱（唯一，可选）
  `phone` VARCHAR(15) UNIQUE DEFAULT NULL,    
  `avatar` VARCHAR(255) DEFAULT 'https://example.com/default_avatar.png', -- 头像URL
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 账户创建时间
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入测试数据
INSERT INTO `users` (`userid`, `username`, `password`, `email`, `phone`, `avatar`) VALUES
('test01', '山田太郎', '12345', 'yamada@example.com', '08012345678', 'https://th.bing.com/th/id/OIP.Dqaa3kuspQWFg5qhAMN5tgAAAA?w=202&h=202&c=7&r=0&o=5&pid=1.7'),
('test02', '佐藤花子', '12345', 'sato@example.com', '09087654321', 'https://th.bing.com/th/id/OIP.nfjnpDlU9VXJ-0slSegg6wAAAA?w=197&h=198&c=7&r=0&o=5&pid=1.7'),
('test03', '田中一郎', '00001', NULL, NULL, 'https://th.bing.com/th/id/OIP.9wAT7y3Fu1aSN7im35vrSgAAAA?w=205&h=205&c=7&r=0&o=5&pid=1.7');

COMMIT;








-- 追加更新

-- 年齢、性別、誕生日カラムを追加
ALTER TABLE `users`
ADD COLUMN `age` TINYINT UNSIGNED DEFAULT NULL COMMENT '年齢',
ADD COLUMN `gender` ENUM('男', '女', 'その他') DEFAULT 'その他' COMMENT '性別',
ADD COLUMN `birthday` DATE DEFAULT NULL COMMENT '誕生日';

-- データを更新
UPDATE `users` SET `age` = 30, `gender` = '男', `birthday` = '1993-05-15' WHERE `userid` = 'test01';
UPDATE `users` SET `age` = 28, `gender` = '女', `birthday` = '1995-08-20' WHERE `userid` = 'test02';
UPDATE `users` SET `age` = 35, `gender` = '男', `birthday` = '1988-12-10' WHERE `userid` = 'test03';