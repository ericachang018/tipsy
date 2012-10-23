



-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'users'
-- 
-- ---

DROP TABLE IF EXISTS `users`;
        
CREATE TABLE `users` (
  `id` INTEGER primary key AUTOINCREMENT,
  `email` VARCHAR(80) NULL DEFAULT NULL,
  `password` VARCHAR(20) NULL DEFAULT NULL,
  `first_name` VARCHAR(64) NULL DEFAULT NULL,
  `last_name` VARCHAR(80) NULL DEFAULT NULL
);

-- ---
-- Table 'tasks'
-- 
-- ---

DROP TABLE IF EXISTS `tasks`;
        
CREATE TABLE `tasks` (
  `id` INTEGER primary key AUTOINCREMENT,
  `title` MEDIUMTEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `completed_at` DATETIME NULL DEFAULT NULL,
  `user_id` INTEGER NULL DEFAULT NULL,
  FOREIGN KEY(user_id) REFERENCES `users`(`id`)
);

-- ---
-- Foreign Keys 
-- ---



-- ---
-- Table Properties
-- ---

-- ALTER TABLE `users` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `tasks` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `users` (`id`,`email`,`password`,`first_name`,`last_name`) VALUES
-- ('','','','','');
-- INSERT INTO `tasks` (`id`,`title`,`created_at`,`completed_at`,`user_id`) VALUES
-- ('','','','','');

