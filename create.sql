BEGIN;
CREATE TABLE `music_music_acg` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `singer` varchar(100) NOT NULL,
    `compose` varchar(100) NOT NULL,
    `album` varchar(200) NOT NULL,
    `time` varchar(100) NOT NULL,
    `source` varchar(400) NOT NULL,
    `label` varchar(500) NOT NULL,
    `mark` varchar(100) NOT NULL,
    `length` varchar(100) NOT NULL,
    `lyrics` longtext NOT NULL,
    `url` varchar(200) NOT NULL,
    `description` longtext NOT NULL,
    `listener` longtext NOT NULL,
    `comment` longtext NOT NULL
)
;

COMMIT;